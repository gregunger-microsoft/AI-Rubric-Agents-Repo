# MathProfessor-CalculusProofs — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic mathematics professor** responsible for grading formal **calculus proof assignments**. It evaluates student submissions against a rigorous rubric that assesses logical validity, correct application of theorems and definitions, proof structure, mathematical notation precision, and completeness across a set of required proof problems.

## Problem It Solves

Grading mathematical proofs is one of the most time-intensive tasks in STEM education. Each proof requires the grader to verify **logical validity step-by-step**, check **correct application of theorems**, and assess **notation and structure**. This agent automates that rigorous evaluation process, ensuring **consistent standards** across all submissions and freeing instructors to focus on teaching rather than line-by-line proof verification.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Logical Validity of Proofs | 35% | Every step follows logically; no gaps or circular reasoning |
| Correct Application of Theorems & Definitions | 20% | Theorems applied correctly; conditions verified before use |
| Proof Structure & Organization | 15% | Clear Statement → Proof → Conclusion for each problem |
| Mathematical Notation & Precision | 15% | Consistent, correct use of quantifiers, variables, and symbols |
| Problem Completeness | 15% | All 4 required proofs attempted with substantive effort |

## Required Proof Problems

| # | Problem |
|---|---------|
| P1 | Prove that the sequence a_n = 1/n converges to 0 using the epsilon-N definition |
| P2 | Prove the power rule (derivative of x^n) from the limit definition |
| P3 | Prove the Fundamental Theorem of Calculus, Part 1 |
| P4 | Prove that a continuous function on [a,b] is bounded |

## Requirements

- **All 4 proofs required** — each missing proof deducts 20%
- **Notation**: LaTeX, handwritten scan, or typed — must be legible
- **Structure**: Statement → Proof → QED/conclusion for each problem
- **Hard fail**: Circular reasoning scores 0 for that problem; plagiarism = 0 overall

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `proof_grading_heuristics_calculus_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT CALCULUS PROOF SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Logic-centric**: Evaluates step-by-step logical validity rather than prose quality
- **Binary validity**: A proof is either valid or invalid — partial credit follows rubric for structure/effort
- **No word count**: Evaluated on completeness and correctness, not length
- **Notation-sensitive**: Correct use of quantifiers (∀, ∃), variables, and mathematical symbols matters
- **Circular reasoning detection**: Assuming the conclusion is a hard-fail condition per proof
