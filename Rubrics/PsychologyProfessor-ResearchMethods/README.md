# PsychologyProfessor-ResearchMethods — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic psychology professor** responsible for grading formal **research proposals and methods papers** in APA 7th edition format. It evaluates student submissions that propose a psychological study complete with literature review, hypothesis, participants, materials, procedure, research design, statistical analysis plan, ethical considerations, and limitations. The agent is suitable for undergraduate Research Methods courses as well as introductory graduate-level methodology classes.

## Problem It Solves

Research methods papers are among the most complex assignments to grade in psychology. Students must demonstrate competency across multiple dimensions simultaneously: **literature synthesis**, **hypothesis formulation**, **experimental design**, **statistical reasoning**, **ethical awareness**, and **APA format compliance**. Errors in any dimension—an inappropriate statistical test, unaddressed confounding variables, missing IRB considerations—reflect fundamental misunderstandings. This agent systematically evaluates all dimensions, ensuring no critical methodological flaw goes undetected and that grading standards remain consistent across all submissions.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Literature Review & Research Gap | 20% | 8+ peer-reviewed sources reviewed; clear gap identified |
| Hypothesis Clarity & Testability | 10% | Specific, testable hypothesis derived from the literature |
| Methodology Quality | 25% | Participants, materials/measures, procedure with detail |
| Research Design & Statistical Analysis Plan | 15% | Design type; IV/DV; appropriate statistical tests justified |
| Ethical Considerations | 10% | Informed consent, IRB, debriefing, risk mitigation |
| Limitations & Future Directions | 10% | 2+ limitations; threats to validity; future research |
| Writing Quality & APA Compliance | 10% | APA 7th edition formatting; clarity; scientific writing style |

## Assignment Prompt (Given to Students)

> Write a formal research proposal in APA format for a psychological study. Include a literature review establishing context and a research gap, a clearly stated hypothesis, a detailed methodology section (participants, materials, procedure, design), a proposed statistical analysis plan, ethical considerations, and a discussion of limitations.

## Requirements

- **Word count**: 2,000–2,500 words (hard limits: 1,500–3,000)
- **Sources**: Minimum 8 peer-reviewed psychology journal articles
- **Format**: APA 7th edition (running head, Times New Roman 12pt, page numbers)
- **Required sections**: Title Page, Abstract, Introduction/Literature Review, Method (Participants, Materials, Procedure, Design & Analysis), Ethics, Limitations, Conclusion, References

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `research_proposal_grading_heuristics_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT RESEARCH PROPOSAL SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Methodology-focused**: Highest weight (25%) on methodology quality (participants, materials, procedure)
- **APA-strict**: APA 7th edition compliance is graded as a separate criterion
- **Statistics-aware**: Evaluates whether proposed statistical tests match the research design
- **Ethics-mandatory**: Informed consent, IRB, and debriefing must be addressed
- **Literature-heavy**: Requires 8+ peer-reviewed sources in the literature review
- **Hypothesis-testable**: Hypothesis must be specific, directional, and derivable from the literature
