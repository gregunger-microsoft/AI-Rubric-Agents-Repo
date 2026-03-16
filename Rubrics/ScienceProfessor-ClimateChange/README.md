# ScienceProfessor-ClimateChange — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic science professor** responsible for grading formal research reports on **climate change**. It evaluates student submissions against a comprehensive rubric covering the scientific mechanisms of climate change (greenhouse effect, carbon cycle), evidence and data analysis from peer-reviewed sources, ecological and societal impacts, and evaluation of mitigation strategies.

## Problem It Solves

Science instructors face the challenge of grading research reports that require both **scientific accuracy** and **analytical depth**. Students must demonstrate they can interpret real data, cite peer-reviewed sources, distinguish between scientific consensus and contested findings, and propose evidence-based mitigation strategies. This agent automates the rigorous evaluation of these skills against a transparent, weighted rubric — ensuring **consistent, fair, and defensible grades** across large class sections.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Introduction & Thesis Quality | 10% | Clear research question/thesis about climate change; scientific context |
| Scientific Background Accuracy | 15% | Greenhouse effect, key gases, historical temperature/CO₂ data |
| Evidence & Data Analysis Depth | 25% | At least 2 data sets cited; interpretation of trends; connection to thesis |
| Impacts Assessment | 15% | Ecological + societal impacts; regional variation |
| Mitigation Strategy Evaluation | 10% | At least 2 strategies evaluated for feasibility/effectiveness |
| Scientific Debate & Counterargument | 10% | Engagement with skeptical claims; evidence-based rebuttal |
| Personal Reflection | 5% | Changed understanding; future scientific/policy challenges |
| Writing Quality & Scientific Communication | 10% | Clarity, organization, proper use of scientific terminology |

## Assignment Prompt (Given to Students)

> Write a formal research report that argues a clear thesis about the causes, mechanisms, or impacts of climate change. Support your thesis with peer-reviewed scientific evidence, data analysis, and critical evaluation of current mitigation strategies.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Sources**: Minimum 5 peer-reviewed scientific sources (IPCC reports acceptable)
- **Citation style**: APA or CSE
- **Required sections**: Title Page, Abstract, Introduction + Thesis, Scientific Background, Evidence & Data Analysis, Impacts Assessment, Mitigation Strategies, Counterargument, Personal Reflection, Conclusion, References

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `report_grading_heuristics_climate_change_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT SCIENCE REPORT SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Data-centric**: Requires students to cite and interpret actual data sets and statistics
- **Scientific accuracy**: Factual errors in climate science are penalized, not just weak writing
- **Abstract required**: Students must write a structured abstract summarizing their report
- **Mitigation evaluation**: Students must go beyond describing problems to evaluating solutions
- Emphasizes **peer-reviewed sources** over general references
