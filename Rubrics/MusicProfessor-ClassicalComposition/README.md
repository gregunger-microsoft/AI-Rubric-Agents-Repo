# MusicProfessor-ClassicalComposition — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic music professor** responsible for grading formal analytical papers on **classical music composition** from the Common Practice Period (c. 1600–1900). It evaluates student submissions that perform formal analysis (sonata form, rondo, fugue, etc.), harmonic analysis (key relationships, modulations, cadences), and contextual analysis (historical period, composer intent, performance conventions). Students must demonstrate the ability to connect musical structure with expressive and dramatic purpose.

## Problem It Solves

Music theory papers require specialized evaluation: students must correctly identify **formal structures** (e.g., sonata-allegro form with exposition, development, recapitulation), **harmonic progressions** (dominant-tonic relationships, modulations to relative keys), and **expressive techniques** (dynamics, tempo, orchestration). Errors in these areas reflect fundamental misunderstandings. This agent systematically evaluates theoretical accuracy and analytical depth, ensuring consistent grading standards that would be difficult to maintain manually across large class sections.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Introduction & Thesis Quality | 10% | Works identified; thesis about form and expression |
| Historical & Stylistic Context | 10% | Composer context, period characteristics, performance history |
| Formal/Structural Analysis | 25% | Form identification; section breakdown; thematic development |
| Harmonic Analysis Accuracy | 20% | Key centers, modulations, cadences, harmonic rhythm |
| Expressive & Dramatic Analysis | 15% | How form/harmony serve expression; dynamics, texture |
| Comparative Element | 10% | Comparison of works/composers; stylistic differences |
| Writing Quality | 10% | Clarity; music-theoretical vocabulary; organization |

## Assignment Prompt (Given to Students)

> Write a formal analytical paper examining at least two compositions from the Common Practice Period. Provide formal analysis (structure/form), harmonic analysis (key relationships, modulations, cadences), and contextual analysis. Argue a thesis about how musical form and harmonic language serve expressive or dramatic purposes.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Compositions**: Minimum 2 works analyzed
- **Sources**: Scholarly music theory texts; score references (measure numbers) encouraged
- **Citation style**: Chicago, MLA, or APA
- **Required sections**: Title Page, Introduction, Historical Context, Formal Analysis, Harmonic Analysis, Expressive Analysis, Comparative Element, Reflection, Conclusion, Works Cited

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `paper_grading_heuristics_classical_composition_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT MUSIC ANALYSIS PAPER SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Music-theoretical verification**: Validates formal and harmonic analysis claims (not just writing quality)
- **Score-referenced**: Measure numbers and specific passages should be cited
- **Multi-layered analysis**: Formal + harmonic + expressive analysis required
- **Period-specific**: Evaluates understanding of Baroque/Classical/Romantic conventions
- **Composition identification**: Each work must have title, composer, catalog number, date, and key
