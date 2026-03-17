# Document Hydration Solution

**Enterprise Service Request Intake Form**

> Automated extraction of structured data from unstructured sources, mapped to a professionally designed Word template with full schema validation and quality grading.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Primary Use Case](#primary-use-case)
- [Additional Use Cases](#additional-use-cases)
- [Solution Architecture](#solution-architecture)
- [File Inventory](#file-inventory)
- [How the Pieces Work Together](#how-the-pieces-work-together)
- [How to Extend the System](#how-to-extend-the-system)
- [Quality Checklist](#quality-checklist)

---

## Problem Statement

Organizations routinely receive unstructured data — emails, meeting notes, scanned forms, chat transcripts, free-text documents — that must be captured in structured, standardized document templates. Manual data entry is slow, error-prone, and expensive. Existing automation tools often require rigid input formats that rarely match real-world data.

This solution addresses the gap by providing a **document hydration system** that:

1. Accepts **unstructured source data** of any format.
2. Infers and extracts field values using **semantic mapping heuristics**.
3. Validates extracted values against a **strict JSON schema**.
4. Hydrates a **professionally designed Word template** by replacing placeholder tokens with mapped values.
5. Produces a **quality report with confidence scores and a letter grade**.
6. Flags ambiguous or missing fields for **human review**.

The result is a system that achieves **maximum automation** while preserving **human oversight** where it matters.

---

## Primary Use Case

**Automated or semi-automated form completion.**

A user (or an upstream system) provides unstructured text — an email requesting a new service, a meeting transcript capturing project requirements, a scanned intake form — and the system produces a completed, validated Word document ready for review and approval.

---

## Additional Use Cases

This document hydration approach is domain-agnostic. The same architecture (template + schema + mapping specification) can be adapted to:

| Use Case | Example |
|---|---|
| **Intake forms** | Patient intake, student enrollment, vendor onboarding |
| **Insurance applications** | Auto, home, or health insurance application pre-fill |
| **Incident reports** | Workplace safety, IT security, law enforcement |
| **HR onboarding** | New hire paperwork, benefits enrollment, I-9 pre-population |
| **RFP responses** | Extracting requirements from RFP documents and mapping to response templates |
| **Compliance documentation** | Regulatory filing forms, audit questionnaires, certification applications |
| **Legal intake** | Client matter intake, case assessment forms, conflict check questionnaires |
| **Medical intake** | Patient history, referral forms, prior authorization requests |
| **Procurement** | Purchase orders, vendor evaluation forms, contract request forms |
| **Project initiation** | Project charter forms, resource allocation requests, budget approval forms |

To adapt the system to a new domain, create a new `Template.docx`, `schema.json`, and update the keyword banks in the mapping specification.

---

## Solution Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    UNSTRUCTURED SOURCE DATA                  │
│         (emails, notes, documents, transcripts, OCR)        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                     MAPPING ENGINE                           │
│                                                              │
│  1. Preprocess & normalize source text                       │
│  2. Detect labels, keywords, and structural patterns         │
│  3. Match candidates to schema fields                        │
│  4. Score confidence per field (0.0 – 1.0)                   │
│  5. Normalize values (dates, names, phones, enums, etc.)     │
│  6. Validate against schema constraints                      │
│  7. Resolve conflicts (highest confidence wins)              │
│                                                              │
│  References:  schema.json · DataMappingSpecification.md      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   MAPPED JSON OUTPUT                          │
│           { "FIELD_KEY": "extracted value", ... }            │
└──────────┬──────────────────────────────────┬───────────────┘
           │                                  │
           ▼                                  ▼
┌─────────────────────────┐   ┌───────────────────────────────┐
│    TEMPLATE HYDRATION    │   │       MAPPING REPORT          │
│                          │   │                               │
│  Replace <<FIELD_KEY>>   │   │  Per-field confidence scores  │
│  tokens in Template.docx │   │  Issues for human review      │
│  with mapped values      │   │  Missing required fields      │
│                          │   │  Overall score & letter grade │
└─────────────┬────────────┘   └───────────────┬───────────────┘
              │                                │
              ▼                                ▼
┌─────────────────────────┐   ┌───────────────────────────────┐
│   COMPLETED DOCUMENT     │   │     HUMAN REVIEW QUEUE        │
│   (ready for approval)   │   │  (flagged fields for review)  │
└──────────────────────────┘   └───────────────────────────────┘
```

---

## File Inventory

| File | Purpose | Format |
|---|---|---|
| `Template.docx` | Visually polished enterprise intake form with 42 placeholder tokens (`<<FIELD_KEY>>`) across 6 sections. Ready for hydration. | Microsoft Word (.docx) |
| `schema.json` | Authoritative field definition with types, constraints, validation rules, and examples for all 42 fields. Single source of truth. | JSON |
| `DataMappingSpecification.md` | Complete mapping strategy: heuristics, confidence scoring, normalization rules, failure handling, grading model, and a worked example. | Markdown |
| `README.md` | This file. Solution overview, architecture, usage, and extension guide. | Markdown |

---

## How the Pieces Work Together

### 1. Word Template (`Template.docx`)

The template is the **output artifact** — the professionally formatted document that end users and approvers see. It contains:

- **6 clearly separated sections** with colored headers and structured tables.
- **42 placeholder tokens** in the format `<<FIELD_KEY>>` that are replaced with actual values during hydration.
- Helper text and required/optional indicators for each field.
- A header banner, consistent typography, and a footer with version and generation date.

The template is the **visual contract**: it defines what the final document looks like.

### 2. JSON Schema (`schema.json`)

The schema is the **data contract**: it defines what values are acceptable. For each of the 42 fields, it specifies:

- Data type (string, integer, boolean, date, enum)
- Required vs. optional
- Min/max length
- Allowed pattern (regex)
- Enum values (for constrained fields)
- Example value

**Schema parity is mandatory** — every field in the template exists in the schema, and vice versa. The schema is the authoritative reference for validation.

### 3. Mapping Specification (`DataMappingSpecification.md`)

The mapping specification is the **logic contract**: it defines how raw, unstructured data becomes structured field values. It covers:

- **How to interpret** source data (preprocessing, normalization).
- **How to match** source fragments to schema fields (keywords, context, patterns).
- **How to score** confidence (0.0 – 1.0 per field).
- **How to handle failures** (unmapped fields, constraint violations, ambiguity).
- **How to grade** the overall mapping quality (100-point model, A–F grades).
- **When to involve humans** (low confidence, ambiguity, missing required fields).

### 4. Human Review Loop

The system is designed to be **human-in-the-loop aware**:

- Fields mapped with high confidence (≥ 0.90) are auto-accepted.
- Fields with moderate confidence (0.70 – 0.89) are auto-accepted but flagged for optional review.
- Fields with low confidence (< 0.70) require human review.
- Ambiguous or conflicting mappings always require human resolution.
- Missing required fields block document finalization until resolved.

The mapping report provides reviewers with all the context they need: source signals, confidence scores, and candidate values.

---

## How to Extend the System

### Adding New Fields

1. **Add the field to `schema.json`** — Define the key, section, label, type, constraints, and example.
2. **Add the placeholder to `Template.docx`** — Insert a new row in the appropriate section table with the `<<NEW_FIELD_KEY>>` token, label, helper text, and required/optional indicator.
3. **Update the keyword bank** — Add primary and secondary keywords for the new field to the mapping specification's heuristic tables.
4. **Update the scoring model** — Recalculate the per-field point allocation to maintain a 100-point total.
5. **Verify parity** — Confirm the field count in the schema, template, and specification all match.

### Modifying Schema Safely

- **Renaming a field key** — Update the key in `schema.json`, the `<<FIELD_KEY>>` token in `Template.docx`, and all references in `DataMappingSpecification.md` simultaneously.
- **Changing type or constraints** — Update `schema.json` first, then verify existing mapped data still validates. Update normalization rules in the specification if needed.
- **Removing a field** — Remove from all three artifacts. Recalculate scoring model.

### Maintaining Schema ↔ Template Parity

Parity is the most critical invariant. To verify:

1. Extract all `<<...>>` tokens from `Template.docx`.
2. Extract all `key` values from `schema.json`.
3. Confirm the two sets are identical (no extras, no missing).
4. Confirm the field count metadata in `schema.json` matches the actual count.

This check should be performed after every modification.

---

## Quality Checklist

Use this checklist before deploying any changes to the system:

| # | Check | Status |
|---|---|---|
| 1 | `Template.docx` contains ≥ 6 clearly separated sections | ☐ |
| 2 | `Template.docx` contains ≥ 40 placeholder tokens (`<<FIELD_KEY>>`) | ☐ |
| 3 | `schema.json` defines the same number of fields as placeholders in the template | ☐ |
| 4 | Every `<<FIELD_KEY>>` in the template has a matching entry in `schema.json` | ☐ |
| 5 | Every field in `schema.json` has a matching `<<FIELD_KEY>>` in the template | ☐ |
| 6 | All required fields are marked `required: true` in the schema | ☐ |
| 7 | All enum fields have non-empty `enumValues` arrays | ☐ |
| 8 | All date fields specify ISO 8601 format in `allowedPattern` | ☐ |
| 9 | The scoring model in the mapping specification totals exactly 100 points | ☐ |
| 10 | Grade bands (A–F) are defined with non-overlapping score ranges | ☐ |
| 11 | Failure handling covers all four scenarios (unmapped, constraint violation, ambiguity, missing required) | ☐ |
| 12 | The worked example in the mapping specification produces a valid mapped JSON that passes schema validation | ☐ |
| 13 | The mapping report structure includes per-field detail and a summary | ☐ |
| 14 | Human review triggers are clearly defined for each confidence threshold | ☐ |
| 15 | The README accurately describes all files and their relationships | ☐ |

---

## Version History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-03-17 | Initial release — 42 fields, 6 sections, full mapping specification |

---

*Generated as part of the Document Hydration Solution. All artifacts are production-quality and ready for deployment.*
