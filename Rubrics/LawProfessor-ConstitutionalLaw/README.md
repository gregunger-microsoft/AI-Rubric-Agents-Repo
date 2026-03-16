# LawProfessor-ConstitutionalLaw — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic law professor** responsible for grading formal **legal memoranda** on **constitutional law**. It evaluates student submissions that analyze constitutional issues using the IRAC method (Issue, Rule, Application, Conclusion), cite controlling case law and constitutional text, apply legal rules to fact patterns, address counterarguments, and reach reasoned conclusions. The agent is designed for pre-law undergraduate courses and introductory law school constitutional law classes.

## Problem It Solves

Legal writing evaluation requires verifying that students can perform **disciplined legal reasoning** — not just write well, but construct arguments grounded in **constitutional authority**. Common student errors include: presenting opinions without authority, misstating case holdings, failing to distinguish precedent, using the wrong standard of review (strict scrutiny vs. rational basis), and ignoring counterarguments. This agent systematically evaluates IRAC structure, case law accuracy, doctrinal framework application, and counterargument engagement — providing the kind of rigorous, consistent feedback that large law classes struggle to deliver.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Issue Identification & Framing | 10% | Precise constitutional question; sub-issues identified |
| Rule Statement & Case Law Accuracy | 25% | Constitutional text cited; controlling cases with holdings; doctrinal test articulated |
| Application & Legal Reasoning | 30% | Rule applied to facts; analogies/distinctions to precedent |
| Counterargument & Distinguishing Precedent | 15% | Opposing argument addressed; cases distinguished |
| Conclusion Quality | 5% | Reasoned conclusion; predicted outcome; uncertainty acknowledged |
| Citation Accuracy & Bluebook Compliance | 5% | Proper Bluebook format for all citations |
| Writing Quality & Legal Communication | 10% | Clarity; precision; professional legal tone |

## Assignment Prompt (Given to Students)

> Write a formal legal memorandum analyzing a constitutional law issue. Frame a specific legal question, identify applicable constitutional provisions and controlling case law, apply legal rules to a fact pattern, and reach a reasoned conclusion. Use IRAC method. Address counterarguments and distinguish competing precedents. Use Bluebook citation format.

## Requirements

- **Word count**: 2,000–2,500 words (hard limits: 1,500–3,000)
- **Cases**: Minimum 5 cases cited with proper Bluebook format
- **Constitutional provisions**: At least 1 provision cited by article/section/amendment
- **Citation style**: Bluebook
- **Required sections**: Heading, Question Presented, Brief Answer, Statement of Facts, Discussion (Issue, Rule, Application, Conclusion), Table of Authorities

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `memo_grading_heuristics_constitutional_law_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT LEGAL MEMO SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **IRAC-mandatory**: Legal analysis must follow Issue → Rule → Application → Conclusion structure
- **Case law verification**: Holdings must be accurately stated; fabricated citations are a hard fail
- **Doctrinal framework**: Students must identify the correct standard of review (strict scrutiny, intermediate, rational basis)
- **Counterargument required**: Students must address opposing arguments and distinguish unfavorable precedent
- **Bluebook citations**: Legal citation format is graded as a separate criterion
- **Highest weight on Application (30%)**: The core skill is applying rules to facts with analogical reasoning
