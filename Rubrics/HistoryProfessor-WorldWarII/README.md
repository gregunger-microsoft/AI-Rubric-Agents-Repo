# HistoryProfessor-WorldWarII — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic history professor** responsible for grading formal analytical essays on **World War II (1939–1945)**. It evaluates student submissions against a comprehensive rubric covering the political, economic, and ideological causes of the war; key military turning points; and the lasting geopolitical consequences including the Cold War, the United Nations, and the reshaping of the global order.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Introduction & Thesis Quality | 15% | Arguable thesis about WWII causes, turning points, or consequences; historical context; roadmap |
| Historical Background | 10% | Pre-war political climate, treaties, rise of totalitarian regimes (250–400 words) |
| Cause Analysis Depth | 20% | Multi-causal analysis: political, economic, ideological factors with primary source evidence |
| Turning Points & Strategic Significance | 15% | At least 2 major turning points with dates, strategic reasoning, and thesis connection |
| Source Evidence & Citation Integration | 15% | 2+ primary sources (speeches, treaties, documents) and 3+ secondary scholarly sources |
| Counterargument / Historiographical Debate | 10% | Engagement with alternative historical interpretations and evidence-based rebuttal |
| Personal Reflection + Modern Connection | 5% | Connection to modern geopolitics or conflict; specific historical moment that shaped understanding |
| Writing Quality | 10% | Clarity, organization, mechanics, academic tone |

## Assignment Prompt (Given to Students)

> Write a formal analytical essay that argues a clear thesis about the causes, key turning points, or lasting consequences of World War II. Support your thesis with primary and secondary historical sources and analysis.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Sources**: Minimum 2 primary sources + 3 secondary peer-reviewed sources
- **Citation style**: Chicago, Turabian, or APA
- **Required sections**: Title Page, Introduction + Thesis, Historical Background, Cause Analysis, Turning Points, Consequences & Legacy, Source Evidence, Counterargument, Personal Reflection, Conclusion, Bibliography

## How It Works

1. **Parse** the student submission and map sections to rubric requirements
2. **Check** for integrity violations (plagiarism, fabricated sources, hate speech/Holocaust denial)
3. **Score** each criterion independently (0–5) with cited evidence from the submission
4. **Calculate** weighted total, apply penalties/caps, assign letter grade
5. **Generate** strengths, improvements, and a high-level revision plan
6. **Self-audit** grading accuracy and flag uncertainty for human review

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order, and safety constraints |
| `essay_grading_heuristics_wwii_v1.json` | Full rubric: required sections, scoring criteria, weights, penalties, and self-audit framework |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions for quick reference or prompt configuration |
| `STUDENT HISTORY ESSAY SUBMISSION C.txt` | Sample student submission for testing and validation |
| `README.md` | This file — use case documentation and guidance |

## Key Differentiation from English Professor Agent

- Requires **primary historical documents** (speeches, treaties, diaries) rather than literary quotations
- Evaluates **multi-causal historical analysis** rather than literary themes and symbols
- Includes **historiographical debate** (counterargument from competing historians)
- Applies **sensitivity rules** for WWII-specific topics (Holocaust, war crimes, atomic weapons)
- Uses **Chicago/Turabian** citation style as preferred format
