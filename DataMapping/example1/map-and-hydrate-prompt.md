Use this folder: C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\example1
Create a folder named 'output' inside the 'example1' folder.

Read the following three reference files before doing any work:
- C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\schema.json
- C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\DataMappingSpecification.md
- C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\Template.docx

Now read the source data file:
- C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\example1\sample-input-1.txt

---

### Role & Objective

You are an expert in data engineering and data mapping. Your task is to extract structured field values from the unstructured source data file and produce a completed Word document.

---

### Rules (Non-Negotiable)

1. You MUST adhere to the **DataMappingSpecification.md** guidelines 100%.
2. Every field in **schema.json** must be evaluated against the source data.
3. For each field, assign a **confidence score** (0.0–1.0) following the heuristics and scoring model defined in the specification.
4. Apply all **normalization rules** from the specification (dates → ISO 8601, phone → standardized format, booleans → true/false, enums → exact match from allowedValues, names → Title Case, IDs → uppercase, etc.).
5. Validate every mapped value against the **type, minLength, maxLength, allowedPattern, and enumValues** constraints in schema.json. If a value violates a constraint, attempt automatic correction per the specification. If correction fails, leave the field unmapped.
6. Fields that cannot be mapped must be left blank (empty string) — do **not** fabricate or hallucinate data.

---

### Deliverables

#### 1. Mapped JSON — `mapped-output.json`

Save to: `C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\example1\output\mapped-output.json`

Produce a JSON object with all 42 field keys from schema.json. For each field:
- If mapped: the normalized, validated value.
- If unmapped: `null`.

#### 2. Mapping Report — `mapping-report.md`

Save to: `C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\example1\output\mapping-report.md`

Following the **Sample Mapping Report Structure** in DataMappingSpecification.md, produce a full report that includes:

- **Summary**: total fields, mapped (by confidence tier), unmapped count, constraint violations, final score, and letter grade.
- **Field-by-field detail**: for every field — mapped value, confidence score, points earned, source signal used, and status (auto-accepted / flagged / unmapped).
- **Issues requiring human review**: list each issue with reason, candidates (if ambiguous), and recommended action.
- **Missing required fields**: list any required fields that could not be mapped.

Calculate the score using the exact point model from the specification:
- Required fields: 3.5 points max each (21 required × 3.5 = 73.5)
- Optional fields: 1.25 points max each (21 optional × 1.25 = 26.25)
- Rounding adjustment: +0.25
- Total: 100.0 points
- Apply the confidence-to-percentage table to each field.

#### 3. Completed Word Document — `MappedOutput.docx`

Save to: `C:\tempGregProj\ProfessorJarvisAIAgent\DataMapping\example1\output\MappedOutput.docx`

Using **Template.docx** as the visual reference, generate a new Word document that:
- Preserves the same layout, section headers, colored tables, banner, and footer from the template.
- Replaces every `<<FIELD_KEY>>` placeholder with the actual mapped value (or leaves it blank if unmapped).
- This is a **completed form**, not a template — it should read as a filled-in document ready for review and approval.

---

### Output Checklist

Before finishing, verify:
- [ ] `output` folder exists inside `example1`
- [ ] `mapped-output.json` contains all 42 keys with mapped values or null
- [ ] `mapping-report.md` follows the specification's report structure exactly
- [ ] `mapping-report.md` includes a calculated score and letter grade
- [ ] `MappedOutput.docx` is a completed (non-template) document with actual values filled in
- [ ] No data was fabricated — every mapped value traces back to the source file
- [ ] All normalization and validation rules from the specification were applied
