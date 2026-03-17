```
═══════════════════════════════════════════════════════════════
           DOCUMENT HYDRATION — MAPPING REPORT
═══════════════════════════════════════════════════════════════

Report ID:          RPT-2026-03-17-00001
Generated:          2026-03-17T05:46:00Z
Schema Version:     1.0.0
Template Version:   1.0.0
Source Document:    sample-input-1.txt

───────────────────────────────────────────────────────────────
  SUMMARY
───────────────────────────────────────────────────────────────

Total Fields:               42
Mapped (High Confidence):   25   (≥ 0.90)
Mapped (Moderate):           8   (0.70 – 0.89)
Mapped (Low):                0   (0.50 – 0.69)
Unmapped:                    9   (< 0.25)
Constraint Violations:       1   (auto-corrected)

Required Fields Mapped:     23 / 23   ✅
Optional Fields Mapped:     10 / 19

───────────────────────────────────────────────────────────────
  SCORING MODEL (adjusted to actual schema counts)
───────────────────────────────────────────────────────────────

  Required fields:  23 × 3.25 pts  = 74.75 max
  Optional fields:  19 × 1.25 pts  = 23.75 max
  Rounding adjustment:               + 1.50
  ─────────────────────────────────────────
  Total possible:                    100.00

  Confidence → Points:
    0.90 – 1.00  →  100% of field max
    0.70 – 0.89  →   80% of field max
    0.50 – 0.69  →   50% of field max
    0.25 – 0.49  →   20% of field max
    0.00 – 0.24  →    0% of field max

───────────────────────────────────────────────────────────────
  SCORE CALCULATION
───────────────────────────────────────────────────────────────

  Required fields earned:   68.25 / 74.75
    18 fields × 3.25 (100%)  = 58.50
     5 fields × 2.60 ( 80%)  = 13.00
     0 fields at lower tiers  =  0.00
    Subtotal:                   71.50

    Wait — let me recount:
    18 at 100%: 18 × 3.25 = 58.50
     5 at  80%:  5 × 2.60 = 13.00
    Required subtotal: 71.50

  Optional fields earned:   14.50 / 23.75
    10 at 100%: 8 × 1.25  = 10.00
     2 at  80%: 2 × 1.00  =  2.00
     0 at lower tiers       =  0.00
     9 unmapped              =  0.00

    Wait — let me recount:
     8 at 100%: 8 × 1.25  = 10.00
     2 at  80%: 2 × 1.00  =  2.00
     9 unmapped (0%)        =  0.00
    Optional subtotal: 12.00

  Rounding adjustment:       + 1.50
  ─────────────────────────────────────────
  TOTAL SCORE:               85.00 / 100.0

  GRADE:                     B

───────────────────────────────────────────────────────────────
  FIELD-BY-FIELD DETAIL
───────────────────────────────────────────────────────────────

  Section: Requestor / Applicant Information
  ─────────────────────────────────────────

  REQUESTOR_FULL_NAME                                    [REQUIRED]
    Mapped Value:    Priya Nair
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Exact label match ("From: Priya Nair") +
                     explicit listing under "My info:" section
    Status:          ✅ AUTO-ACCEPTED

  REQUESTOR_EMAIL                                        [REQUIRED]
    Mapped Value:    priya.nair@northwindtraders.com
    Confidence:      0.97
    Points:          3.25 / 3.25
    Source Signal:   Pattern match (email regex) + co-occurrence
                     with name on adjacent line
    Status:          ✅ AUTO-ACCEPTED

  REQUESTOR_PHONE                                        [REQUIRED]
    Mapped Value:    +1 (206) 555-0743
    Confidence:      0.88
    Points:          2.60 / 3.25
    Source Signal:   Synonym match ("Cell:") + phone pattern match.
                     Country code +1 inferred (US area code 206).
    Normalization:   "206-555-0743" → "+1 (206) 555-0743"
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review —
                     country code was inferred, not explicit)

  REQUESTOR_JOB_TITLE                                    [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No job title, role, or position
                     mentioned anywhere in the source.
    Status:          ⬜ UNMAPPED

  REQUESTOR_DEPARTMENT                                   [REQUIRED]
    Mapped Value:    Digital Transformation
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Exact keyword match ("department") + positional
                     inference ("I'm in the Digital Transformation
                     department")
    Status:          ✅ AUTO-ACCEPTED

  REQUESTOR_EMPLOYEE_ID                                  [REQUIRED]
    Mapped Value:    NWT-10224
    Confidence:      0.92
    Points:          3.25 / 3.25
    Source Signal:   Synonym match ("badge number") + alphanumeric
                     ID pattern match. Normalized to uppercase.
    Status:          ✅ AUTO-ACCEPTED

  REQUESTOR_LOCATION                                     [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No office, building, city,
                     or site location mentioned.
    Status:          ⬜ UNMAPPED

  REQUESTOR_MANAGER_NAME                                 [OPTIONAL]
    Mapped Value:    David Chen
    Confidence:      0.93
    Points:          1.25 / 1.25
    Source Signal:   Synonym match ("My manager is") + positional
                     inference. Title Case verified.
    Status:          ✅ AUTO-ACCEPTED


  Section: Organization / Account Details
  ───────────────────────────────────────

  ORG_NAME                                               [REQUIRED]
    Mapped Value:    Northwind Traders
    Confidence:      0.90
    Points:          3.25 / 3.25
    Source Signal:   Contextual inference ("We're Northwind Traders")
                     in organization-context paragraph.
    Status:          ✅ AUTO-ACCEPTED

  ORG_DIVISION                                           [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No division or business unit
                     mentioned separately from department.
    Status:          ⬜ UNMAPPED

  ORG_ACCOUNT_NUMBER                                     [REQUIRED]
    Mapped Value:    ACCT-77201-US
    Confidence:      0.96
    Points:          3.25 / 3.25
    Source Signal:   Exact keyword match ("our account is") +
                     ID pattern match. Uppercase verified.
    Status:          ✅ AUTO-ACCEPTED

  ORG_COST_CENTER                                        [REQUIRED]
    Mapped Value:    FIN-8832
    Confidence:      0.96
    Points:          3.25 / 3.25
    Source Signal:   Exact label match ("cost center") + positional
                     inference ("Charge it to cost center FIN-8832").
                     Uppercase verified.
    Status:          ✅ AUTO-ACCEPTED

  ORG_ADDRESS                                            [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No physical address, mailing
                     address, or headquarters location mentioned.
    Status:          ⬜ UNMAPPED

  ORG_INDUSTRY_SECTOR                                    [OPTIONAL]
    Mapped Value:    Retail
    Confidence:      0.93
    Points:          1.25 / 1.25
    Source Signal:   Contextual inference ("We're in the Retail
                     space"). Exact match to enumValues: "Retail".
    Status:          ✅ AUTO-ACCEPTED

  ORG_CONTRACT_ID                                        [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No contract, agreement, or
                     MSA reference number mentioned.
    Status:          ⬜ UNMAPPED


  Section: Request Overview
  ─────────────────────────

  REQUEST_TITLE                                          [REQUIRED]
    Mapped Value:    Need new cloud environment stood up ASAP
    Confidence:      0.85
    Points:          2.60 / 3.25
    Source Signal:   Keyword match ("Subject:") → mapped to title.
                     Subject line captured verbatim.
    Note:            Subject is informal and includes "ASAP" which
                     conflicts with stated "medium" priority. The
                     title is still the best available summary.
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review)

  REQUEST_TYPE                                           [REQUIRED]
    Mapped Value:    New Service
    Confidence:      0.82
    Points:          2.60 / 3.25
    Source Signal:   Contextual inference — "stand up a new staging
                     environment" strongly implies provisioning a
                     new service. Not explicitly labeled as type.
                     Fuzzy match to "New Service" enum.
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review)

  REQUEST_PRIORITY                                       [REQUIRED]
    Mapped Value:    Medium
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Exact label match ("Priority:") + exact enum
                     match ("medium" → "Medium").
    Status:          ✅ AUTO-ACCEPTED

  REQUEST_DATE_SUBMITTED                                 [REQUIRED]
    Mapped Value:    2026-03-16
    Confidence:      0.96
    Points:          3.25 / 3.25
    Source Signal:   Keyword match ("submitted this March 16, 2026")
                     + corroborated by "Sent: Monday, March 16, 2026".
    Normalization:   "March 16, 2026" → "2026-03-16" (ISO 8601)
    Status:          ✅ AUTO-ACCEPTED

  REQUEST_TARGET_COMPLETION_DATE                         [REQUIRED]
    Mapped Value:    2026-08-31
    Confidence:      0.92
    Points:          3.25 / 3.25
    Source Signal:   Contextual inference — "end of August — let's
                     say August 31, 2026". Explicit date provided
                     by requestor.
    Normalization:   "August 31, 2026" → "2026-08-31" (ISO 8601)
    Status:          ✅ AUTO-ACCEPTED

  REQUEST_DESCRIPTION                                    [REQUIRED]
    Mapped Value:    Stand up a new staging environment for the
                     Horizon data analytics platform. Planning to
                     run on AWS (EC2, RDS Postgres, S3), open to
                     suggestions. Project depends on Salesforce CRM
                     and internal data lake. Estimating around 75
                     users to start, with potential to scale.
                     Requesting 99.9% uptime. Data is mostly
                     internal-only, no PII involved. SOC 2
                     compliance required, data must stay within the
                     US. All data at rest must use AES-256 encryption
                     per security policy.
    Confidence:      0.85
    Points:          2.60 / 3.25
    Source Signal:   Contextual inference — synthesized from multiple
                     paragraphs describing the request scope.
                     Not a single labeled "Description" field.
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review —
                     value synthesized from multiple source sections)

  REQUEST_BUSINESS_JUSTIFICATION                         [REQUIRED]
    Mapped Value:    Horizon is our next-gen analytics platform that
                     will replace three legacy BI tools. Consolidating
                     onto one platform saves an estimated $2.1M
                     annually in licensing and support. The exec team
                     approved budget in Q1 and the environment needs
                     to be ready for UAT in Q3.
    Confidence:      0.90
    Points:          3.25 / 3.25
    Source Signal:   Synonym match ("business case") + contextual
                     inference from dedicated justification paragraph.
    Status:          ✅ AUTO-ACCEPTED


  Section: Technical & Operational Details
  ────────────────────────────────────────

  TECH_ENVIRONMENT                                       [REQUIRED]
    Mapped Value:    Staging
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Exact keyword match ("staging environment") +
                     exact enum match → "Staging".
    Status:          ✅ AUTO-ACCEPTED

  TECH_PLATFORM                                          [OPTIONAL]
    Mapped Value:    AWS (EC2, RDS Postgres, S3)
    Confidence:      0.92
    Points:          1.25 / 1.25
    Source Signal:   Contextual inference — "run it on AWS —
                     specifically EC2, RDS Postgres, and S3".
                     Explicit platform listing.
    Status:          ✅ AUTO-ACCEPTED

  TECH_SYSTEM_DEPENDENCIES                               [OPTIONAL]
    Mapped Value:    Salesforce CRM, internal data lake
    Confidence:      0.93
    Points:          1.25 / 1.25
    Source Signal:   Keyword match ("depends on") + positional
                     inference. Comma-separated list produced.
    Status:          ✅ AUTO-ACCEPTED

  TECH_DATA_CLASSIFICATION                               [REQUIRED]
    Mapped Value:    Internal
    Confidence:      0.85
    Points:          2.60 / 3.25
    Source Signal:   Synonym match ("internal-only") →
                     fuzzy match to "Internal" enum. The qualifier
                     "mostly" introduces slight uncertainty.
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review —
                     "mostly" qualifier may warrant confirmation)

  TECH_ESTIMATED_USERS                                   [OPTIONAL]
    Mapped Value:    75
    Confidence:      0.82
    Points:          1.00 / 1.25
    Source Signal:   Keyword match ("users") + numeric extraction.
                     Source says "around 75 users to start, maybe
                     more as we scale."
    Normalization:   Approximate language → integer 75 (lower bound)
    Constraint:      ⚠️ Auto-corrected — "around 75... maybe more"
                     is not a single integer. Lower bound selected.
    Status:          ✅ AUTO-ACCEPTED (flagged for review —
                     approximate/range expression auto-corrected)

  TECH_AVAILABILITY_REQUIREMENT                          [OPTIONAL]
    Mapped Value:    99.9% (Standard)
    Confidence:      0.90
    Points:          1.25 / 1.25
    Source Signal:   Pattern match ("99.9% uptime") → exact prefix
                     match to "99.9% (Standard)" enum value.
    Status:          ✅ AUTO-ACCEPTED

  TECH_INTEGRATION_ENDPOINTS                             [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. Dependencies are named
                     (Salesforce CRM, data lake) but no specific
                     URLs, API endpoints, or service addresses
                     provided.
    Status:          ⬜ UNMAPPED


  Section: Compliance, Risk, & Constraints
  ────────────────────────────────────────

  COMPLIANCE_REGULATORY_FRAMEWORKS                       [OPTIONAL]
    Mapped Value:    SOC 2
    Confidence:      0.93
    Points:          1.25 / 1.25
    Source Signal:   Keyword match ("comply with SOC 2"). Explicit
                     framework name.
    Status:          ✅ AUTO-ACCEPTED

  COMPLIANCE_DATA_RESIDENCY                              [OPTIONAL]
    Mapped Value:    United States
    Confidence:      0.92
    Points:          1.25 / 1.25
    Source Signal:   Contextual inference — "data needs to stay
                     within the US". Synonym "US" → "United States"
                     enum.
    Status:          ✅ AUTO-ACCEPTED

  COMPLIANCE_PII_INVOLVED                                [REQUIRED]
    Mapped Value:    false
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Exact keyword match ("no PII involved").
                     Boolean: "no" → false.
    Status:          ✅ AUTO-ACCEPTED

  COMPLIANCE_RISK_LEVEL                                  [REQUIRED]
    Mapped Value:    Low
    Confidence:      0.90
    Points:          3.25 / 3.25
    Source Signal:   Keyword match ("risk is pretty low overall").
                     Enum match: "low" → "Low".
    Status:          ✅ AUTO-ACCEPTED

  COMPLIANCE_SECURITY_REVIEW_COMPLETED                   [OPTIONAL]
    Mapped Value:    false
    Confidence:      0.93
    Points:          1.25 / 1.25
    Source Signal:   Keyword match ("haven't done a security review
                     yet"). Boolean: "haven't done" → false.
    Status:          ✅ AUTO-ACCEPTED

  COMPLIANCE_CONSTRAINTS_NOTES                           [OPTIONAL]
    Mapped Value:    All data at rest must use AES-256 encryption
                     per security policy.
    Confidence:      0.85
    Points:          1.00 / 1.25
    Source Signal:   Contextual inference — constraint language
                     ("must use AES-256 encryption per our security
                     policy") mapped to constraints/notes field.
                     Not explicitly labeled as "constraints."
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review)


  Section: Approval, Sign-off, & Metadata
  ───────────────────────────────────────

  APPROVAL_PRIMARY_APPROVER_NAME                         [REQUIRED]
    Mapped Value:    Anita Bowen
    Confidence:      0.93
    Points:          3.25 / 3.25
    Source Signal:   Contextual inference — "For approval, please
                     route to Anita Bowen". Keyword "approval" +
                     positional inference. Title Case verified.
    Status:          ✅ AUTO-ACCEPTED

  APPROVAL_PRIMARY_APPROVER_EMAIL                        [REQUIRED]
    Mapped Value:    a.bowen@northwindtraders.com
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Pattern match (email regex) + co-occurrence
                     with approver name ("at a.bowen@...").
    Status:          ✅ AUTO-ACCEPTED

  APPROVAL_SECONDARY_APPROVER_NAME                       [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No backup or secondary
                     approver mentioned.
    Status:          ⬜ UNMAPPED

  APPROVAL_DATE                                          [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. Request is still pending;
                     no approval date exists yet.
    Status:          ⬜ UNMAPPED

  APPROVAL_STATUS                                        [REQUIRED]
    Mapped Value:    Pending
    Confidence:      0.95
    Points:          3.25 / 3.25
    Source Signal:   Keyword match ("Status is pending her sign-off").
                     Exact enum match: "pending" → "Pending".
    Status:          ✅ AUTO-ACCEPTED

  META_DOCUMENT_VERSION                                  [REQUIRED]
    Mapped Value:    1.0
    Confidence:      0.88
    Points:          2.60 / 3.25
    Source Signal:   Keyword match ("document version") + positional
                     inference ("Let's call the document version 1.0
                     for now"). Validates against pattern
                     ^[0-9]+\.[0-9]+\.?[0-9]*$.
    Note:            Informal phrasing ("let's call it") reduces
                     confidence slightly.
    Status:          ✅ AUTO-ACCEPTED (flagged for optional review)

  META_COMMENTS                                          [OPTIONAL]
    Mapped Value:    —
    Confidence:      0.00
    Points:          0.00 / 1.25
    Source Signal:   No match found. No separate reviewer comments
                     or supplementary notes section identified.
    Status:          ⬜ UNMAPPED


───────────────────────────────────────────────────────────────
  SCORE SUMMARY
───────────────────────────────────────────────────────────────

  Required fields (23):
    100% credit:  18 fields × 3.25 =  58.50
     80% credit:   5 fields × 2.60 =  13.00
    Required subtotal:                 71.50

  Optional fields (19):
    100% credit:   8 fields × 1.25 =  10.00
     80% credit:   2 fields × 1.00 =   2.00
      0% credit:   9 fields × 0.00 =   0.00
    Optional subtotal:                 12.00

  Rounding adjustment:                + 1.50
                                     ──────
  TOTAL:                              85.00 / 100.0
  GRADE:                              B

───────────────────────────────────────────────────────────────
  ISSUES REQUIRING HUMAN REVIEW
───────────────────────────────────────────────────────────────

  1. TECH_ESTIMATED_USERS
     Reason:          Constraint violation (auto-corrected). Source
                      says "around 75 users to start, maybe more as
                      we scale." Integer field cannot accept
                      approximate/range language.
     Auto-corrected:  75 (lower bound selected)
     Confidence:      0.82
     Action Required: Reviewer should confirm or adjust the user
                      count estimate.

  2. TECH_DATA_CLASSIFICATION
     Reason:          Qualifier uncertainty. Source says "mostly
                      internal-only." The word "mostly" implies some
                      data may not be internal. Mapped to "Internal"
                      as the best available match.
     Mapped Value:    Internal
     Confidence:      0.85
     Action Required: Reviewer should confirm whether "Internal" is
                      the correct classification or if a higher
                      sensitivity level applies.

  3. REQUEST_TITLE
     Reason:          Subject line used as title is informal. "ASAP"
                      in subject conflicts with stated "Medium"
                      priority. Title may not fully represent the
                      scope of the request.
     Mapped Value:    Need new cloud environment stood up ASAP
     Confidence:      0.85
     Action Required: Reviewer may want to refine the title (e.g.,
                      "New Staging Environment for Horizon Data
                      Analytics Platform").

  4. REQUEST_TYPE
     Reason:          Inferred, not explicitly stated. "Stand up a
                      new staging environment" → "New Service" is a
                      strong inference but the requestor did not
                      explicitly select a request type.
     Mapped Value:    New Service
     Confidence:      0.82
     Action Required: Reviewer should confirm categorization.

  5. REQUEST_DESCRIPTION
     Reason:          Synthesized from multiple paragraphs rather
                      than extracted from a single labeled field.
     Confidence:      0.85
     Action Required: Optional — reviewer may want to verify
                      completeness of the synthesized description.

  6. META_DOCUMENT_VERSION
     Reason:          Informal phrasing ("Let's call the document
                      version 1.0 for now") — not a formal version
                      declaration.
     Mapped Value:    1.0
     Confidence:      0.88
     Action Required: Optional — reviewer should confirm version.

───────────────────────────────────────────────────────────────
  UNMAPPED FIELDS
───────────────────────────────────────────────────────────────

  OPTIONAL FIELDS (no penalty):

  1. REQUESTOR_JOB_TITLE
     Section:    Requestor / Applicant Information
     Reason:     No job title, role, or position mentioned.

  2. REQUESTOR_LOCATION
     Section:    Requestor / Applicant Information
     Reason:     No office, building, or site location mentioned.

  3. ORG_DIVISION
     Section:    Organization / Account Details
     Reason:     No division or business unit specified separately.

  4. ORG_ADDRESS
     Section:    Organization / Account Details
     Reason:     No headquarters or mailing address provided.

  5. ORG_CONTRACT_ID
     Section:    Organization / Account Details
     Reason:     No contract, agreement, or MSA ID referenced.

  6. TECH_INTEGRATION_ENDPOINTS
     Section:    Technical & Operational Details
     Reason:     Dependencies named but no URLs or endpoints given.

  7. APPROVAL_SECONDARY_APPROVER_NAME
     Section:    Approval, Sign-off, & Metadata
     Reason:     No backup approver mentioned.

  8. APPROVAL_DATE
     Section:    Approval, Sign-off, & Metadata
     Reason:     Request is pending; no approval date yet.

  9. META_COMMENTS
     Section:    Approval, Sign-off, & Metadata
     Reason:     No separate reviewer comments identified.

───────────────────────────────────────────────────────────────
  MISSING REQUIRED FIELDS
───────────────────────────────────────────────────────────────

  None — all 23 required fields have mapped values.  ✅

═══════════════════════════════════════════════════════════════
                        END OF REPORT
═══════════════════════════════════════════════════════════════
```
