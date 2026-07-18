# ESS–TTM STAGE 0 — PROTOCOL DEVIATIONS 001

**Experiment Identifier:** ESS-TTM-STAGE-0-001
**Knowledge Unit:** ESS-TTM-KU-001
**Date:** 2026-07-18
**Status:** PROTOCOL DEVIATION TEMPLATE
**Operating Posture:** APPEND-ONLY / EXPLICIT-DEVIATION / NO-SILENT-CORRECTION / UNKNOWN → HOLD

---

# 1. PURPOSE

This document provides the append-only record for protocol deviations arising during the ESS–TTM Stage 0 Pilot Calibration.

A protocol deviation is any material departure from the frozen experiment design, role structure, event sequence, criteria, evidence requirements, or recording procedure.

A deviation does not automatically invalidate the experiment.

It must remain visible and its effect must be assessed.

---

# 2. APPEND-ONLY RULE

Once execution begins:

```text
existing deviation entries must not be rewritten or deleted
```

Corrections must be appended as new records referencing the original deviation.

Boundary:

```text
Deviation Correction
≠
Deviation Erasure
```

---

# 3. DEVIATION IDENTIFIER FORMAT

Canonical format:

```text
DEV-001
DEV-002
DEV-003
```

Identifiers must be unique and sequential.

An identifier does not imply severity or resolution.

---

# 4. REQUIRED DEVIATION FIELDS

Every deviation must include:

```text
deviation_id
observed_time
reported_by
reporter_role
event_id
affected_artifact
deviation_type
original_requirement
observed_departure
reason
raw_evidence_reference
known_effect
unknown_effect
classification_impact
corrective_action
review_required
review_status
final_disposition
```

---

# 5. DEVIATION TYPES

Permitted deviation types:

```text
CRITERIA_CHANGE
EVENT_SEQUENCE_CHANGE
ROLE_SUBSTITUTION
MISSING_EVIDENCE
UNRECORDED_OR_PROPOSED_RETRY
REPOSITORY_STATE_SURPRISE
INSTRUMENT_FAILURE
COMMAND_VARIATION
TIMESTAMP_AMBIGUITY
KNOWLEDGE_UNIT_CHANGE
SCOPE_CHANGE
AUTHORITY_CHANGE
CONTEXT_CHANGE
RECORDING_ERROR
OTHER
```

`OTHER` requires a plain-language explanation.

---

# 6. CRITERIA CHANGE

A criteria change occurs when any PASS, PARTIAL, FAIL, or HOLD condition is altered after execution begins.

Required record:

```text
original criterion
proposed revised criterion
reason
time of change
person proposing change
effect on comparability
effect on classification
```

The original criterion remains authoritative for the initial run unless the deviation is independently reviewed.

---

# 7. EVENT-SEQUENCE CHANGE

An event-sequence deviation includes:

```text
event reordered
event skipped
event repeated
event merged
event substituted
event interrupted materially
```

Required effect assessment:

```text
whether temporal reconstruction remains possible
whether later observations remain interpretable
whether restart is required
```

---

# 8. ROLE SUBSTITUTION

A role deviation occurs when:

```text
an assigned actor becomes unavailable
one person assumes another role
independence conditions change
review authority changes
```

The substitute actor must declare:

```text
relationship to ESS
relationship to TTM
relationship to Research OS
relationship to protocol design
relationship to execution
```

Unreviewed role substitution forces HOLD.

---

# 9. MISSING EVIDENCE

Missing evidence includes:

```text
expected report absent
manifest absent
Git output absent
raw command output not preserved
authority declaration absent
scope declaration absent
review note absent
timestamp absent
```

A missing-evidence deviation must not be resolved through inference alone.

---

# 10. RETRY DEVIATION

A retry deviation occurs when:

```text
a command is repeated without prior retry proposal
inputs change during a retry
environment changes during a retry
a failed attempt is omitted
```

Every retry must remain separately visible.

Boundary:

```text
Successful Retry
≠
Original Procedure Uninterrupted
```

---

# 11. REPOSITORY-STATE SURPRISE

A repository-state surprise includes:

```text
unexpected branch
unexpected HEAD
working tree not clean
untracked evidence appears
remote state differs from assumption
repository changes between events
```

The surprise must record the raw Git output.

No repository-state surprise may be summarized away.

---

# 12. INSTRUMENT FAILURE

An instrument failure includes:

```text
template cannot capture required information
field meaning is ambiguous
reviewers use fields inconsistently
document cannot preserve raw output
dimension separation collapses
timestamp semantics fail
```

Instrument failure is scientifically relevant.

It may support PARTIAL, FAIL, or HOLD.

---

# 13. COMMAND VARIATION

A command variation occurs when the executed command differs materially from the predeclared command.

Required comparison:

```text
declared command
executed command
reason
changed inputs
changed outputs
effect on interpretation
```

Minor formatting differences may be classified as non-material only with rationale.

---

# 14. TIMESTAMP AMBIGUITY

Timestamp ambiguity includes:

```text
time unavailable
timezone missing
event order uncertain
creation and verification times collapsed
execution and revalidation times confused
```

Ambiguity affecting event order forces HOLD until reviewed.

---

# 15. KNOWLEDGE-UNIT CHANGE

A knowledge-unit deviation occurs when any material identity field changes:

```text
knowledge unit identifier
subject report
repository commit
declared use
scope
authority source
time window
```

A material change may require a new knowledge unit rather than continuation.

---

# 16. SCOPE CHANGE

A scope deviation occurs when proposed use expands beyond:

```text
one report
one repository state
one read-only review
one declared purpose
one declared temporal window
```

Related use is not automatically in scope.

---

# 17. AUTHORITY CHANGE

An authority deviation includes:

```text
authority expires
authority is revoked
authority source changes
actor exceeds declared role
review permission changes
```

Authority change does not alter historical evidence.

---

# 18. CONTEXT CHANGE

A context deviation includes any unplanned change beyond the controlled T2 event.

Examples:

```text
branch changes unexpectedly
runtime assumptions change
review purpose changes
required evidence changes
toolchain changes materially
```

---

# 19. RECORDING ERROR

A recording error includes:

```text
transcription mistake
wrong actor attribution
wrong event identifier
incorrect repository commit copied
raw output truncated accidentally
```

Corrections must be appended.

The original record remains visible.

---

# 20. SEVERITY STATES

Each deviation must be assigned one provisional severity:

```text
MINOR
MATERIAL
CRITICAL
UNKNOWN
```

Definitions:

```text
MINOR
does not affect event reconstruction or classification basis

MATERIAL
affects interpretation but may remain bounded

CRITICAL
invalidates a required condition or makes classification unreliable

UNKNOWN
effect cannot yet be determined
```

Severity is an observation, not a final disposition.

---

# 21. CLASSIFICATION IMPACT

Permitted classification-impact states:

```text
NONE OBSERVED
MAY FORCE PARTIAL
MAY FORCE FAIL
FORCES HOLD
UNKNOWN
```

No deviation may be classified as harmless without rationale.

---

# 22. CORRECTIVE ACTION

Corrective action must record:

```text
action proposed
actor
time
whether evidence changes
whether inputs change
whether criteria change
whether event must restart
```

Corrective action cannot erase the deviation.

---

# 23. REVIEW REQUIREMENT

Every MATERIAL, CRITICAL, or UNKNOWN deviation requires review.

Required reviewers:

```text
Research OS Operator
External Methodological Reviewer
Independent Outcome Reviewer
```

The framework owner participates when ESS or TTM interpretation is affected.

---

# 24. REVIEW STATUS

Permitted review statuses:

```text
NOT REVIEWED
UNDER REVIEW
DISPOSITION PROPOSED
RESOLVED
UNRESOLVED
```

`RESOLVED` means the effect has been dispositioned.

It does not mean the deviation ceased to exist.

---

# 25. FINAL DISPOSITION

Permitted final dispositions:

```text
NO MATERIAL EFFECT
PROCEED WITH LIMITATION
REPEAT EVENT
RESTART EXPERIMENT
CLASSIFY PARTIAL
CLASSIFY FAIL
HOLD
```

Only the independent review process may support final disposition.

---

# 26. DEVIATION RECORD TEMPLATE

```text
deviation_id:

observed_time:

reported_by:

reporter_role:

event_id:

affected_artifact:

deviation_type:

provisional_severity:

original_requirement:

observed_departure:

reason:

raw_evidence_reference:

known_effect:

unknown_effect:

classification_impact:

corrective_action:

review_required:

review_status:

final_disposition:
```

---

# 27. DEVIATION CORRECTION TEMPLATE

```text
correction_id:

original_deviation_id:

observed_time:

corrected_by:

incorrect_recorded_value:

corrected_value:

reason:

effect_on_interpretation:
```

The original deviation record remains preserved.

---

# 28. NO SILENT EXCEPTION

No deviation may be omitted because it is:

```text
inconvenient
small
successfully corrected
caused by the operator
caused by the framework owner
unlikely to affect the conclusion
```

Boundary:

```text
Corrected Deviation
≠
No Deviation Occurred
```

---

# 29. UNKNOWN EFFECT

When impact is uncertain:

```text
provisional_severity: UNKNOWN
classification_impact: FORCES HOLD
```

The deviation remains unresolved until reviewed.

---

# 30. PRE-EXECUTION REGISTER

Current deviation register:

```text
Recorded deviations: NONE
Deviation corrections: NONE
Unresolved deviations: NONE
Execution: HOLD
```

The earlier use of PowerShell syntax in Command Prompt occurred before experiment execution and before this instrument existed.

It is not an experiment deviation.

---

# 31. EXECUTION-START CONDITION

Execution remains HOLD until:

```text
PROTOCOL_DEVIATIONS.md is frozen
OBSERVATIONS.md is frozen
EXECUTION_RECORD.md is frozen
independent reviewer is assigned
```

---

# 32. REQUIRED FINAL REVIEW

Before Stage 0 classification, the independent reviewer must confirm:

```text
all deviations were visible
all critical deviations were dispositioned
no retry was hidden
no criteria were silently changed
no historical record was overwritten
```

---

# 33. LIMITATIONS

This record cannot establish:

```text
truth
causal independence
authority
admissibility
trust
production readiness
TTM validity
ESS validity
```

It records and bounds procedural departures only.

---

# 34. CURRENT STATUS

```text
Deviation instrument: DEFINED
Append-only posture: DEFINED
Deviation types: DEFINED
Severity states: DEFINED
Classification impact: DEFINED
Corrective-action semantics: DEFINED
Review requirement: DEFINED
Final disposition states: DEFINED
Execution: HOLD
UNKNOWN → HOLD
```

---

# 35. NEXT CHECKPOINT

After verification, freeze together:

```text
KNOWLEDGE_UNIT.md
EVENT_TIMELINE.md
EXECUTION_RECORD.md
OBSERVATIONS.md
PROTOCOL_DEVIATIONS.md
```

The independent reviewer remains required before execution may begin.
