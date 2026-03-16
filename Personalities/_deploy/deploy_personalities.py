"""
deploy_personalities.py — Deploy personality personas as Azure AI Foundry Agents.

Usage:
    python deploy_personalities.py --all                         Deploy all enabled personas
    python deploy_personalities.py --persona Lawyer-CriminalDefense   Deploy one persona
    python deploy_personalities.py --list                        List available personas
    python deploy_personalities.py --delete --all                Delete all deployed agents
    python deploy_personalities.py --delete --persona Nurse-ICU  Delete one agent

Requires:
    pip install azure-ai-projects azure-identity python-dotenv

Environment variables (or .env file):
    PROJECT_ENDPOINT          Azure AI Foundry project endpoint
    MODEL_DEPLOYMENT_NAME     Model deployment name (default: gpt-4o)
"""

import argparse
import json
import os
import sys
from pathlib import Path

from azure.ai.agents.models import (
    FileSearchToolDefinition,
    FileSearchToolResource,
    FilePurpose,
    ToolResources,
)
from azure.ai.projects import AIProjectClient
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG = SCRIPT_DIR / "deploy-config.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_config(config_path: Path) -> dict:
    """Load and validate the deployment configuration."""
    if not config_path.exists():
        print(f"ERROR: Config file not found: {config_path}")
        sys.exit(1)
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_endpoint(config: dict) -> str:
    """Resolve the project endpoint from env vars or config."""
    endpoint = os.environ.get("PROJECT_ENDPOINT") or config.get("project_endpoint")
    if not endpoint:
        print("ERROR: PROJECT_ENDPOINT not set. Set it as an environment variable or in deploy-config.json.")
        sys.exit(1)
    return endpoint


def resolve_model(config: dict) -> str:
    """Resolve the model deployment name from env vars or config."""
    return os.environ.get("MODEL_DEPLOYMENT_NAME") or config.get("model_deployment_name", "gpt-4o")


def load_persona(personalities_root: Path, folder_name: str) -> dict:
    """Load and parse persona.json for a given personality folder."""
    persona_path = personalities_root / folder_name / "persona.json"
    if not persona_path.exists():
        print(f"ERROR: persona.json not found at {persona_path}")
        sys.exit(1)
    with open(persona_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_instructions(personalities_root: Path, folder_name: str) -> str:
    """Load INSTRUCTION.md for a given personality folder."""
    instruction_path = personalities_root / folder_name / "INSTRUCTION.md"
    if not instruction_path.exists():
        print(f"WARNING: INSTRUCTION.md not found at {instruction_path}, using fallback instructions.")
        return ""
    with open(instruction_path, "r", encoding="utf-8") as f:
        return f.read()


def load_description(personalities_root: Path, folder_name: str) -> str:
    """Load DESCRIPTION.md for a given personality folder."""
    desc_path = personalities_root / folder_name / "DESCRIPTION.md"
    if not desc_path.exists():
        return ""
    with open(desc_path, "r", encoding="utf-8") as f:
        return f.read()


def build_agent_instructions(persona_data: dict, instruction_md: str) -> str:
    """
    Build the system instructions for the agent.

    Combines a concise identity statement with the INSTRUCTION.md behavioral rules.
    The full persona.json is attached separately as a Knowledge file (vector store).
    """
    persona = persona_data["personas"][0]
    name = persona["identity"]["fictional_name"]
    occupation = persona["occupation_profile"]["occupation"]

    parts = []

    # Lead with a concise identity statement
    parts.append(f"You are {name}, a {persona['identity']['age']}-year-old {occupation}.")
    parts.append(f"Location: {persona['location_context']['region_or_state']}, {persona['location_context']['country']}.")
    parts.append("")
    parts.append("Your complete character specification (identity, psychometrics, values,")
    parts.append("backstory, scenario hooks, dialogue calibration) is provided in the")
    parts.append("attached persona.json knowledge file. Use it as your authoritative")
    parts.append("reference for all persona details. Search it whenever you need to")
    parts.append("recall specific traits, backstory events, or behavioral constraints.")
    parts.append("")

    # Include the INSTRUCTION.md as behavioral rules
    if instruction_md:
        parts.append("# BEHAVIORAL RULES AND INSTRUCTIONS")
        parts.append("")
        parts.append(instruction_md)

    return "\n".join(parts)


def build_agent_description(persona_data: dict, description_md: str) -> str:
    """Build a concise agent description from persona data."""
    persona = persona_data["personas"][0]
    name = persona["identity"]["fictional_name"]
    occupation = persona["occupation_profile"]["occupation"]
    age = persona["identity"]["age"]
    location = persona["location_context"]["region_or_state"]

    if description_md:
        # Extract just the first paragraph from DESCRIPTION.md (skip the title)
        lines = description_md.strip().split("\n")
        summary_lines = []
        started = False
        for line in lines:
            if line.startswith("### Overview"):
                started = True
                continue
            if started:
                if line.startswith("#") or line.startswith("---"):
                    break
                if line.strip():
                    summary_lines.append(line.strip())
        if summary_lines:
            return " ".join(summary_lines)[:500]

    # Fallback to persona backstory
    backstory = persona.get("backstory", {}).get("one_paragraph_summary", "")
    if backstory:
        return backstory[:500]

    return f"{name}, {age}, {occupation} based in {location}."


# ---------------------------------------------------------------------------
# Agent CRUD operations
# ---------------------------------------------------------------------------


def upload_persona_knowledge(
    client: AIProjectClient,
    personalities_root: Path,
    folder_name: str,
    agent_name: str,
) -> str:
    """
    Upload persona.json as a file and create a vector store for it.
    Returns the vector store ID.
    """
    persona_path = personalities_root / folder_name / "persona.json"

    # Upload the file
    print(f"  Uploading {persona_path.name} as knowledge file...")
    uploaded_file = client.agents.files.upload_and_poll(
        file_path=str(persona_path),
        purpose=FilePurpose.AGENTS,
    )
    print(f"  Uploaded file: {uploaded_file.id} ({uploaded_file.filename})")

    # Create a vector store containing the file
    vector_store_name = f"{agent_name}-knowledge"
    print(f"  Creating vector store: {vector_store_name}...")
    vector_store = client.agents.vector_stores.create_and_poll(
        name=vector_store_name,
        file_ids=[uploaded_file.id],
    )
    print(f"  Vector store created: {vector_store.id} (status: {vector_store.status})")

    return vector_store.id


def deploy_single_persona(
    client: AIProjectClient,
    model: str,
    personalities_root: Path,
    folder_name: str,
    agent_name: str,
) -> str:
    """Deploy a single persona as an Azure AI Foundry agent. Returns agent ID."""

    print(f"\n{'='*60}")
    print(f"  Deploying: {folder_name}")
    print(f"  Agent name: {agent_name}")
    print(f"{'='*60}")

    # Load persona files
    persona_data = load_persona(personalities_root, folder_name)
    instruction_md = load_instructions(personalities_root, folder_name)
    description_md = load_description(personalities_root, folder_name)

    # Build agent parameters
    instructions = build_agent_instructions(persona_data, instruction_md)
    description = build_agent_description(persona_data, description_md)

    persona_name = persona_data["personas"][0]["identity"]["fictional_name"]
    print(f"  Persona: {persona_name}")
    print(f"  Instructions length: {len(instructions)} chars")
    print(f"  Description length: {len(description)} chars")

    # Upload persona.json as a knowledge file (vector store)
    vector_store_id = upload_persona_knowledge(
        client, personalities_root, folder_name, agent_name
    )

    # Build tool and resource definitions for file search knowledge
    file_search_tool = FileSearchToolDefinition()
    tool_resources = ToolResources(
        file_search=FileSearchToolResource(vector_store_ids=[vector_store_id])
    )

    # Check if agent already exists by listing and matching name
    existing_agent_id = find_agent_by_name(client, agent_name)

    if existing_agent_id:
        print(f"  Agent already exists (ID: {existing_agent_id}). Updating...")
        agent = client.agents.update_agent(
            agent_id=existing_agent_id,
            model=model,
            name=agent_name,
            instructions=instructions,
            description=description,
            tools=[file_search_tool],
            tool_resources=tool_resources,
        )
        print(f"  UPDATED agent: {agent.id}")
        return agent.id
    else:
        agent = client.agents.create_agent(
            model=model,
            name=agent_name,
            instructions=instructions,
            description=description,
            tools=[file_search_tool],
            tool_resources=tool_resources,
        )
        print(f"  CREATED agent: {agent.id}")
        return agent.id


def find_agent_by_name(client: AIProjectClient, agent_name: str) -> str | None:
    """Find an existing agent by name. Returns agent_id or None."""
    try:
        for agent in client.agents.list_agents():
            if agent.name == agent_name:
                return agent.id
    except HttpResponseError:
        pass
    return None


def delete_single_agent(client: AIProjectClient, agent_name: str) -> bool:
    """Delete an agent by name. Returns True if deleted."""
    agent_id = find_agent_by_name(client, agent_name)
    if not agent_id:
        print(f"  Agent '{agent_name}' not found. Nothing to delete.")
        return False

    client.agents.delete_agent(agent_id)
    print(f"  DELETED agent '{agent_name}' (ID: {agent_id})")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def list_personas(config: dict, personalities_root: Path) -> None:
    """List all available personas and their deployment status."""
    print(f"\n{'Folder':<30} {'Agent Name':<45} {'Enabled':<10}")
    print(f"{'-'*30} {'-'*45} {'-'*10}")
    for folder_name, settings in sorted(config["personas"].items()):
        agent_name = settings.get("agent_name", f"{config.get('agent_name_prefix', 'Personality')}-{folder_name}")
        enabled = settings.get("enabled", True)
        persona_exists = (personalities_root / folder_name / "persona.json").exists()
        status = "Yes" if enabled else "No"
        if not persona_exists:
            status += " (MISSING)"
        print(f"{folder_name:<30} {agent_name:<45} {status:<10}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Deploy personality personas as Azure AI Foundry Agents.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python deploy_personalities.py --list
  python deploy_personalities.py --all
  python deploy_personalities.py --persona Lawyer-CriminalDefense
  python deploy_personalities.py --persona Nurse-ICU --persona Doctor-EmergencyMedicine
  python deploy_personalities.py --delete --all
  python deploy_personalities.py --delete --persona Nurse-ICU
        """,
    )
    parser.add_argument("--all", action="store_true", help="Deploy all enabled personas")
    parser.add_argument("--persona", action="append", dest="personas", metavar="FOLDER",
                        help="Deploy a specific persona by folder name (repeatable)")
    parser.add_argument("--list", action="store_true", help="List available personas and exit")
    parser.add_argument("--delete", action="store_true", help="Delete agent(s) instead of deploying")
    parser.add_argument("--config", type=str, default=str(DEFAULT_CONFIG),
                        help=f"Path to deploy-config.json (default: {DEFAULT_CONFIG})")

    args = parser.parse_args()

    # Load env and config
    load_dotenv()
    config = load_config(Path(args.config))
    personalities_root = (SCRIPT_DIR / config.get("personalities_root", "../")).resolve()

    # Handle --list
    if args.list:
        list_personas(config, personalities_root)
        return

    # Validate we have something to do
    if not args.all and not args.personas:
        parser.print_help()
        print("\nERROR: Specify --all or --persona <FOLDER>")
        sys.exit(1)

    # Resolve which personas to operate on
    if args.all:
        targets = {
            folder: settings
            for folder, settings in config["personas"].items()
            if settings.get("enabled", True)
        }
    else:
        targets = {}
        for folder in args.personas:
            if folder not in config["personas"]:
                print(f"ERROR: '{folder}' not found in deploy-config.json. Available: {', '.join(config['personas'].keys())}")
                sys.exit(1)
            targets[folder] = config["personas"][folder]

    # Resolve connection parameters
    endpoint = resolve_endpoint(config)
    model = resolve_model(config)

    print(f"\nProject endpoint: {endpoint}")
    print(f"Model deployment: {model}")
    print(f"Personalities root: {personalities_root}")
    print(f"Operation: {'DELETE' if args.delete else 'DEPLOY'}")
    print(f"Targets: {len(targets)} persona(s)")

    # Initialize client
    credential = DefaultAzureCredential()
    client = AIProjectClient(endpoint=endpoint, credential=credential)

    results = {"success": [], "failed": []}

    for folder_name, settings in sorted(targets.items()):
        agent_name = settings.get("agent_name", f"{config.get('agent_name_prefix', 'Personality')}-{folder_name}")

        try:
            if args.delete:
                deleted = delete_single_agent(client, agent_name)
                if deleted:
                    results["success"].append(folder_name)
                else:
                    results["failed"].append((folder_name, "Not found"))
            else:
                agent_id = deploy_single_persona(
                    client=client,
                    model=model,
                    personalities_root=personalities_root,
                    folder_name=folder_name,
                    agent_name=agent_name,
                )
                results["success"].append(folder_name)
        except HttpResponseError as e:
            print(f"\n  ERROR deploying {folder_name}: {e.status_code} — {e.message}")
            results["failed"].append((folder_name, f"{e.status_code}: {e.message}"))
        except Exception as e:
            print(f"\n  ERROR deploying {folder_name}: {e}")
            results["failed"].append((folder_name, str(e)))

    # Summary
    action = "Deleted" if args.delete else "Deployed"
    print(f"\n{'='*60}")
    print(f"  SUMMARY")
    print(f"{'='*60}")
    print(f"  {action} successfully: {len(results['success'])}")
    for name in results["success"]:
        print(f"    + {name}")
    if results["failed"]:
        print(f"  Failed: {len(results['failed'])}")
        for name, reason in results["failed"]:
            print(f"    x {name}: {reason}")
    print()


if __name__ == "__main__":
    main()
