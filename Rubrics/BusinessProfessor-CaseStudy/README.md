# BusinessProfessor-CaseStudy — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic business professor** responsible for grading formal **case study analyses**. It evaluates student submissions that analyze a real-world business scenario, apply strategic frameworks (SWOT, Porter's Five Forces, PESTLE, Value Chain, BCG Matrix), develop actionable recommendations, and assess implementation risks. This agent is designed for both undergraduate business courses and MBA-level strategy classes.

## Problem It Solves

Business case study assignments are notoriously difficult to grade consistently. Students often confuse **description** with **analysis**, present **opinions as recommendations** without framework support, or propose solutions that ignore the financial and competitive data in the case. This agent systematically verifies that students have:
- Correctly identified the central strategic problem
- Applied at least two recognized frameworks with case-specific evidence
- Developed multiple strategic alternatives before recommending one
- Addressed implementation risks and contingencies

This ensures **rigorous, consistent, framework-grounded grading** across large business class sections.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Problem Identification & Framing | 15% | Central strategic problem; context; stakeholders |
| Situational Analysis & Framework Application | 25% | 2+ frameworks applied with case data; industry context |
| Strategic Alternatives Quality | 15% | At least 3 options with pros/cons; evaluation criteria |
| Recommendation Quality & Justification | 20% | Specific action; tied to analysis; implementation timeline |
| Risk Assessment | 10% | 2+ risks identified; mitigation strategies; contingencies |
| Personal Reflection / Key Takeaways | 5% | Lessons learned; connection to management principles |
| Writing Quality & Professional Communication | 10% | Clarity; executive-ready language; organization |

## Assignment Prompt (Given to Students)

> Write a formal case study analysis of a real-world business scenario. Identify the central strategic problem, apply at least two analytical frameworks, develop strategic alternatives, and make specific actionable recommendations with implementation plans and risk assessment.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Frameworks**: Minimum 2 applied (SWOT, Porter's Five Forces, PESTLE, etc.)
- **Alternatives**: At least 3 strategic options evaluated
- **Citation style**: APA or Harvard
- **Required sections**: Title Page, Executive Summary, Problem ID, Situational Analysis, Alternatives, Recommendations, Risk Assessment, Reflection, Conclusion, References

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `case_study_grading_heuristics_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT CASE STUDY SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Framework-mandatory**: At least 2 recognized business frameworks must be applied with case data
- **Action-oriented**: Recommendations must be specific with implementation steps and timelines
- **Risk-aware**: Risk assessment section is mandatory — students cannot ignore implementation challenges
- **Executive summary**: Students must condense their analysis into a 100–200 word executive summary
- **Data-driven**: Financial metrics and case evidence must support all analytical claims
