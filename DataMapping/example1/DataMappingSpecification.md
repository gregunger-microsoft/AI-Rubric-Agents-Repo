# Data Mapping Specification

**Version:** 1.0.0  
**Date:** 2026-03-17  
**Schema Reference:** `schema.json` v1.0.0  
**Template Reference:** `Template.docx` v1.0.0  

---

## Table of Contents

1. [Overview](#1-overview)
2. [Mapping Strategy](#2-mapping-strategy)
3. [Mapping Heuristics](#3-mapping-heuristics)
4. [Failure Handling](#4-failure-handling)
5. [Mapping Report & Grading](#5-mapping-report--grading)
6. [Worked Example](#6-worked-example)

---

## 1. Overview

This specification defines how **unstructured source data** — such as emails, meeting notes, free-text documents, or scanned forms — is interpreted, normalized, and mapped into the **42 structured fields** defined in `schema.json`. The resulting mapped values are then hydrated into `Template.docx` by replacing `<<FIELD_KEY>>` placeholder tokens with their corresponding values.

The goal is **maximum automation with optional human review**. Every mapping decision produces a confidence score, and the overall quality of a mapping pass is expressed as a letter grade derived from a 100-point scoring model.

---

## 2. Mapping Strategy

### 2.1 Source Data Interpretation

Source data may arrive in any of the following formats:

| Source Type | Examples |
|---|---|
| Email body | Outlook message, forwarded thread |
| Free-text document | Word doc, PDF, plain text file |
| Meeting notes | OneNote export, Teams transcript |
| Form submission | Web form JSON, CSV row |
| Scanned / OCR output | Image-to-text extraction |

The mapping engine treats all source data as a **single normalized text corpus** after the following preprocessing steps:

1. **Encoding normalization** — Convert to UTF-8.
2. **Whitespace normalization** — Collapse multiple spaces, tabs, and line breaks into single spaces; preserve paragraph boundaries.
3. **Character cleanup** — Replace smart quotes with straight quotes, normalize dashes (em-dash → hyphen), and strip invisible Unicode characters.
4. **Section detection** — Identify document structure (headings, bullet lists, labeled fields) to infer context boundaries.

### 2.2 Field Inference Strategy

Each of the 42 schema fields is matched against the source corpus using a **multi-signal approach**:

| Signal | Weight | Description |
|---|---|---|
| Exact label match | 0.40 | Source contains the field's label verbatim (e.g., "Full Name:") |
| Synonym / alias match | 0.25 | Source contains a known synonym (e.g., "Submitter" → REQUESTOR_FULL_NAME) |
| Contextual proximity | 0.20 | A candidate value appears near a recognized label or in the expected section |
| Pattern match | 0.15 | Value matches the field's `allowedPattern` or structural type (e.g., email format) |

The weighted sum of active signals produces the **raw confidence score** for each candidate mapping.

### 2.3 Normalization Rules

All extracted values are normalized before insertion:

| Data Type | Normalization Rule |
|---|---|
| **Names** | Title Case. Remove extraneous whitespace. Preserve hyphens and apostrophes. |
| **Email addresses** | Lowercase. Trim whitespace. Validate format against regex. |
| **Phone numbers** | Strip letters and extraneous symbols. Normalize to `+X (XXX) XXX-XXXX` format where possible. Preserve original if international format is ambiguous. |
| **Dates** | Convert to ISO 8601 (`YYYY-MM-DD`). Supported input formats: `MM/DD/YYYY`, `DD-Mon-YYYY`, `Month DD, YYYY`, natural language ("next Friday" → resolved to absolute date based on submission context). |
| **IDs / Account Numbers** | Uppercase. Strip leading/trailing whitespace. Preserve hyphens. |
| **Boolean fields** | Map `yes/no`, `true/false`, `y/n`, `1/0`, `checked/unchecked` → `true` or `false`. |
| **Enum fields** | Fuzzy-match against `enumValues` list. Accept if Levenshtein distance ≤ 2 or cosine similarity ≥ 0.85. Otherwise flag for review. |
| **Free-text (long)** | Preserve original formatting. Trim leading/trailing whitespace. Truncate to `maxLength` with `[TRUNCATED]` marker if exceeded. |
| **Integers** | Strip commas and currency symbols. Parse to integer. Reject non-numeric. |
| **Casing** | Apply per-type rules above. Do not globally force casing on free-text fields. |

---

## 3. Mapping Heuristics

### 3.1 Keyword and Phrase Detection

For each schema field, a **keyword bank** is maintained. Examples:

| Schema Field | Primary Keywords | Secondary Keywords / Phrases |
|---|---|---|
| `REQUESTOR_FULL_NAME` | "name", "full name", "requestor" | "submitted by", "from", "contact person", "applicant" |
| `REQUESTOR_EMAIL` | "email", "e-mail" | "contact email", "send to", "reply to" |
| `REQUESTOR_PHONE` | "phone", "telephone", "mobile" | "call", "cell", "contact number", "direct line" |
| `REQUESTOR_DEPARTMENT` | "department", "dept" | "team", "group", "unit", "division" |
| `REQUESTOR_EMPLOYEE_ID` | "employee id", "emp id", "badge" | "staff number", "personnel id", "worker id" |
| `ORG_NAME` | "organization", "company" | "firm", "entity", "business name", "org" |
| `ORG_ACCOUNT_NUMBER` | "account number", "account #", "acct" | "customer id", "client number" |
| `ORG_COST_CENTER` | "cost center", "cost centre" | "budget code", "charge code", "finance code" |
| `REQUEST_TITLE` | "title", "subject", "request name" | "re:", "regarding", "summary" |
| `REQUEST_TYPE` | "type", "category", "request type" | "classification", "nature of request" |
| `REQUEST_PRIORITY` | "priority", "urgency" | "severity", "importance", "critical level" |
| `REQUEST_DATE_SUBMITTED` | "date submitted", "submission date" | "date", "submitted on", "filed on" |
| `REQUEST_DESCRIPTION` | "description", "details" | "overview", "summary", "narrative", "scope" |
| `TECH_ENVIRONMENT` | "environment", "env" | "target env", "deploy to", "production", "staging" |
| `TECH_DATA_CLASSIFICATION` | "data classification", "sensitivity" | "confidential", "public", "restricted", "data level" |
| `COMPLIANCE_PII_INVOLVED` | "pii", "personal data" | "personally identifiable", "contains pii", "sensitive data" |
| `COMPLIANCE_RISK_LEVEL` | "risk level", "risk" | "risk rating", "threat level", "risk assessment" |
| `APPROVAL_STATUS` | "approval status", "status" | "approved", "pending", "rejected", "decision" |

*(Additional keyword banks exist for all 42 fields; the above is a representative sample.)*

### 3.2 Contextual Inference

When keyword detection is insufficient, the engine applies contextual reasoning:

1. **Section-aware inference** — If source data has discernible sections (e.g., "Requestor Info" heading), values found within that section are preferentially mapped to fields in the corresponding schema section.

2. **Positional inference** — In labeled source data (e.g., "Name: John Smith"), the value immediately following a recognized label is the primary candidate.

3. **Co-occurrence inference** — If an email address and a phone number appear on adjacent lines, and a name appears above them, all three are grouped as a single entity (likely the requestor).

4. **Type-based inference** — Values matching specific structural patterns (email regex, phone format, date pattern, numeric ID format) are type-matched to compatible schema fields even without explicit labels.

### 3.3 Confidence Scoring

Each field mapping receives a confidence score from **0.0 to 1.0**:

| Score Range | Interpretation | Action |
|---|---|---|
| **0.90 – 1.00** | High confidence — exact or near-exact match | Auto-accept |
| **0.70 – 0.89** | Moderate confidence — strong inference but not exact | Auto-accept; flag for optional review |
| **0.50 – 0.69** | Low confidence — plausible but uncertain | Map tentatively; **require human review** |
| **0.25 – 0.49** | Very low confidence — weak signal | Do not map; present as candidate for human selection |
| **0.00 – 0.24** | No viable candidate found | Leave field unmapped; escalate as missing |

### 3.4 Conflict Resolution

When multiple candidate values compete for the same field:

1. **Highest confidence wins** — Select the candidate with the highest composite confidence score.
2. **Source priority** — If scores are tied (within ±0.05), prefer the value from the most authoritative source (e.g., a formal submission over a forwarded email thread).
3. **Recency** — If still tied, prefer the most recently written or most recently dated value.
4. **Human tiebreaker** — If all automated tiebreakers fail, flag the field for human review with all candidates presented.

---

## 4. Failure Handling

### 4.1 Field Cannot Be Mapped

| Attribute | Value |
|---|---|
| **Reason** | No candidate value found in the source data for this field. The keyword bank and contextual inference returned no matches above the 0.25 threshold. |
| **Impact** | Field will remain as `<<FIELD_KEY>>` placeholder in the hydrated document. If the field is marked `required: true`, the mapping is considered incomplete. |
| **Resolution** | Present the unmapped field to the human reviewer with the field's label, description, and helper text. Reviewer may manually enter the value or confirm it is unavailable. |
| **Human Review** | **Required** for required fields. **Recommended** for optional fields during initial deployment; may be relaxed once mapping quality is validated. |

### 4.2 Value Violates Schema Constraints

| Attribute | Value |
|---|---|
| **Reason** | A candidate value was found but fails validation: exceeds `maxLength`, does not match `allowedPattern`, is not in `enumValues`, or has an incorrect type. |
| **Impact** | The value cannot be inserted as-is. If inserted without correction, downstream systems or compliance checks may reject the document. |
| **Resolution** | Attempt automatic normalization (e.g., truncate to `maxLength`, fuzzy-match to `enumValues`). If normalization succeeds, insert the corrected value and annotate the mapping report. If normalization fails, flag for human correction. |
| **Human Review** | **Required** if automatic normalization fails. **Recommended** if normalization succeeded but confidence dropped below 0.70 as a result. |

### 4.3 Source Data Is Ambiguous

| Attribute | Value |
|---|---|
| **Reason** | The source data contains conflicting, contradictory, or unclear information for a field. For example, two different phone numbers appear near a "Phone" label, or a priority is described as both "urgent" and "low priority" in different paragraphs. |
| **Impact** | Mapping confidence is split across multiple candidates; no single candidate exceeds the auto-accept threshold. |
| **Resolution** | Present all candidates to the human reviewer with individual confidence scores and source context (surrounding text). Reviewer selects the correct value. |
| **Human Review** | **Required.** Ambiguous data must never be resolved by automated selection alone. |

### 4.4 Required Fields Are Missing

| Attribute | Value |
|---|---|
| **Reason** | One or more fields marked `required: true` in the schema have no mapped value after the full mapping pass. |
| **Impact** | The document is **not considered complete**. The mapping grade is penalized (see Section 5). The document should not be finalized until all required fields are populated. |
| **Resolution** | Generate a **Missing Required Fields** report listing each missing field with its label, section, and description. Route to the human reviewer or back to the original requestor for supplemental information. |
| **Human Review** | **Mandatory.** The document cannot be approved with missing required fields unless an explicit waiver is granted by an authorized approver. |

---

## 5. Mapping Report & Grading

### 5.1 Scoring Model

The mapping quality is scored on a **100-point scale**.

#### Point Allocation

| Category | Fields | Points per Field | Max Points |
|---|---|---|---|
| Required fields | 21 | 3.5 | 73.5 |
| Optional fields | 21 | 1.25 | 26.25 |
| **Rounding adjustment** | — | — | **+0.25** |
| **Total** | **42** | — | **100.0** |

#### Per‑Field Scoring

Each field earns points based on its mapping confidence:

| Confidence Range | Points Earned (% of field max) | Description |
|---|---|---|
| 0.90 – 1.00 | 100% | Full credit |
| 0.70 – 0.89 | 80% | Strong mapping, minor deduction |
| 0.50 – 0.69 | 50% | Partial credit; human review recommended |
| 0.25 – 0.49 | 20% | Minimal credit; value likely needs correction |
| 0.00 – 0.24 | 0% | No credit; field unmapped |

#### Example Calculation

A required field (`REQUESTOR_FULL_NAME`, 3.5 max points) mapped with confidence 0.82:

> Points earned = 3.5 × 80% = **2.80 points**

An optional field (`REQUESTOR_LOCATION`, 1.25 max points) mapped with confidence 0.55:

> Points earned = 1.25 × 50% = **0.625 points**

### 5.2 Grade Bands

| Grade | Score Range | Interpretation |
|---|---|---|
| **A** | 90.0 – 100.0 | Excellent — document is ready for final review with minimal corrections expected. |
| **B** | 80.0 – 89.9 | Good — most fields mapped accurately; a few may need review. |
| **C** | 70.0 – 79.9 | Acceptable — document is usable but several fields need attention. |
| **D** | 60.0 – 69.9 | Below average — significant gaps or low-confidence mappings; human review is mandatory. |
| **F** | 0.0 – 59.9 | Failing — document is incomplete; source data may be insufficient or misaligned with the template. |

### 5.3 Sample Mapping Report Structure

```
═══════════════════════════════════════════════════════════════
           DOCUMENT HYDRATION — MAPPING REPORT
═══════════════════════════════════════════════════════════════

Report ID:          RPT-2026-03-17-00142
Generated:          2026-03-17T14:32:00Z
Schema Version:     1.0.0
Template Version:   1.0.0
Source Document:    intake_email_march17.txt

───────────────────────────────────────────────────────────────
  SUMMARY
───────────────────────────────────────────────────────────────

Total Fields:               42
Mapped (High Confidence):   28
Mapped (Moderate):           7
Mapped (Low):                3
Unmapped:                    4
Constraint Violations:       1 (auto-corrected)

Score:                      82.6 / 100.0
Grade:                      B

───────────────────────────────────────────────────────────────
  FIELD-BY-FIELD DETAIL
───────────────────────────────────────────────────────────────

  Section: Requestor / Applicant Information
  ─────────────────────────────────────────

  REQUESTOR_FULL_NAME
    Mapped Value:    Maria Elena Gutierrez
    Confidence:      0.95
    Points:          3.50 / 3.50
    Source Signal:   Exact label match ("From: Maria Elena Gutierrez")
    Status:          ✅ AUTO-ACCEPTED

  REQUESTOR_EMAIL
    Mapped Value:    m.gutierrez@contoso.com
    Confidence:      0.97
    Points:          3.50 / 3.50
    Source Signal:   Pattern match (email regex) + proximity to name
    Status:          ✅ AUTO-ACCEPTED

  REQUESTOR_PHONE
    Mapped Value:    +1 (425) 555-0198
    Confidence:      0.88
    Points:          2.80 / 3.50
    Source Signal:   Pattern match (phone regex) + synonym ("cell")
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review)

  REQUESTOR_JOB_TITLE
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found
    Status:          ⬜ UNMAPPED (optional — no penalty for grade)

  ... (remaining fields follow same format) ...

───────────────────────────────────────────────────────────────
  ISSUES REQUIRING HUMAN REVIEW
───────────────────────────────────────────────────────────────

  1. COMPLIANCE_RISK_LEVEL
     Reason:          Ambiguous — source mentions "moderate risk" and
                      "potentially high" in different paragraphs.
     Candidates:      "Medium" (0.62), "High" (0.58)
     Action Required: Reviewer must select correct value.

  2. TECH_ESTIMATED_USERS
     Reason:          Constraint violation — source says "about 250-300".
                      Integer field cannot accept a range.
     Auto-corrected:  250 (lower bound selected)
     Action Required: Reviewer should confirm or adjust.

  3. REQUEST_TARGET_COMPLETION_DATE
     Reason:          Low confidence — source says "end of Q2".
                      Resolved to 2026-06-30 (last day of Q2).
     Confidence:      0.55
     Action Required: Reviewer should confirm date.

  4. ORG_CONTRACT_ID
     Reason:          Unmapped (required: false). No contract reference
                      found in source.
     Action Required: None (optional field).

───────────────────────────────────────────────────────────────
  MISSING REQUIRED FIELDS
───────────────────────────────────────────────────────────────

  None — all 21 required fields have mapped values.

═══════════════════════════════════════════════════════════════
                        END OF REPORT
═══════════════════════════════════════════════════════════════
```

### 5.4 Score Calculation Walkthrough

The final score is the **sum of all per-field points**:

1. For each field, look up its **maximum points** (3.5 for required, 1.25 for optional).
2. Determine the **confidence range** of the mapping.
3. Multiply maximum points by the **percentage** for that confidence range.
4. Sum all 42 field scores.
5. Add the 0.25 rounding adjustment.
6. Look up the **grade band** for the total.

---

## 6. Worked Example

### 6.1 Sample Unstructured Input

```
From: Maria Elena Gutierrez <m.gutierrez@contoso.com>
Date: March 17, 2026
Subject: New Azure Environment Request — Project Atlas

Hi Team,

I'm submitting a request to provision a new Azure landing zone for our
Project Atlas migration. My details:

  Name: Maria Elena Gutierrez
  Cell: +1 (425) 555-0198
  Department: Cloud Infrastructure
  Employee ID: EMP-20948
  Manager: James T. Kirk

Our organization is Contoso Ltd., account ACCT-83920-NA, cost center
CC-4490. We're in the Technology sector.

Request Details:
  Title: Provision New Azure Landing Zone for Project Atlas
  Type: New Service
  Priority: High
  Target completion: end of Q2 2026

We need a production environment on Azure (App Service, SQL Database,
Key Vault) with hub-spoke networking. The service will integrate with
Active Directory, SAP ERP, and our internal REST API gateway. Expected
users: about 250-300. We need 99.9% SLA.

Data classification is Confidential and yes, PII is involved. We comply
with SOC 2 Type II and GDPR. Data must stay in the United States. Risk
is moderate, though some areas might be considered potentially high.
Security review has not been completed yet. Data must be encrypted at
rest and in transit, and annual pen testing is required per our MSA.

This request supports a board-level initiative with a hard Q3 deadline.
Please expedite.

Approval should go to Sarah J. Connor (s.connor@contoso.com). Backup
approver can be Robert A. Martinez.

Thanks,
Maria
```

### 6.2 Resulting Mapped JSON

```json
{
  "REQUESTOR_FULL_NAME": "Maria Elena Gutierrez",
  "REQUESTOR_EMAIL": "m.gutierrez@contoso.com",
  "REQUESTOR_PHONE": "+1 (425) 555-0198",
  "REQUESTOR_JOB_TITLE": null,
  "REQUESTOR_DEPARTMENT": "Cloud Infrastructure",
  "REQUESTOR_EMPLOYEE_ID": "EMP-20948",
  "REQUESTOR_LOCATION": null,
  "REQUESTOR_MANAGER_NAME": "James T. Kirk",
  "ORG_NAME": "Contoso Ltd.",
  "ORG_DIVISION": null,
  "ORG_ACCOUNT_NUMBER": "ACCT-83920-NA",
  "ORG_COST_CENTER": "CC-4490",
  "ORG_ADDRESS": null,
  "ORG_INDUSTRY_SECTOR": "Technology",
  "ORG_CONTRACT_ID": null,
  "REQUEST_TITLE": "Provision New Azure Landing Zone for Project Atlas",
  "REQUEST_TYPE": "New Service",
  "REQUEST_PRIORITY": "High",
  "REQUEST_DATE_SUBMITTED": "2026-03-17",
  "REQUEST_TARGET_COMPLETION_DATE": "2026-06-30",
  "REQUEST_DESCRIPTION": "We need a production environment on Azure (App Service, SQL Database, Key Vault) with hub-spoke networking. The service will integrate with Active Directory, SAP ERP, and our internal REST API gateway. Expected users: about 250-300. We need 99.9% SLA.",
  "REQUEST_BUSINESS_JUSTIFICATION": "This request supports a board-level initiative with a hard Q3 deadline. Project Atlas is a strategic initiative to modernize our legacy ERP system.",
  "TECH_ENVIRONMENT": "Production",
  "TECH_PLATFORM": "Azure (App Service, SQL Database, Key Vault)",
  "TECH_SYSTEM_DEPENDENCIES": "Active Directory, SAP ERP, internal REST API gateway",
  "TECH_DATA_CLASSIFICATION": "Confidential",
  "TECH_ESTIMATED_USERS": 250,
  "TECH_AVAILABILITY_REQUIREMENT": "99.9% (Standard)",
  "TECH_INTEGRATION_ENDPOINTS": "Active Directory, SAP ERP, internal REST API gateway",
  "COMPLIANCE_REGULATORY_FRAMEWORKS": "SOC 2 Type II, GDPR",
  "COMPLIANCE_DATA_RESIDENCY": "United States",
  "COMPLIANCE_PII_INVOLVED": true,
  "COMPLIANCE_RISK_LEVEL": "Medium",
  "COMPLIANCE_SECURITY_REVIEW_COMPLETED": false,
  "COMPLIANCE_CONSTRAINTS_NOTES": "Data must be encrypted at rest and in transit. Annual penetration testing is required per our MSA.",
  "APPROVAL_PRIMARY_APPROVER_NAME": "Sarah J. Connor",
  "APPROVAL_PRIMARY_APPROVER_EMAIL": "s.connor@contoso.com",
  "APPROVAL_SECONDARY_APPROVER_NAME": "Robert A. Martinez",
  "APPROVAL_DATE": null,
  "APPROVAL_STATUS": "Pending",
  "META_DOCUMENT_VERSION": "1.0.0",
  "META_COMMENTS": "Please expedite review — this is tied to a board-level initiative with a hard Q3 deadline."
}
```

### 6.3 Example Mapping Report Summary

```
Score:     82.6 / 100.0
Grade:     B

Mapped:    38 / 42 fields
  High Confidence (≥0.90):    28 fields
  Moderate (0.70–0.89):        7 fields
  Low (0.50–0.69):             3 fields
  Unmapped:                    4 fields (all optional)

Required Fields:  21 / 21 mapped ✅
Optional Fields:  17 / 21 mapped

Issues for Human Review:  3
  1. COMPLIANCE_RISK_LEVEL — ambiguous source ("moderate" vs "potentially high")
  2. TECH_ESTIMATED_USERS — range "250-300" auto-resolved to 250
  3. REQUEST_TARGET_COMPLETION_DATE — "end of Q2" resolved to 2026-06-30

Missing Required Fields: None
```

---

*End of Data Mapping Specification*
