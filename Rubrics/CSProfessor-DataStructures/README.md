# CSProfessor-DataStructures — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic computer science professor** responsible for grading formal analytical papers on **data structures and algorithms**. It evaluates student submissions that compare multiple data structures (arrays, linked lists, hash tables, trees, heaps, graphs), analyze their time and space complexity, provide code/pseudocode examples, and argue for the best-fit data structure for a specific application scenario.

## Problem It Solves

CS instructors grading data structures papers must verify **technical accuracy** of complexity analysis (Big-O claims), **correctness of algorithm descriptions**, and **quality of trade-off reasoning** — all while evaluating writing quality. Students frequently make errors in asymptotic analysis (e.g., claiming hash table lookup is always O(1)) or confuse time and space complexity. This agent catches those technical errors systematically and applies consistent grading standards, allowing instructors to focus on advanced curriculum development rather than repetitive paper evaluation.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Introduction & Thesis Quality | 10% | Problem context; thesis about data structure suitability |
| Data Structure Descriptions | 15% | At least 3 structures defined with key operations and properties |
| Complexity Analysis Accuracy | 25% | Big-O for insert/search/delete; space complexity; best/avg/worst case |
| Code / Pseudocode Quality | 15% | At least 2 examples; logical correctness; explanations |
| Trade-off Analysis & Application | 20% | Comparison of trade-offs; specific scenario; justified recommendation |
| Personal Reflection | 5% | Lessons learned; connection to software engineering practice |
| Writing Quality & Technical Communication | 10% | Clarity, organization, proper use of CS terminology |

## Assignment Prompt (Given to Students)

> Write a formal analytical paper comparing at least three data structures. For each, analyze time and space complexity for key operations, discuss real-world use cases, and argue which data structure is best suited for a specific application scenario you define. Include pseudocode or code examples.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Data structures**: Minimum 3 compared
- **Code**: At least 2 code/pseudocode examples
- **Citation style**: ACM, IEEE, or APA
- **Required sections**: Title Page, Introduction, Data Structure Descriptions, Complexity Analysis, Code Examples, Trade-off Analysis, Reflection, Conclusion, References

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `paper_grading_heuristics_data_structures_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT CS PAPER SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Technical verification**: Validates correctness of Big-O claims, not just prose quality
- **Code evaluation**: Assesses pseudocode/code for logical correctness and relevance
- **Complexity-focused**: Highest weight criterion (25%) is complexity analysis accuracy
- **Application-driven**: Students must define and defend a real-world scenario
- **No tolerance for incorrect complexity claims**: Wrong Big-O = penalty regardless of writing
