# AI Rubric Agents Repository

## The Problem

Every organization evaluates unstructured work — essays, proposals, reports, resumes, code reviews, compliance documents, support tickets, grant applications. Today, that evaluation is:

- **Inconsistent**: Two reviewers score the same submission differently depending on mood, fatigue, or personal bias
- **Slow**: A professor grading 120 essays spends 15–20 minutes each. A hiring manager reviewing 200 resumes skims for 6 seconds and misses qualified candidates
- **Unscalable**: Quality evaluation requires domain expertise, and domain experts don't scale
- **Opaque**: When someone receives a grade or a rejection, they rarely get specific, evidence-based feedback tied to explicit criteria
- **Unrepeatable**: Rubrics exist on paper but aren't enforced systematically — they're guidelines, not guarantees

The core challenge isn't AI capability. **The challenge is giving AI agents enough structured knowledge to evaluate like a domain expert — consistently, defensibly, and at scale.**

---

## The Solution

This repository provides a **proven, repeatable pattern** for building AI evaluation agents using **low-code tools and knowledge source files** — no custom code, no fine-tuning, no model training required.

Each agent is powered by **three JSON/text knowledge source files** that can be uploaded directly into **Microsoft Copilot Studio**, **Azure AI Agent Service**, **OpenAI Assistants**, or any AI platform that supports knowledge grounding:

| File | What It Does |
|------|-------------|
| **Instruction Set JSON** | Defines the agent's role, behavioral rules, grading philosophy, and mandatory 6-step execution order |
| **Grading Heuristics JSON** | Contains the complete rubric: assignment prompt, submission requirements, scoring criteria with weights, penalty rules, and a self-audit framework |
| **Agent Instructions TXT** | Plain-text behavioral summary that works as a system prompt in any AI platform |

**That's it.** Three files. Upload them as knowledge sources. The agent is ready to evaluate.

---

## Why This Matters: The 30-Second Rubric

The most powerful aspect of this pattern is **how fast you can create new agents**.

Every agent in this repository was generated from the same template structure. Once you understand the pattern, creating a new evaluation agent for any domain takes **under 30 seconds**:

1. Copy an existing agent's three files
2. Replace the domain-specific content (topic, criteria, weights, penalties)
3. Upload to Copilot Studio as knowledge sources
4. Done — the agent inherits the entire evaluation architecture automatically

**You are not building AI agents. You are authoring rubrics.** The AI agent architecture is already solved. The 6-step workflow, the self-audit framework, the evidence-grounding rules, the penalty system, the confidence scoring — all of that is baked into the template. You just fill in the domain expertise.

This means **any subject matter expert** — a professor, a hiring manager, a compliance officer, a grant reviewer — can create a production-quality evaluation agent by editing a JSON file. No prompt engineering certification required.

---

## The Architecture

### 6-Step Mandatory Evaluation Workflow

Every agent in this repository follows the same execution pipeline, enforced by the instruction set:

```
Step 1: Parse Submission     → Extract text, detect sections, compute word counts
Step 2: Integrity Checks     → Verify required sections, apply word-count penalties, flag plagiarism
Step 3: Criterion Scoring    → Score each criterion (0–5) independently with cited evidence
Step 4: Score Calculation    → Apply rubric weights, penalties, and caps → final percentage + letter grade
Step 5: Feedback Generation  → Strengths, improvement areas, and a revision plan
Step 6: Accuracy Self-Audit  → Confidence level across 5 dimensions + human review flag
```

### Built-In Self-Audit (The Differentiator)

Most AI evaluation tools give you a score. This pattern gives you a score **plus a reliability assessment of that score**:

| Audit Dimension | What It Checks |
|----------------|---------------|
| Rubric Adherence | Did every score map to an explicit rubric rule? |
| Evidence Grounding | Is every score justified by specific text from the submission? |
| Internal Consistency | Do the individual scores align logically with the overall grade? |
| Uncertainty Handling | Were edge cases flagged rather than guessed through? |
| Safety & Bias | Was the evaluation free from bias, unprofessional language, or policy violations? |

**This is the pattern missing from most AI agent implementations.** The agent doesn't just evaluate — it evaluates its own evaluation, tells you how confident it is, and flags when a human should review.

### The Evidence-or-Lower Rule

Every agent enforces one absolute rule:

> *If a score cannot be confidently justified using the rubric and the submission text, the agent must lower the score and record uncertainty.*

This eliminates hallucinated justifications. The agent cannot invent reasons to give a higher score. If the evidence isn't there, the score goes down and the uncertainty gets logged. This is what makes the output defensible.

---

## Copilot Studio Integration

This pattern was designed for **Microsoft Copilot Studio** and low-code AI agent platforms:

### How to Deploy

1. **Create a new agent** in Copilot Studio
2. **Upload the three knowledge source files** (instruction set JSON, heuristics JSON, instructions TXT)
3. **Set the system prompt** to reference the uploaded knowledge sources as authoritative and canonical
4. **Add a topic** that accepts student/user submissions as input
5. **Test** with the included sample submission file

### Why Copilot Studio Is the Right Fit

- **No code required** — the entire agent is defined by knowledge source files
- **Version control** — update the rubric JSON, re-upload, and the agent immediately uses the new criteria
- **Multi-channel deployment** — publish to Teams, web, email, or embed in a learning management system
- **Enterprise security** — runs within your Microsoft 365 tenant with existing compliance and data residency controls
- **Scalability** — one agent can grade thousands of submissions with identical consistency
- **Audit trail** — every evaluation follows the same 6-step pipeline, producing structured output that can be logged and reviewed

### Beyond Copilot Studio

The same knowledge source files work with:
- **Azure AI Agent Service** — for programmatic agent orchestration
- **OpenAI Assistants API** — upload as retrieval files
- **Semantic Kernel / LangChain** — use as grounding documents in RAG pipelines
- **Any LLM with system prompts** — the instructions TXT file works as a standalone system prompt

---

## What's in This Repository

### 13 Ready-to-Use Evaluation Agents

| Agent | Domain | What It Evaluates |
|-------|--------|-------------------|
| **EnglishProfessor-MaryShelleys** | English Literature | Book reports on *Frankenstein* — thesis, textual evidence, thematic analysis |
| **HistoryProfessor-WorldWarII** | History | WWII essays — causes, major events, geopolitical consequences, historiography |
| **ScienceProfessor-ClimateChange** | Environmental Science | Climate research reports — peer-reviewed data, impact analysis, mitigation strategies |
| **MathProfessor-CalculusProofs** | Mathematics | Formal proofs — logical validity, theorem application, notation precision |
| **PhilosophyProfessor-Ethics** | Philosophy | Ethics essays — framework comparison, counterarguments, principle of charity |
| **CSProfessor-DataStructures** | Computer Science | Data structures papers — Big-O accuracy, code correctness, trade-off reasoning |
| **ArtProfessor-RenaissancePeriod** | Art History | Renaissance essays — formal, iconographic, and contextual analysis of artworks |
| **MusicProfessor-ClassicalComposition** | Music Theory | Composition analysis — sonata form, harmonic analysis, expressive interpretation |
| **BusinessProfessor-CaseStudy** | Business Strategy | Case studies — SWOT, Porter's Five Forces, alternatives, risk assessment |
| **PsychologyProfessor-ResearchMethods** | Psychology | Research proposals — APA format, methodology, statistics plan, ethics |
| **LawProfessor-ConstitutionalLaw** | Law | Legal memoranda — IRAC method, case law, Bluebook citations, counterarguments |
| **PriestCommunication** | Seminary / Homiletics | Homilies & pastoral letters — exegesis, rhetoric, pastoral sensitivity |
| **ResumeJudger** | Career Services | Resumes — role targeting, quantified accomplishments, ATS compatibility |

Each agent includes a **sample student submission** so you can validate behavior immediately after deployment.

---

## Beyond Academia: Where This Pattern Applies

The academic grading use case is a demonstration. The pattern generalizes to **any structured evaluation problem**:

### Corporate & Enterprise

| Use Case | How It Works |
|----------|-------------|
| **Proposal Scoring** | Evaluate vendor proposals against RFP requirements with weighted criteria and evidence-based scoring |
| **Code Review** | Grade pull requests for security, readability, test coverage, and architectural alignment |
| **Compliance Auditing** | Assess regulatory filings against compliance checklists with penalty rules for missing elements |
| **Performance Reviews** | Evaluate self-assessments against role-specific competency frameworks |
| **Grant Applications** | Score research grant proposals against funding criteria with structured reviewer feedback |

### Hiring & Talent

| Use Case | How It Works |
|----------|-------------|
| **Resume Screening** | Score resumes against job-specific requirements with quantified accomplishment weighting |
| **Cover Letter Evaluation** | Assess targeting, enthusiasm, and qualification mapping to the specific role |
| **Technical Assessment Grading** | Evaluate coding challenges or case study responses against detailed rubrics |
| **Interview Scorecard** | Structure post-interview evaluations against competency criteria with evidence requirements |

### Customer & Support

| Use Case | How It Works |
|----------|-------------|
| **Support Ticket Quality** | Evaluate agent responses for completeness, tone, accuracy, and resolution quality |
| **Content Moderation** | Score user-generated content against community guidelines with escalation thresholds |
| **Documentation Review** | Assess technical documentation for completeness, accuracy, and accessibility |

### Healthcare & Legal

| Use Case | How It Works |
|----------|-------------|
| **Clinical Note Review** | Evaluate medical documentation for completeness, coding accuracy, and compliance |
| **Legal Brief Assessment** | Score briefs for argument structure, authority citation, and persuasiveness |
| **Policy Analysis** | Evaluate policy proposals against impact criteria with stakeholder consideration scoring |

---

## Key Advantages

### For Organizations
- **Consistency at scale** — 1,000 evaluations with identical standards, not 1,000 different interpretations
- **Speed** — what takes a human reviewer 15–20 minutes takes the agent under 60 seconds
- **Transparency** — every score is justified by specific evidence from the submission, creating a defensible audit trail
- **Cost reduction** — domain experts author rubrics once; the agent applies them indefinitely
- **Continuous improvement** — update the heuristics JSON to adjust criteria, weights, or penalties instantly

### For AI Developers
- **No model training** — works with any foundation model through knowledge grounding
- **No prompt engineering heroics** — the behavioral rules and rubric are in structured JSON, not fragile prompt text
- **Separation of concerns** — agent behavior (instruction set) is decoupled from evaluation criteria (heuristics), enabling independent versioning
- **Built-in guardrails** — the evidence-or-lower rule, self-audit framework, and human-review flags are architectural, not afterthoughts
- **Testable** — every agent ships with a sample submission; automated validation is straightforward

### For Subject Matter Experts
- **Author rubrics, not code** — if you can fill in a JSON template, you can build an evaluation agent
- **30-second deployment** — copy, customize, upload, test
- **Domain expertise preserved** — your grading standards are encoded in a structured, shareable, version-controlled format instead of living in your head
- **Iterate instantly** — change a weight, add a penalty, adjust a criterion — re-upload and the agent adapts immediately

---

## Getting Started

### Create Your First Custom Agent in 4 Steps

1. **Pick a template** — Choose the agent closest to your use case from the 13 included
2. **Edit the heuristics JSON** — Replace the topic, criteria, weights, and penalties with your domain's requirements
3. **Edit the instruction set JSON** — Adjust the role definition and any domain-specific rules
4. **Upload to Copilot Studio** — Add the three files as knowledge sources, set the system prompt, and test

### Template Anatomy (What to Customize)

```
heuristics JSON
├── assignment.topic          ← Your evaluation topic
├── assignment.promptToStudent ← The instructions given to the person being evaluated
├── submissionRequirements    ← Word counts, formatting, required sections
├── scoring.criteria[]        ← Your criteria with names, weights, and score types
└── accuracyAssessment        ← Self-audit dimensions (usually keep as-is)

instruction set JSON
├── roleDefinition.role       ← "Academic Professor" → "Compliance Auditor" etc.
├── roleDefinition.audience   ← Who is being evaluated
├── gradingPhilosophy         ← Domain-specific evaluation principles
└── mandatoryExecutionOrder   ← 6-step workflow (usually keep as-is)
```

The structural scaffolding — execution order, self-audit, evidence rules, output schema — stays the same across every agent. You only customize the domain-specific content.

---

## Summary

The AI Rubric Agents Repository is not a collection of prompts. It is a **low-code evaluation architecture** that turns structured rubrics into consistent, scalable, self-auditing AI agents.

- **13 production-ready agents** across 13 disciplines
- **3 files per agent** — upload as knowledge sources to Copilot Studio or any AI platform
- **30-second customization** — copy a template, edit the domain content, deploy
- **Built-in self-audit** — every evaluation includes a confidence assessment and human-review flag
- **Evidence-or-lower rule** — no hallucinated justifications, ever
- **Generalizable pattern** — academia is the demo; the architecture works for any structured evaluation

**The bottleneck in AI evaluation isn't the model. It's the rubric. This repository solves the rubric.**
