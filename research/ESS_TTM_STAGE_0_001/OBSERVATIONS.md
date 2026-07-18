# ESS–TTM STAGE 0 — OBSERVATIONS 001

**Experiment Identifier:** ESS-TTM-STAGE-0-001
**Knowledge Unit:** ESS-TTM-KU-001
**Date:** 2026-07-18
**Status:** OBSERVATION TEMPLATE
**Operating Posture:** DIMENSION-SEPARATED / EVIDENCE-BOUND / NON-ADMITTING / UNKNOWN → HOLD

---

# 1. PURPOSE

This document provides the observation format for the ESS–TTM Stage 0 Pilot Calibration.

It records what is observed about the five temporal-trust dimensions at each relevant event.

It does not authorize execution, validate TTM, certify ESS, or establish causal independence.

---

# 2. OBSERVATION DIMENSIONS

Every current-standing review must assess separately:

```text
evidence
authority
context
scope
sufficiency
```

No dimension may be omitted silently.

No single aggregate score may replace these observations.

---

# 3. PERMITTED OBSERVATION STATES

Each dimension must be assigned exactly one observation state:

```text
SUPPORTED
DEGRADED
UNSUPPORTED
UNKNOWN
NOT OBSERVED
```

These are descriptive observation states.

They are not execution decisions.

---

# 4. OBSERVATION IDENTIFIER FORMAT

Canonical identifiers:

```text
OBS-T0-001
OBS-T1-001
OBS-T2-001
OBS-T3-001
OBS-T4-001
OBS-T5-001
OBS-T6-001
```

Additional observations use increasing suffixes.

Identifiers do not imply validity or completion.

---

# 5. REQUIRED OBSERVATION FIELDS

Every observation must include:

```text
observation_id
event_id
observed_time
reviewer
reviewer_role
knowledge_unit_id
repository_branch
repository_head
dimension
observed_state
supporting_evidence
contradictory_evidence
unknowns
assumptions
protocol_deviation_reference
interpretive_limit
```

---

# 6. SUPPORTING-EVIDENCE RULE

Every non-UNKNOWN state must identify the evidence supporting it.

A conclusion without an evidence reference is insufficient.

Permitted evidence references may include:

```text
execution-record entry
subject report
manifest
integrity verification
binding verification
Git output
authority declaration
scope declaration
timeline event
review note
```

---

# 7. CONTRADICTORY EVIDENCE

Every observation must provide a place for contradictory evidence.

When none is observed, record:

```text
None observed within the bounded review.
```

This does not establish that no contradiction exists outside the reviewed evidence.

---

# 8. UNKNOWN PRESERVATION

Unknowns must remain explicit.

Unknowns may not be converted into:

```text
SUPPORTED
UNSUPPORTED
approved
rejected
trusted
authorized
```

through assumption or reviewer preference.

Boundary:

```text
Unresolved
≠
False
```

---

# 9. ASSUMPTION REGISTER

Any assumption used during observation must be declared.

An assumption must not be written as evidence.

Each assumption must state:

```text
assumption
reason used
affected dimension
effect if false
```

---

# 10. EVIDENCE DIMENSION

Question:

```text
Does the preserved evidence remain intact,
identifiable, available, and reconstructable?
```

Candidate evidence includes:

```text
subject report identity
deterministic representation
JSON text
UTF-8 bytes
digest
manifest
integrity result
binding result
```

The evidence observation must not infer:

```text
current authority
context alignment
scope alignment
current sufficiency
```

---

# 11. AUTHORITY DIMENSION

Question:

```text
Does the declared authority still exist
for this exact subject, use, scope, role, and time?
```

Authority evidence may include:

```text
protocol declaration
role declaration
time boundary
scope restriction
revocation or expiry record
```

Integrity evidence cannot substitute for authority evidence.

---

# 12. CONTEXT DIMENSION

Question:

```text
Does the current operational environment still match
the environment associated with verification?
```

Relevant observations include:

```text
branch
HEAD commit
working-tree state
inspection target
review purpose
runtime assumptions
required evidence set
```

A context observation must identify the compared states.

---

# 13. SCOPE DIMENSION

Question:

```text
Does the proposed use remain inside the declared boundary?
```

Relevant boundaries include:

```text
subject report
repository
branch
commit
review purpose
reviewer role
time window
consequence class
```

Similarity does not establish scope inclusion.

---

# 14. SUFFICIENCY DIMENSION

Question:

```text
Is the currently available evidence enough
for this exact use at this exact time?
```

Sufficiency must be assessed after the other four dimensions remain separately visible.

No automatic conjunction or score is authorized.

Sufficiency may remain UNKNOWN even when several dimensions are SUPPORTED.

---

# 15. T0 OBSERVATION

## T0 — Knowledge Unit Creation

```text
Observation status: NOT STARTED
```

Required focus:

```text
identity recorded
declared use recorded
authority source declared
context declared
scope declared
sufficiency not yet verified
```

---

# 16. T1 OBSERVATION

## T1 — Structural Verification

```text
Observation status: NOT STARTED
```

Required focus:

```text
mechanical evidence availability
subject identity
integrity result
binding result
verified repository state
verification time
```

Expected distinctions:

```text
mechanical evidence may be supported
execution-time sufficiency remains provisional
```

---

# 17. T2 OBSERVATION

## T2 — Controlled Condition Change

```text
Observation status: NOT STARTED
```

Required focus:

```text
pre-change HEAD
post-change HEAD
report unchanged or changed
manifest unchanged or changed
authority changed or unchanged
scope changed or unchanged
context effect
sufficiency effect
```

---

# 18. T3 OBSERVATION

## T3 — Proposed Execution-Time Use

```text
Observation status: NOT STARTED
```

Required focus:

```text
proposed use
current repository state
current authority
current context
current scope
available evidence
known contradictions
unknowns
```

No execution permission may be inferred.

---

# 19. T4 OBSERVATION

## T4 — Current-Standing Review

```text
Observation status: NOT STARTED
```

This is the primary five-dimension observation point.

Use one complete observation block for each dimension.

### Observation Block

```text
observation_id:
event_id: T4
observed_time:
reviewer:
reviewer_role:
knowledge_unit_id: ESS-TTM-KU-001
repository_branch:
repository_head:

dimension:

observed_state:

supporting_evidence:

contradictory_evidence:

unknowns:

assumptions:

protocol_deviation_reference:

interpretive_limit:
```

---

# 20. T5 OBSERVATION

## T5 — Revalidation Attempt

```text
Observation status: NOT STARTED
```

Required focus:

```text
what was revalidated
new evidence
authority for revalidation
current scope
new temporal boundary
remaining unknowns
whether original evidence remained preserved
```

Renewal must not be inferred from a new timestamp alone.

---

# 21. T6 OBSERVATION

## T6 — Final Calibration Observation

```text
Observation status: NOT STARTED
```

Required focus:

```text
temporal-event distinguishability
dimension distinguishability
event reconstruction
unknown preservation
deviation visibility
role separation
review reproducibility
claim discipline
```

T6 observes the instruments and procedure—not the truth of TTM.

---

# 22. REVIEWER INDEPENDENCE FIELD

Every reviewer observation must identify the reviewer’s relationship to:

```text
ESS
TTM
Research OS
protocol design
experiment execution
```

An external reviewer must not automatically be described as independent.

---

# 23. DISAGREEMENT RECORD

When reviewers disagree, record:

```text
disagreement_id
observation identifiers
disputed dimension
reviewer A interpretation
reviewer B interpretation
evidence cited by each
classification impact
disposition status
```

Unresolved material disagreement forces HOLD.

---

# 24. NO CONSENSUS SUBSTITUTION

Reviewer agreement alone does not prove the observation.

Boundary:

```text
Reviewer Agreement
≠
Independent Truth
```

Agreement must remain traceable to the evidence basis.

---

# 25. NO CAUSAL-INDEPENDENCE INFERENCE

The observation instrument may record:

```text
declared sources
provenance references
reviewer separation
apparent lineage differences
```

It may not classify causal independence as proven.

Boundary:

```text
Distinct Sources Observed
≠
Causal Orthogonality Established
```

---

# 26. OBSERVATION CORRECTION

Observation corrections must be appended.

A correction must include:

```text
correction_id
original observation_id
incorrect field
corrected value
reason
reviewer
time
effect on interpretation
```

The original observation remains preserved.

---

# 27. PROTOCOL DEVIATION LINK

Every observation must reference:

```text
NONE
DEV-001
DEV-002
...
UNKNOWN — REVIEW REQUIRED
```

Observations affected by unresolved deviations cannot support PASS.

---

# 28. OBSERVATION LIMITATIONS

This instrument cannot establish:

```text
truth
causal independence
execution authority
admission
trust
production safety
TTM validity
ESS validity
```

It records bounded reviewer observations only.

---

# 29. PRE-EXECUTION STATE

```text
T0 observations: NONE
T1 observations: NONE
T2 observations: NONE
T3 observations: NONE
T4 observations: NONE
T5 observations: NONE
T6 observations: NONE
Reviewer disagreements: NONE RECORDED
Observation corrections: NONE RECORDED
Observation collection: HOLD
```

---

# 30. NEXT AUTHORIZED ARTIFACT

```text
PROTOCOL_DEVIATIONS.md
```

That document must define the append-only deviation format for:

```text
criteria changes
event-sequence changes
role substitutions
missing evidence
hidden or proposed retries
repository-state surprises
instrument failures
interpretive impact
```

---

# 31. FINAL STATUS

```text
Five dimensions: DEFINED
Observation states: DEFINED
Evidence citation: REQUIRED
Contradictory evidence: REQUIRED
Unknown preservation: REQUIRED
Assumption declaration: REQUIRED
Reviewer attribution: REQUIRED
Disagreement recording: DEFINED
Aggregate score: PROHIBITED
Causal-independence inference: PROHIBITED
Observation collection: HOLD
UNKNOWN → HOLD
```
