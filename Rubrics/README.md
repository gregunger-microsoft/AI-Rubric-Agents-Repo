# AI Rubric Agents - Use Case Repository

A collection of AI Agents that act as **strict academic professors**, each specialized in a different discipline. Every agent evaluates student submissions against a comprehensive, weighted rubric; produces defensible, evidence-based grades; and performs a self-audit of grading accuracy and confidence.

Each agent follows the same core principles:
- **Grade only what is written** — never assume intent or effort
- **Evidence-based scoring** — every score is justified by rubric and submission text
- **Mandatory self-audit** — confidence level and human-review flags on every grade
- **No tutoring or rewriting** — the agent is an evaluator, not a collaborator

---

## Available Use Cases

| # | Agent | Discipline | Submission Type |
|---|-------|-----------|-----------------|
| 1 | [EnglishProfessor-MaryShelleys](EnglishProfessor-MaryShelleys/) | English Literature | Book report on *Frankenstein* |
| 2 | [HistoryProfessor-WorldWarII](HistoryProfessor-WorldWarII/) | History | Analytical essay on WWII causes, events & consequences |
| 3 | [ScienceProfessor-ClimateChange](ScienceProfessor-ClimateChange/) | Environmental Science | Research report with peer-reviewed data & mitigation analysis |
| 4 | [MathProfessor-CalculusProofs](MathProfessor-CalculusProofs/) | Mathematics | Formal calculus proofs (epsilon-N, power rule, FTC, boundedness) |
| 5 | [PhilosophyProfessor-Ethics](PhilosophyProfessor-Ethics/) | Philosophy | Ethics essay comparing frameworks on a moral dilemma |
| 6 | [CSProfessor-DataStructures](CSProfessor-DataStructures/) | Computer Science | Data structures analysis paper with Big-O & code examples |
| 7 | [ArtProfessor-RenaissancePeriod](ArtProfessor-RenaissancePeriod/) | Art History | Essay with formal, iconographic & contextual analysis of Renaissance art |
| 8 | [MusicProfessor-ClassicalComposition](MusicProfessor-ClassicalComposition/) | Music Theory | Analytical paper on Classical/Romantic compositions |
| 9 | [BusinessProfessor-CaseStudy](BusinessProfessor-CaseStudy/) | Business / Strategy | Case study analysis with SWOT, Porter's Five Forces & risk assessment |
| 10 | [PsychologyProfessor-ResearchMethods](PsychologyProfessor-ResearchMethods/) | Psychology | APA-format research proposal with methodology & stats plan |
| 11 | [LawProfessor-ConstitutionalLaw](LawProfessor-ConstitutionalLaw/) | Law | Legal memorandum using IRAC method with Bluebook citations |

---

## What's Inside Each Folder

Every agent folder contains **5 files** that follow a consistent structure:

| File | Purpose |
|------|---------|
| `ai_professor_grader_instruction_set_v1.json` | Agent behavioral rules, role definition, and mandatory execution order |
| `*_grading_heuristics_*_v1.json` | Full rubric with scoring criteria, weights, penalties, and accuracy self-audit |
| `ProfessorJarvis-AIAgent-Instructions.txt` | Plain-text agent instructions (quick-reference summary) |
| `README.md` | Detailed use-case description, grading criteria table, and assignment prompt |
| `STUDENT * SUBMISSION C.txt` | Sample student submission for testing and validation |

---

## How It Works

Each agent follows a **6-step mandatory grading workflow**:

1. **Parse Submission** — Extract text, detect sections, compute word counts
2. **Rule & Integrity Checks** — Verify required sections, apply penalties, flag plagiarism
3. **Criterion Scoring** — Score each criterion (0–5) independently with cited evidence
4. **Score Calculation** — Apply rubric weights, penalties, and caps to compute final grade
5. **Feedback Generation** — Produce strengths, improvements, and a revision plan
6. **Grading Accuracy Self-Audit** — Assess confidence level and flag for human review

---

## Use-Case Highlights

### English Literature — *Frankenstein*
Grades book reports on Mary Shelley's *Frankenstein* for thesis quality, textual evidence, thematic analysis, and personal reflection. Requires primary-text citations and penalizes plot summary over analysis.

### History — World War II
Evaluates WWII essays covering causes (Treaty of Versailles, appeasement), major events (Stalingrad, D-Day, Pacific Theater), and geopolitical consequences (Cold War, UN, decolonization). Requires primary and secondary sources with proper historiographic methodology.

### Science — Climate Change
Grades research reports on climate change mechanisms, data analysis from peer-reviewed sources, ecological/societal impacts, and evaluation of mitigation strategies. Requires an abstract, 5+ peer-reviewed sources, and distinguishes scientific consensus from contested findings.

### Mathematics — Calculus Proofs
Evaluates formal proofs for logical validity step-by-step. Circular reasoning scores 0 for the affected proof. Assesses correct application of theorems, proof structure, and notation precision across 4 required problems.

### Philosophy — Ethics
Grades essays applying ethical frameworks (utilitarianism, deontology, virtue ethics) to contemporary moral dilemmas. Position-neutral — evaluates argument quality, not which position is defended. Requires engagement with counterarguments using the principle of charity.

### Computer Science — Data Structures
Evaluates papers comparing 3+ data structures with Big-O complexity analysis, code/pseudocode examples, and trade-off reasoning. Validates technical accuracy of complexity claims — wrong Big-O results in penalties regardless of writing quality.

### Art History — Renaissance Period
Grades essays analyzing Renaissance artworks through formal (composition, perspective, technique), iconographic (symbols, themes), and contextual (patronage, humanism) lenses. Each artwork must be fully identified by artist, title, date, and medium.

### Music Theory — Classical Composition
Evaluates analytical papers on compositions from the Common Practice Period with formal analysis (sonata form, rondo), harmonic analysis (key relationships, modulations, cadences), and expressive interpretation. Score/measure references are expected.

### Business — Case Study Analysis
Grades strategic case analyses requiring 2+ business frameworks (SWOT, Porter's Five Forces, PESTLE), at least 3 strategic alternatives, specific actionable recommendations with implementation timelines, and mandatory risk assessment.

### Psychology — Research Methods
Evaluates APA 7th edition research proposals with literature review (8+ peer-reviewed sources), operationally defined variables, appropriate statistical analysis plans, ethical considerations (IRB, informed consent), and methodology quality.

### Law — Constitutional Law
Grades legal memoranda using IRAC structure (Issue, Rule, Application, Conclusion) with Bluebook citations, case law holdings, doctrinal frameworks (strict scrutiny, rational basis), and counterargument engagement. Application carries the highest weight at 30%.

### Seminary — Priest Communication
Evaluates homilies, sermons, and pastoral letters for scriptural exegesis, theological depth, rhetorical effectiveness, and pastoral sensitivity. Denomination-neutral — grades communication quality, not doctrinal correctness. Misquoted scripture is penalized.

### Career Services — Resume Judger
Grades resumes for role targeting, quantified accomplishments, ATS compatibility, action-verb usage, and a required tailoring reflection. Evaluates the resume as a hiring manager would — "Would this survive a 6-second resume scan?"
