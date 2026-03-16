# ArtProfessor-RenaissancePeriod — AI Grading Agent

## Use Case

This AI Agent acts as a **strict academic art history professor** responsible for grading formal essays on **Italian Renaissance art (c. 1400–1600)**. It evaluates student submissions that analyze specific artworks through formal, contextual, and iconographic lenses. Students must demonstrate understanding of artistic innovations (perspective, chiaroscuro, sfumato), patronage systems (Medici, Church), the intellectual climate of humanism, and the cultural significance of Renaissance masterworks.

## Problem It Solves

Art history essays require a unique evaluation approach: students must **describe what they see** (formal analysis), **explain what it means** (iconographic analysis), and **connect it to the broader world** (contextual analysis). Many students default to surface-level description without interpretation, or make claims about artworks they haven't truly analyzed. This agent systematically evaluates whether students can perform all three levels of art historical analysis, verify that artworks are correctly identified, and assess comparative reasoning between works.

## What This Agent Grades

| Criterion | Weight | What It Evaluates |
|-----------|--------|-------------------|
| Introduction & Thesis Quality | 10% | Historical context; thesis about art and cultural values |
| Historical & Cultural Context | 15% | Humanism, patronage systems, political/economic conditions |
| Formal Analysis of Artworks | 25% | Composition, color, light, perspective, technique for 3+ works |
| Iconographic & Symbolic Analysis | 15% | Symbol identification; connection to religious/humanist themes |
| Comparative Analysis | 15% | Comparison of 2+ artworks/artists; evolving styles |
| Personal Reflection | 5% | Changed understanding; connection to modern visual culture |
| Writing Quality | 15% | Clarity; art historical vocabulary; organization |

## Assignment Prompt (Given to Students)

> Write a formal art history essay analyzing the artistic innovations of the Italian Renaissance. Select at least three artworks by at least two different artists. Provide formal, contextual, and iconographic analysis. Argue a thesis about how Renaissance art reflected or shaped the cultural, intellectual, or political values of the period.

## Requirements

- **Word count**: 1,500–2,000 words (hard limits: 1,200–2,500)
- **Artworks**: Minimum 3 artworks analyzed, by at least 2 artists
- **Sources**: Minimum 3 scholarly art history sources
- **Citation style**: Chicago or MLA
- **Required sections**: Title Page, Introduction, Historical Context, Formal Analysis, Iconographic Analysis, Comparative Analysis, Reflection, Conclusion, Works Cited

## Files in This Folder

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, execution order |
| `essay_grading_heuristics_renaissance_v1.json` | Full rubric with scoring criteria, weights, penalties |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions |
| `STUDENT ART HISTORY ESSAY SUBMISSION C.txt` | Sample student submission for testing |
| `README.md` | This file |

## Key Differentiation

- **Visual analysis focus**: Evaluates formal analysis skills (composition, color, perspective) not just writing
- **Artwork verification**: Each artwork must be identified by artist, title, date, and medium
- **Triple-layer analysis**: Formal + contextual + iconographic analysis required
- **Comparative dimension**: Students must compare artworks/artists, not just describe one at a time
- **Patronage awareness**: Understanding of who commissioned art and why is required
