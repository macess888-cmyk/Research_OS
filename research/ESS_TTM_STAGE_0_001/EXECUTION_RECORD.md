# ESS–TTM STAGE 0 — EXECUTION RECORD 001

**Experiment Identifier:** ESS-TTM-STAGE-0-001
**Knowledge Unit:** ESS-TTM-KU-001
**Date:** 2026-07-18
**Status:** EXECUTION RECORD TEMPLATE
**Operating Posture:** APPEND-ONLY / RAW-OUTPUT-PRESERVING / NO-HIDDEN-RETRY / UNKNOWN → HOLD

---

# 1. PURPOSE

This document provides the append-only execution record for the ESS–TTM Stage 0 Pilot Calibration.

It records the commands, actors, times, repository states, inputs, outputs, failures, retries, unknowns, and protocol deviations associated with events T0 through T6.

This document is a recording instrument.

It is not an interpretation, approval, or validation result.

---

# 2. RECORDING RULE

Once execution begins:

```text
existing execution entries must not be rewritten
```

Corrections must be appended as new entries referencing the original entry.

Boundary:

```text
Correction
≠
Historical Replacement
```

---

# 3. EXECUTION STATUS

Current status:

```text
Execution: HOLD
Reason:
- independent outcome reviewer unassigned
- observation template not yet frozen
- protocol deviation template not yet frozen
```

No event record may be marked executed until all execution-start conditions are satisfied.

---

# 4. REQUIRED ENTRY FIELDS

Every execution entry must include:

```text
entry_id
event_id
entry_type
observed_time
actor
role
working_directory
repository_branch
repository_head
working_tree_status
command_or_action
declared_inputs
raw_output
declared_outputs
unknowns
failures
retry_reference
protocol_deviation_reference
entry_status
```

---

# 5. ENTRY IDENTIFIER FORMAT

Canonical format:

```text
EXEC-T0-001
EXEC-T1-001
EXEC-T2-001
EXEC-T3-001
EXEC-T4-001
EXEC-T5-001
EXEC-T6-001
```

Retries or supplemental records use increasing suffixes:

```text
EXEC-T1-002
EXEC-T1-003
```

The identifier does not imply success.

---

# 6. ENTRY TYPES

Permitted entry types:

```text
EVENT_START
COMMAND
OBSERVATION
FAILURE
RETRY_PROPOSAL
RETRY_EXECUTION
CORRECTION
EVENT_END
```

No other entry type may be introduced after execution begins without a protocol deviation.

---

# 7. TIME RECORDING

`observed_time` records the local time visible to the operator.

Recommended format:

```text
YYYY-MM-DDTHH:MM:SS±HH:MM
```

The observed time does not establish:

```text
trusted time
independent timestamp authority
causal ordering beyond the recorded procedure
```

---

# 8. ACTOR AND ROLE

Every entry must identify both:

```text
actor
role
```

Candidate roles:

```text
ESS Framework Owner
Research OS Operator
External Methodological Reviewer
Independent Outcome Reviewer
```

An actor may hold more than one declared role, but the active role for each entry must be explicit.

---

# 9. REPOSITORY STATE

Before each event action, record:

```text
git branch --show-current
git rev-parse HEAD
git status --porcelain=v1 --branch
```

The raw outputs must be preserved.

Do not convert the repository state into only:

```text
clean
dirty
```

when the underlying Git output is available.

---

# 10. COMMAND RECORDING

Commands must be recorded exactly as entered.

Example:

```text
Command:
git rev-parse HEAD
```

Do not rewrite commands into cleaner or more successful forms after execution.

---

# 11. RAW OUTPUT RECORDING

Raw output must be copied without semantic correction.

If the command returns no visible output, record:

```text
<NO VISIBLE OUTPUT>
```

If the command is not run, record:

```text
<NOT EXECUTED>
```

Do not infer output from expectations.

---

# 12. DECLARED INPUTS

Each entry must identify the artifacts or states intentionally supplied to the action.

Examples:

```text
ESS-TTM-KU-001
subject inspection report
digest manifest
repository HEAD
authority declaration
review scope
```

Inputs not explicitly supplied must not be assumed.

---

# 13. DECLARED OUTPUTS

Each entry must identify artifacts actually created or observed.

Examples:

```text
report representation
digest verification result
repository commit observation
review record
```

Expected outputs that were not produced must remain absent.

---

# 14. UNKNOWN RECORDING

Every entry must include an `unknowns` field.

When none are observed, record:

```text
None observed within the bounded procedure.
```

This means only that no unknown was recorded within that event.

It does not mean no unknown exists.

---

# 15. FAILURE RECORDING

A failure entry must include:

```text
failed action
raw failure output
observed time
known input state
known repository state
immediate effect
whether evidence was altered
whether retry is proposed
```

A failed command must not be silently repeated.

---

# 16. RETRY PROPOSAL

Before any retry, append a `RETRY_PROPOSAL` entry containing:

```text
original entry identifier
reason for retry
whether command changes
whether inputs change
whether repository state changes
expected effect on interpretation
review requirement
```

Retry execution remains HOLD until the proposal is recorded.

---

# 17. RETRY EXECUTION

A retry execution must receive its own entry identifier.

It must not replace the original attempt.

Boundary:

```text
Successful Retry
≠
Original Attempt Never Failed
```

---

# 18. CORRECTION ENTRY

If an earlier record contains a transcription or attribution error, append:

```text
entry_type: CORRECTION
original_entry_id
incorrect_recorded_value
corrected_value
reason
actor
observed_time
```

The original entry remains preserved.

---

# 19. PROTOCOL DEVIATION REFERENCE

Every entry must include:

```text
protocol_deviation_reference
```

Permitted values:

```text
NONE
DEV-001
DEV-002
...
```

If it is unclear whether a deviation occurred:

```text
UNKNOWN — REVIEW REQUIRED
```

---

# 20. ENTRY STATUS

Permitted entry statuses:

```text
RECORDED
FAILED
RETRY PROPOSED
RETRIED
PARTIAL
HOLD
```

`RECORDED` does not mean successful or admissible.

It means the entry was preserved.

---

# 21. EVENT START RECORD

Each event begins with an `EVENT_START` entry.

Required content:

```text
event purpose
authorized actor
planned action
expected inputs
repository state
known unknowns
deviation status
```

---

# 22. EVENT END RECORD

Each event ends with an `EVENT_END` entry.

Required content:

```text
entries completed
outputs actually produced
failures
retries
unknowns
deviations
event status
next authorized event
```

An event cannot end as PASS.

Permitted event statuses:

```text
RECORDED
PARTIAL
FAILED
HOLD
```

---

# 23. T0 RECORD SECTION

## T0 — Knowledge Unit Creation

```text
Event status: NOT STARTED
```

### Entry Template

```text
entry_id:
event_id: T0
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 24. T1 RECORD SECTION

## T1 — Structural Verification

```text
Event status: NOT STARTED
```

### Entry Template

```text
entry_id:
event_id: T1
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 25. T2 RECORD SECTION

## T2 — Controlled Condition Change

```text
Event status: NOT STARTED
```

### Entry Template

```text
entry_id:
event_id: T2
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 26. T3 RECORD SECTION

## T3 — Proposed Execution-Time Use

```text
Event status: NOT STARTED
```

### Entry Template

```text
entry_id:
event_id: T3
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 27. T4 RECORD SECTION

## T4 — Current-Standing Review

```text
Event status: NOT STARTED
```

T4 interpretation belongs in the observation artifact.

The execution record preserves only the review procedure, supplied evidence, commands, and outputs.

### Entry Template

```text
entry_id:
event_id: T4
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 28. T5 RECORD SECTION

## T5 — Revalidation Attempt

```text
Event status: NOT STARTED
```

### Entry Template

```text
entry_id:
event_id: T5
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 29. T6 RECORD SECTION

## T6 — Final Calibration Observation

```text
Event status: NOT STARTED
```

T6 classification belongs in `STAGE_0_CALIBRATION_RESULT.md`.

The execution record preserves the procedure and evidence used to reach it.

### Entry Template

```text
entry_id:
event_id: T6
entry_type:
observed_time:
actor:
role:
working_directory:
repository_branch:
repository_head:
working_tree_status:

command_or_action:

declared_inputs:

raw_output:

declared_outputs:

unknowns:

failures:

retry_reference:

protocol_deviation_reference:

entry_status:
```

---

# 30. EXECUTION RECORD LIMITATIONS

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

It establishes only that specified actions and observations were recorded.

---

# 31. PROHIBITED RECORDING BEHAVIOUR

The operator must not:

```text
summarize raw output in place of preserving it
delete failed attempts
reuse entry identifiers
overwrite earlier entries
hide retries
hide protocol deviations
convert assumptions into observations
mark an event PASS
```

---

# 32. EXECUTION START CHECKLIST

Before T0 begins, confirm:

```text
PROTOCOL.md frozen
ROLE_DECLARATIONS.md frozen
PREDEFINED_CRITERIA.md frozen
KNOWLEDGE_UNIT.md frozen
EVENT_TIMELINE.md frozen
EXECUTION_RECORD.md frozen
OBSERVATIONS.md frozen
PROTOCOL_DEVIATIONS.md frozen
independent reviewer assigned
repository working tree clean
```

Any unsatisfied condition means:

```text
Execution: HOLD
```

---

# 33. CURRENT RECORD STATE

```text
T0 entries: NONE
T1 entries: NONE
T2 entries: NONE
T3 entries: NONE
T4 entries: NONE
T5 entries: NONE
T6 entries: NONE
Failures: NONE RECORDED
Retries: NONE RECORDED
Protocol deviations: NONE RECORDED
Execution: HOLD
```

---

# 34. NEXT AUTHORIZED ARTIFACT

```text
OBSERVATIONS.md
```

That document must define the independent observation format for:

```text
evidence
authority
context
scope
sufficiency
supporting evidence
unknowns
reviewer attribution
```

---

# 35. FINAL STATUS

```text
Execution-record structure: DEFINED
Append-only posture: DEFINED
Raw-output preservation: REQUIRED
Failure recording: REQUIRED
Retry visibility: REQUIRED
Correction semantics: DEFINED
Repository-state recording: REQUIRED
T0–T6 templates: DEFINED
Execution: HOLD
UNKNOWN → HOLD
```
