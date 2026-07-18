# ESS–TTM STAGE 0 — KNOWLEDGE UNIT DEFINITION 001

**Experiment Identifier:** ESS-TTM-STAGE-0-001
**Date:** 2026-07-18
**Status:** KNOWLEDGE UNIT DRAFT
**Operating Posture:** SYNTHETIC / BOUNDED / NON-PRODUCTION / NON-ADMITTING / UNKNOWN → HOLD

---

# 1. PURPOSE

This document defines the exact synthetic knowledge unit used in the ESS–TTM Stage 0 Pilot Calibration.

The knowledge unit must remain stable throughout the experiment.

Any change to its identity, scope, declared use, evidence, authority source, context, or sufficiency conditions requires a documented protocol deviation.

---

# 2. KNOWLEDGE UNIT IDENTIFIER

```text
ESS-TTM-KU-001
```

Canonical name:

```text
Synthetic Runtime Inspection Report Eligibility Claim
```

---

# 3. KNOWLEDGE UNIT STATEMENT

The knowledge unit is:

```text
A specific RuntimeRecordInspectionReport is eligible to support
one bounded, read-only repository review under a declared scope,
authority source, operational context, and time window.
```

This is a synthetic research claim.

It is not a production authorization.

---

# 4. DECLARED USE

The knowledge unit may be considered only for:

```text
one read-only review
of one declared repository state
for one declared reviewer purpose
within one declared temporal window
```

The declared use excludes:

```text
code execution
repository modification
Git mutation
release approval
deployment approval
production authorization
financial action
medical action
legal action
```

---

# 5. SUBJECT REPORT

The subject report is:

```text
one immutable RuntimeRecordInspectionReport instance
```

The exact report instance must be identified before execution through:

```text
record_id
record_type
record_category
append_position
recorded_at
schema_version
provenance_ref
external_id
declared_fields
```

The report must not be replaced during the experiment without a protocol deviation.

---

# 6. EVIDENCE BASIS

The initial evidence basis may include:

```text
the immutable inspection report
its deterministic primitive representation
its deterministic JSON text
its deterministic UTF-8 bytes
its SHA-256 digest
its digest manifest
embedded report integrity verification
report-derived manifest binding verification
```

These artifacts establish only mechanical evidence about representation, bytes, digest, length, BOM posture, and reconstruction.

They do not establish current admissibility.

---

# 7. EVIDENCE DIMENSION

The evidence dimension asks:

```text
Does the preserved evidence remain intact, identifiable, and reconstructable?
```

Candidate observations:

```text
report exists
report identity is stable
report representation is deterministic
report bytes match manifest claims
report-derived manifest binding matches
```

Evidence status must remain separate from all other dimensions.

Boundary:

```text
Evidence Intact
≠
Current Use Sufficient
```

---

# 8. AUTHORITY SOURCE

The synthetic authority source is:

```text
a bounded Stage 0 protocol declaration authorizing
read-only review of ESS-TTM-KU-001 only
```

The authority source does not authorize:

```text
production execution
repository mutation
external publication
admission
trust
deployment
```

The authority source must be attributable and time-bounded.

---

# 9. AUTHORITY DIMENSION

The authority dimension asks:

```text
Does the declared authority still exist for this exact use,
scope, subject, reviewer role, and time?
```

Authority may change independently of evidence.

Example:

```text
the report remains intact
but the reviewer authorization expires
```

Boundary:

```text
Evidence Preserved
≠
Authority Preserved
```

---

# 10. OPERATIONAL CONTEXT

The initial operational context is:

```text
Research OS
master branch
controlled local repository
synthetic Stage 0 experiment
read-only review posture
no production consequence
```

The exact repository commit must be recorded in `EVENT_TIMELINE.md`.

Context must not be assumed stable merely because the report remains unchanged.

---

# 11. CONTEXT DIMENSION

The context dimension asks:

```text
Does the current environment still match the environment
for which the knowledge unit was verified?
```

Context-change examples include:

```text
repository HEAD changes
branch changes
inspection target changes
runtime assumptions change
review purpose changes
required evidence changes
```

Boundary:

```text
Same Report
≠
Same Context
```

---

# 12. SCOPE

The authorized scope is:

```text
one report
one repository state
one bounded read-only review
one declared reviewer purpose
one declared temporal window
```

The knowledge unit may not be reused for:

```text
another repository
another branch
another commit
another report
another reviewer purpose
another consequence class
```

without explicit revalidation.

---

# 13. SCOPE DIMENSION

The scope dimension asks:

```text
Does the proposed use remain inside the originally declared boundary?
```

Boundary:

```text
Related Use
≠
Authorized Use
```

---

# 14. SUFFICIENCY CONDITIONS

The knowledge unit is sufficient for the declared use only if all required current conditions are demonstrably present.

Required sufficiency conditions:

```text
subject report identity is established
mechanical integrity evidence remains available
binding verification remains available
authority remains current
context remains aligned
scope remains unchanged
required evidence is complete
no unresolved contradiction affects use
no protocol deviation invalidates the basis
```

No aggregate score may substitute for these conditions.

---

# 15. SUFFICIENCY DIMENSION

The sufficiency dimension asks:

```text
Is the currently available evidence enough
for this exact use at this exact time?
```

Sufficiency may fail even when the report is historically correct.

Example:

```text
the report accurately describes an earlier repository state
but the current repository HEAD has changed
```

Boundary:

```text
Historically Correct
≠
Currently Sufficient
```

---

# 16. TEMPORAL FIELDS

The knowledge unit requires separate fields for:

```text
creation_time
verification_time
condition_change_time
expiry_time
execution_time
revalidation_time
```

Each field must have a distinct meaning.

No single timestamp may substitute for the full lifecycle.

---

# 17. CREATION TIME

Creation time means:

```text
the moment ESS-TTM-KU-001 is first recorded as a candidate knowledge unit
```

Creation does not imply verification.

Boundary:

```text
Created
≠
Verified
```

---

# 18. VERIFICATION TIME

Verification time means:

```text
the moment the knowledge unit first satisfies
the predefined structural verification conditions
```

Verification does not imply future execution standing.

Boundary:

```text
Verified Previously
≠
Valid For Later Use
```

---

# 19. CONDITION-CHANGE TIME

Condition-change time means:

```text
the first observed moment when authority, context,
scope, evidence, or sufficiency may no longer match
the verified state
```

A condition change may occur without changing the report itself.

---

# 20. EXPIRY TIME

Expiry time means:

```text
the declared end of the knowledge unit’s permitted usage window
```

Expiry may be:

```text
time-based
condition-based
event-based
```

An expired unit cannot regain standing through timestamp replacement alone.

---

# 21. EXECUTION TIME

Execution time means:

```text
the moment the knowledge unit is proposed for actual use
within the Stage 0 review procedure
```

The experiment must inspect current standing at this moment.

Boundary:

```text
Prior Standing
≠
Execution-Time Standing
```

---

# 22. REVALIDATION TIME

Revalidation time means:

```text
the moment a documented attempt is made
to restore or renew standing after change, degradation, or expiry
```

Revalidation must document:

```text
what was rechecked
who performed the review
under what authority
for which scope
against which evidence
until what time or condition
```

---

# 23. INITIAL SYNTHETIC STATE

Before the controlled event sequence begins:

```text
knowledge unit: CREATED
evidence: PRESENT
authority: PROVISIONAL
context: DECLARED
scope: DECLARED
sufficiency: NOT YET VERIFIED
execution: NOT ATTEMPTED
classification: HOLD
```

---

# 24. CONTROLLED CONDITION CHANGE

The first experiment will introduce one synthetic condition change:

```text
repository HEAD changes after verification
but before proposed execution-time use
```

The report and its integrity evidence remain unchanged.

This is intended to test whether the instruments distinguish:

```text
historical integrity
from
current contextual sufficiency
```

---

# 25. EXPECTED DIMENSION EFFECT

The controlled change is expected to permit:

```text
evidence: unchanged
authority: unchanged unless separately altered
context: changed
scope: unchanged
sufficiency: unresolved pending review
```

This expectation is not the result.

The actual observation must be recorded independently.

---

# 26. REVALIDATION SCENARIO

After the condition change, revalidation will require:

```text
inspection of the new repository state
confirmation of the declared review purpose
confirmation of authority
confirmation of scope
creation of new or updated evidence where required
documented reviewer attribution
new validity boundary
```

The original report must remain preserved.

It must not be rewritten to conceal the earlier state.

---

# 27. IDENTITY BOUNDARY

ESS-TTM-KU-001 is identified by:

```text
knowledge unit identifier
subject report identifier
declared repository commit
declared use
declared scope
declared authority source
declared temporal window
```

Changing any material identity field creates a new candidate knowledge unit or requires a protocol deviation.

---

# 28. PROVENANCE BOUNDARY

The experiment may record provenance references.

It does not claim that provenance alone proves:

```text
truth
independence
authority
sufficiency
admissibility
```

Boundary:

```text
Provenance Recorded
≠
Standing Established
```

---

# 29. EXTERNAL REVIEW BOUNDARY

External review may assess the knowledge unit.

External review does not automatically establish causal independence.

Boundary:

```text
External Reviewer
≠
Independent Origin
```

---

# 30. EXCLUSION BOUNDARIES

ESS-TTM-KU-001 does not include:

```text
a trust score
a causal-independence proof
an execution authorization
a production workflow
a live external witness
a constitutional ESS decision
a TTM validation result
```

---

# 31. FAILURE CONDITIONS

The knowledge-unit definition fails if:

```text
the report subject is ambiguous
the repository state is not identified
the declared use changes silently
authority is unspecified
scope is undefined
sufficiency conditions are incomplete
timestamps are collapsed
the controlled condition change cannot be distinguished
```

---

# 32. REQUIRED SUPPORTING ARTIFACTS

The knowledge unit must later reference:

```text
EVENT_TIMELINE.md
EXECUTION_RECORD.md
evidence/
observations/
reviews/
```

No evidence files are authorized yet.

---

# 33. INITIAL DECISION

```text
Knowledge unit identifier: FROZEN CANDIDATE
Subject report type: DEFINED
Declared use: DEFINED
Evidence dimension: DEFINED
Authority dimension: DEFINED
Context dimension: DEFINED
Scope dimension: DEFINED
Sufficiency dimension: DEFINED
Temporal fields: DEFINED
Controlled condition change: DEFINED
Production consequence: NONE
Execution: HOLD
```

---

# 34. NEXT AUTHORIZED ARTIFACT

```text
EVENT_TIMELINE.md
```

That document must freeze:

```text
T0 through T6
the exact controlled event order
required observations at each event
the repository commit or synthetic state attached to each event
the prohibition on hidden retries
```

---

# 35. FINAL STATUS

```text
Synthetic knowledge unit: DEFINED
Identity boundary: DEFINED
Declared use: BOUNDED
Evidence basis: BOUNDED
Authority source: PROVISIONAL
Context: DECLARED
Scope: BOUNDED
Sufficiency conditions: PREDEFINED
Temporal lifecycle: DEFINED
Controlled condition change: DEFINED
Execution: HOLD
Observation collection: HOLD
Validation claim: NONE
UNKNOWN → HOLD
```
