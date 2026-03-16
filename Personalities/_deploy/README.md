# Personality Agent Deployment

Deploy personality personas as **Azure AI Foundry Prompt Agents** using the Azure AI Projects SDK.

---

## Prerequisites

1. **Azure AI Foundry project** with a deployed model (e.g., `gpt-4o`)
2. **Python 3.10+**
3. **Azure CLI** authenticated (`az login`)
4. **DefaultAzureCredential** access — your identity needs the **Azure AI User** role on the Foundry project

### Install Dependencies

```bash
cd Personalities/_deploy
pip install -r requirements.txt
```

### Configure

Copy the environment template and fill in your project endpoint:

```bash
cp .env.template .env
```

Edit `.env`:

```
PROJECT_ENDPOINT=https://<your-resource>.services.ai.azure.com/api/projects/<your-project>
MODEL_DEPLOYMENT_NAME=gpt-4o
```

Alternatively, set these as environment variables directly.

---

## Usage

### List available personas

```bash
python deploy_personalities.py --list
```

Output:
```
Folder                         Agent Name                                     Enabled
------------------------------ --------------------------------------------- ----------
Chaplain-Hospital              Personality-Chaplain-Hospital                  Yes
Doctor-EmergencyMedicine       Personality-Doctor-EmergencyMedicine            Yes
Electrician-Commercial         Personality-Electrician-Commercial              Yes
...
```

### Deploy all personas

```bash
python deploy_personalities.py --all
```

### Deploy a single persona

```bash
python deploy_personalities.py --persona Lawyer-CriminalDefense
```

### Deploy multiple specific personas

```bash
python deploy_personalities.py --persona Nurse-ICU --persona Doctor-EmergencyMedicine
```

### Delete a deployed agent

```bash
python deploy_personalities.py --delete --persona Nurse-ICU
```

### Delete all deployed agents

```bash
python deploy_personalities.py --delete --all
```

---

## What Gets Deployed

For each persona, the script creates an **Azure AI Foundry Prompt Agent** with:

| Agent Property | Source |
|---------------|--------|
| **Name** | `agent_name` from `deploy-config.json` (e.g., `Personality-Lawyer-CriminalDefense`) |
| **Description** | Extracted from the persona's `DESCRIPTION.md` overview section |
| **Instructions** | Combined from: (1) identity statement, (2) `INSTRUCTION.md` behavioral rules, (3) full `persona.json` embedded as knowledge |
| **Model** | The configured model deployment (default: `gpt-4o`) |

### Idempotent Deployments

- If an agent with the same name **already exists**, the script **updates** it in place
- If the agent **doesn't exist**, the script **creates** it
- This means running the script repeatedly is safe — it will not create duplicates

---

## Configuration

### deploy-config.json

```json
{
    "project_endpoint": "",
    "model_deployment_name": "gpt-4o",
    "personalities_root": "../",
    "agent_name_prefix": "Personality",
    "personas": {
        "Lawyer-CriminalDefense": {
            "enabled": true,
            "agent_name": "Personality-Lawyer-CriminalDefense"
        }
    }
}
```

| Field | Description |
|-------|-------------|
| `project_endpoint` | Azure AI Foundry project endpoint (overridden by `PROJECT_ENDPOINT` env var) |
| `model_deployment_name` | Model to use for all agents (overridden by `MODEL_DEPLOYMENT_NAME` env var) |
| `personalities_root` | Relative path from `_deploy/` to the `Personalities/` folder |
| `agent_name_prefix` | Default prefix for agent names |
| `personas.<folder>.enabled` | Set to `false` to skip a persona when deploying `--all` |
| `personas.<folder>.agent_name` | Custom agent name (overrides prefix + folder convention) |

### Environment Variables

Environment variables take precedence over `deploy-config.json`:

| Variable | Purpose |
|----------|---------|
| `PROJECT_ENDPOINT` | Azure AI Foundry project endpoint |
| `MODEL_DEPLOYMENT_NAME` | Model deployment name |

---

## File Structure

```
_deploy/
├── deploy_personalities.py    # Main deployment script
├── deploy-config.json         # Persona registry and deployment settings
├── requirements.txt           # Python dependencies
├── .env.template              # Environment variable template
└── README.md                  # This file
```

---

## How the Agent Instructions Are Built

The deployment script assembles the agent's system instructions from three sources, in order:

1. **Identity statement** — A one-line persona identity derived from `persona.json` (name, age, occupation, location)
2. **INSTRUCTION.md** — The full behavioral rules document (role adoption, constraints, triggers, taboos, moral red lines, dialogue calibration, quality guardrails)
3. **persona.json** — The complete persona JSON embedded as a fenced code block, serving as the agent's authoritative knowledge source

This structure gives the agent a clear role, behavioral boundaries, and deep reference data for consistent character embodiment.
