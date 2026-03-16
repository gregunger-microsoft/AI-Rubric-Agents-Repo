# PhilosophyProfessor-Ethics — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic philosophy professor** responsible for grading formal essays on **ethical frameworks and applied ethics**. It evaluates student submissions that compare multiple ethical theories (utilitarianism, deontology, virtue ethics, care ethics, etc.) and apply them to a contemporary moral dilemma. The agent assesses the quality of philosophical argumentation, engagement with primary texts, logical structure, and the student's ability to consider and respond to objections.

## Problem It Solves

Philosophy instructors must evaluate essays not for factual correctness but for **quality of reasoning**. A student can defend any ethical position—what matters is whether the argument is logically valid, well-structured, grounded in philosophical texts, and honestly engages with counterarguments. This agent applies consistent evaluation of **argumentative rigor** across all submissions, catching logical fallacies, strawman arguments, and unsupported assertions that might be missed or evaluated inconsistently by human graders under time pressure.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Introduction & Thesis Quality | 10% | Clear moral dilemma identified; arguable thesis defending one framework |
| Ethical Framework Exposition | 20% | At least 2 frameworks defined with principles and philosopher references |
| Applied Ethical Analysis | 25% | Each framework applied to the dilemma; comparison of outcomes/judgments |
| Thesis Defense & Argumentation | 20% | Logical argument with clear premises and conclusion |
| Objection & Response | 10% | Charitable reconstruction of objection; reasoned response |
| Personal Reflection | 5% | Changed moral reasoning; connection to real-world challenges |
| Writing Quality & Philosophical Clarity | 10% | Precision of language, organization, use of philosophical terminology |

## Assignment Prompt (Given to Students)

> Write a formal philosophy essay that applies at least two ethical frameworks (e.g., utilitarianism, deontology, virtue ethics, care ethics) to a specific contemporary moral dilemma. Argue for which framework provides the most defensible response. Support your argument with references to primary philosophical texts and engage with at least one substantive objection.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Sources**: Minimum 2 primary philosophical texts (e.g., Mill, Kant, Aristotle)
- **Citation style**: MLA, APA, or Chicago
- **Required sections**: Title Page, Introduction + Thesis, Framework Exposition, Applied Analysis, Thesis Defense, Objection & Response, Personal Reflection, Conclusion, Works Cited

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `essay_grading_heuristics_ethics_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT PHILOSOPHY ESSAY SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Argument-centric**: Evaluates logical structure of arguments, not factual accuracy
- **Position-neutral**: Grades the quality of reasoning regardless of which ethical position is defended
- **Fallacy detection**: Identifies and penalizes logical fallacies (ad hominem, straw man, false dilemma)
- **Principle of charity**: Interprets arguments in their strongest reasonable form before evaluating
- **Objection engagement**: Requires genuine engagement with counterarguments, not dismissal
