# READ-ONLY RUNTIME RECORD INSPECTION ARTIFACT REGISTRY — SERVICE CONTRACT 001

**Project:** Research OS
**Subsystem:** Runtime Kernel
**Capability Area:** Read-Only Runtime Record Inspection Artifact Registry
**Artifact Type:** Service Contract
**Date:** 2026-07-19
**Status:** SERVICE CONTRACT DRAFT
**Operating Posture:** TYPE-FIRST / COLLISION-EXPLICIT / MONOTONIC / IN-MEMORY / NON-PERSISTING / NON-ADMITTING / UNKNOWN → HOLD

---

# 1. PURPOSE

This document freezes the service contract for:

```text
RuntimeRecordInspectionArtifactRegistry
```

The registry provides narrow in-memory registration and lookup behavior for:

```text
RuntimeRecordInspectionReportArtifact
RuntimeRecordInspectionDigestManifestArtifact
```

The registry classifies each valid registration attempt as:

```text
REGISTERED
ALREADY_REGISTERED
IDENTITY_COLLISION
```

through:

```text
RuntimeRecordInspectionArtifactRegistrationResult
```

The service provides:

```text
typed registration
registry-local uniqueness evaluation
equal re-registration classification
identity-collision classification
exact-object retention
typed lookup
observational counts
monotonic in-memory membership
```

The service does not provide:

```text
identifier allocation
global uniqueness
overwrite
removal
update
enumeration
serialization
persistence
registration receipts
registration chronology
provenance
custody
lineage
report–manifest association
admission
trust
authority
```

This document freezes the service contract only.

It does not authorize tests or implementation.

---

# 2. SERVICE NAME

The exact service name is:

```text
RuntimeRecordInspectionArtifactRegistry
```

Rejected alternatives include:

```text
ArtifactRegistry
RuntimeArtifactRegistry
RuntimeRecordArtifactRegistry
InspectionArtifactRegistry
RuntimeRecordInspectionArtifactStore
PersistentArtifactRegistry
```

The selected name preserves:

```text
runtime-record scope
inspection scope
artifact-wrapper scope
registry behavior
```

---

# 3. MODULE NAME

The exact module path is:

```text
services/runtime_record_inspection_artifact_registry.py
```

The module must contain:

```text
RuntimeRecordInspectionArtifactRegistry
```

as its single primary production service.

The module must not define:

```text
artifact wrapper models
registration-result model
identifier allocator
persistent store
receipt model
association model
custom exception hierarchy
```

---

# 4. REQUIRED IMPORTS

The module may import:

```python
import re

from models.runtime_record_inspection_artifact_registration_result import (
    RuntimeRecordInspectionArtifactRegistrationResult,
)
from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
)
```

No other production dependency is required.

The module must not import:

```text
datetime
json
hashlib
pathlib
uuid
os
sys
database libraries
application frameworks
persistence services
admission services
authority services
```

---

# 5. PRIVATE IDENTIFIER PATTERNS

The module must define:

```python
_REPORT_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIRA-[0-9]{9}$"
)

_MANIFEST_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIDMA-[0-9]{9}$"
)
```

These constants support raw lookup validation.

They must remain private.

They must not allocate identifiers.

---

# 6. CLASS DECLARATION

The exact declaration is:

```python
class RuntimeRecordInspectionArtifactRegistry:
```

The registry is not a dataclass.

Reason:

```text
registry
=
stateful service with mutable internal collections
```

Boundary:

```text
Mutable Registry Service
≠
Immutable Artifact Model
```

No inheritance hierarchy is authorized.

---

# 7. CONSTRUCTOR CONTRACT

The constructor must require no arguments:

```python
def __init__(self) -> None:
```

A new instance creates two empty dictionaries:

```python
self._report_artifacts_by_id = {}
self._manifest_artifacts_by_id = {}
```

Equivalent typed declarations are permitted.

The constructor must not accept:

```text
initial artifacts
filesystem paths
database connections
registry identifiers
clock services
allocators
configuration objects
```

---

# 8. EMPTY INITIALIZATION

Immediately after construction:

```text
report_count = 0
manifest_count = 0
total_count = 0
```

The internal dictionaries must be distinct objects.

No global or shared registry state is authorized.

---

# 9. INSTANCE-LOCAL STATE

Each registry instance owns its own state.

Required invariant:

```text
registry_a registrations
do not affect
registry_b
```

Two instances may independently register the same typed identifier with different artifact values.

Boundary:

```text
Registry-Instance Consistency
≠
System-Wide Consistency
```

---

# 10. PROCESS-LOCAL STATE

Registry state exists only during the current Python process lifetime.

A new process or newly constructed registry begins empty.

The service must not claim:

```text
restart reconstruction
durable membership
historical continuity
cross-process uniqueness
```

---

# 11. INTERNAL REPORT STORAGE

The exact private attribute name is:

```text
_report_artifacts_by_id
```

Candidate type:

```python
dict[
    str,
    RuntimeRecordInspectionReportArtifact,
]
```

Key:

```text
report_artifact.report_artifact_id
```

Value:

```text
exact submitted report artifact object
```

---

# 12. INTERNAL MANIFEST STORAGE

The exact private attribute name is:

```text
_manifest_artifacts_by_id
```

Candidate type:

```python
dict[
    str,
    RuntimeRecordInspectionDigestManifestArtifact,
]
```

Key:

```text
manifest_artifact.manifest_artifact_id
```

Value:

```text
exact submitted manifest artifact object
```

---

# 13. SEPARATE STORAGE CONTRACT

Report and manifest artifacts must remain in separate dictionaries.

A unified map is not authorized.

The following typed identifiers may coexist:

```text
RIRA-000000001
RIDMA-000000001
```

Boundary:

```text
Matching Numeric Suffix
≠
Registry Collision
```

---

# 14. PUBLIC REGISTRATION METHODS

The exact public registration methods are:

```text
register_report_artifact
register_manifest_artifact
```

No generic:

```text
register
```

method is authorized.

---

# 15. REPORT REGISTRATION SIGNATURE

The exact signature is:

```python
def register_report_artifact(
    self,
    artifact: RuntimeRecordInspectionReportArtifact,
) -> RuntimeRecordInspectionArtifactRegistrationResult:
```

The method accepts exactly one report artifact wrapper.

---

# 16. MANIFEST REGISTRATION SIGNATURE

The exact signature is:

```python
def register_manifest_artifact(
    self,
    artifact: RuntimeRecordInspectionDigestManifestArtifact,
) -> RuntimeRecordInspectionArtifactRegistrationResult:
```

The method accepts exactly one digest-manifest artifact wrapper.

---

# 17. REPORT REGISTRATION TYPE VALIDATION

The report registration method must validate using:

```python
isinstance(
    artifact,
    RuntimeRecordInspectionReportArtifact,
)
```

Invalid input raises:

```text
TypeError
```

Exact message:

```text
artifact must be a RuntimeRecordInspectionReportArtifact
```

No coercion or conversion is permitted.

---

# 18. MANIFEST REGISTRATION TYPE VALIDATION

The manifest registration method must validate using:

```python
isinstance(
    artifact,
    RuntimeRecordInspectionDigestManifestArtifact,
)
```

Invalid input raises:

```text
TypeError
```

Exact message:

```text
artifact must be a RuntimeRecordInspectionDigestManifestArtifact
```

---

# 19. TYPE-FAILURE ATOMICITY

When registration receives an invalid type:

```text
raise TypeError
registry state unchanged
counts unchanged
no result returned
```

The method must not inspect fields on an invalid object before type validation succeeds.

---

# 20. REPORT REGISTRATION IDENTIFIER

The report registration key is:

```text
artifact.report_artifact_id
```

The service must not use:

```text
artifact.report.record_id
artifact.report.append_position
artifact.report.external_id
artifact.report.provenance_ref
report content
Python hash
```

as the key.

---

# 21. MANIFEST REGISTRATION IDENTIFIER

The manifest registration key is:

```text
artifact.manifest_artifact_id
```

The service must not use:

```text
artifact.manifest.sha256_digest
artifact.manifest.byte_length
artifact.manifest.manifest_schema_version
manifest content
Python hash
```

as the key.

---

# 22. REPORT REGISTRATION SEQUENCE

The exact report registration sequence is:

```text
1. validate artifact type
2. derive report_artifact_id
3. inspect _report_artifacts_by_id
4. if absent:
      retain candidate
      return REGISTERED
5. if existing == candidate:
      return ALREADY_REGISTERED
6. otherwise:
      return IDENTITY_COLLISION
```

The sequence must remain deterministic.

---

# 23. MANIFEST REGISTRATION SEQUENCE

The exact manifest registration sequence is:

```text
1. validate artifact type
2. derive manifest_artifact_id
3. inspect _manifest_artifacts_by_id
4. if absent:
      retain candidate
      return REGISTERED
5. if existing == candidate:
      return ALREADY_REGISTERED
6. otherwise:
      return IDENTITY_COLLISION
```

---

# 24. NEW REPORT REGISTRATION

Condition:

```text
report_artifact_id not present
```

Required behavior:

```text
store exact candidate object
report count increases by one
manifest count unchanged
total count increases by one
return REGISTERED result
```

Result fields:

```text
artifact_kind = REPORT
artifact_id = candidate.report_artifact_id
status = REGISTERED
existing_artifact = None
candidate_artifact = candidate
```

---

# 25. NEW MANIFEST REGISTRATION

Condition:

```text
manifest_artifact_id not present
```

Required behavior:

```text
store exact candidate object
manifest count increases by one
report count unchanged
total count increases by one
return REGISTERED result
```

Result fields:

```text
artifact_kind = DIGEST_MANIFEST
artifact_id = candidate.manifest_artifact_id
status = REGISTERED
existing_artifact = None
candidate_artifact = candidate
```

---

# 26. EXACT-OBJECT RETENTION

For successful new registration:

```python
registry.get_report_artifact(
    artifact.report_artifact_id
) is artifact
```

or:

```python
registry.get_manifest_artifact(
    artifact.manifest_artifact_id
) is artifact
```

The service must not:

```text
copy
deep-copy
reconstruct
serialize and deserialize
normalize
replace
```

the artifact.

---

# 27. EQUAL REPORT RE-REGISTRATION

Condition:

```text
same report_artifact_id
existing artifact == candidate artifact
```

Required behavior:

```text
do not mutate dictionary
do not replace stored object
counts unchanged
return ALREADY_REGISTERED result
```

Result fields:

```text
artifact_kind = REPORT
artifact_id = candidate.report_artifact_id
status = ALREADY_REGISTERED
existing_artifact = original stored artifact
candidate_artifact = submitted candidate
```

---

# 28. EQUAL MANIFEST RE-REGISTRATION

Condition:

```text
same manifest_artifact_id
existing artifact == candidate artifact
```

Required behavior:

```text
do not mutate dictionary
do not replace stored object
counts unchanged
return ALREADY_REGISTERED result
```

Result fields:

```text
artifact_kind = DIGEST_MANIFEST
artifact_id = candidate.manifest_artifact_id
status = ALREADY_REGISTERED
existing_artifact = original stored artifact
candidate_artifact = submitted candidate
```

---

# 29. STRUCTURAL EQUALITY OWNERSHIP

Equal re-registration classification must use:

```python
existing == artifact
```

It must not depend on:

```text
existing is artifact
hash(existing) == hash(artifact)
retained report equality only
retained manifest equality only
content digest equality
```

Boundary:

```text
Structural Wrapper Equality
≠
Python Object Identity
```

---

# 30. ORIGINAL OBJECT PRESERVATION

For equal re-registration:

```text
existing object remains stored
candidate object is not substituted
```

Required invariant:

```text
lookup returns original object
```

even when:

```text
existing == candidate
existing is not candidate
```

---

# 31. REPORT IDENTITY COLLISION

Condition:

```text
same report_artifact_id
existing artifact != candidate artifact
```

Required behavior:

```text
registry unchanged
report count unchanged
original stored artifact preserved
candidate not stored
return IDENTITY_COLLISION result
```

Result fields:

```text
artifact_kind = REPORT
artifact_id = candidate.report_artifact_id
status = IDENTITY_COLLISION
existing_artifact = original stored artifact
candidate_artifact = submitted candidate
```

---

# 32. MANIFEST IDENTITY COLLISION

Condition:

```text
same manifest_artifact_id
existing artifact != candidate artifact
```

Required behavior:

```text
registry unchanged
manifest count unchanged
original stored artifact preserved
candidate not stored
return IDENTITY_COLLISION result
```

Result fields:

```text
artifact_kind = DIGEST_MANIFEST
artifact_id = candidate.manifest_artifact_id
status = IDENTITY_COLLISION
existing_artifact = original stored artifact
candidate_artifact = submitted candidate
```

---

# 33. COLLISION NON-MUTATION

On identity collision, the service must not:

```text
overwrite
replace
merge
append a second value under the same key
alter the existing wrapper
retain the candidate in another hidden collection
```

Boundary:

```text
Collision Classified
≠
Collision Candidate Registered
```

---

# 34. CONTENT REPETITION

Different artifact identifiers may contain equal retained values.

Examples:

```text
RIRA-000000001 + report A
RIRA-000000002 + report A
```

and:

```text
RIDMA-000000001 + manifest A
RIDMA-000000002 + manifest A
```

Both registrations must succeed.

The registry does not deduplicate by content.

---

# 35. NO CROSS-TYPE COLLISION

A report artifact and manifest artifact with matching numeric suffixes do not collide.

Example:

```text
RIRA-000000001
RIDMA-000000001
```

Expected:

```text
both REGISTERED
total count = 2
```

---

# 36. REGISTRATION RESULT CONSTRUCTION

Each valid registration attempt must return a new:

```text
RuntimeRecordInspectionArtifactRegistrationResult
```

The service must construct results only after classification is known.

The service must not mutate result objects after construction.

---

# 37. RESULT PROPERTY EXPECTATIONS

For `REGISTERED`:

```text
registry_changed = True
registration_accepted = True
collision_detected = False
```

For `ALREADY_REGISTERED`:

```text
registry_changed = False
registration_accepted = True
collision_detected = False
```

For `IDENTITY_COLLISION`:

```text
registry_changed = False
registration_accepted = False
collision_detected = True
```

The service does not independently supply these properties.

---

# 38. PUBLIC LOOKUP METHODS

The exact public lookup methods are:

```text
get_report_artifact
get_manifest_artifact
```

No generic lookup method is authorized.

---

# 39. REPORT LOOKUP SIGNATURE

The exact signature is:

```python
def get_report_artifact(
    self,
    report_artifact_id: str,
) -> RuntimeRecordInspectionReportArtifact:
```

---

# 40. MANIFEST LOOKUP SIGNATURE

The exact signature is:

```python
def get_manifest_artifact(
    self,
    manifest_artifact_id: str,
) -> RuntimeRecordInspectionDigestManifestArtifact:
```

---

# 41. REPORT LOOKUP VALIDATION ORDER

The exact report lookup validation sequence is:

```text
1. report_artifact_id type
2. report_artifact_id syntax
3. positive numeric component
4. dictionary lookup
```

---

# 42. MANIFEST LOOKUP VALIDATION ORDER

The exact manifest lookup validation sequence is:

```text
1. manifest_artifact_id type
2. manifest_artifact_id syntax
3. positive numeric component
4. dictionary lookup
```

---

# 43. REPORT LOOKUP TYPE CONTRACT

`report_artifact_id` must be a string.

Invalid type raises:

```text
TypeError
```

Exact message:

```text
report_artifact_id must be a string
```

Validation must use:

```python
isinstance(report_artifact_id, str)
```

---

# 44. MANIFEST LOOKUP TYPE CONTRACT

`manifest_artifact_id` must be a string.

Invalid type raises:

```text
TypeError
```

Exact message:

```text
manifest_artifact_id must be a string
```

---

# 45. REPORT LOOKUP SYNTAX CONTRACT

The identifier must match:

```regex
^RIRA-[0-9]{9}$
```

Invalid syntax raises:

```text
ValueError
```

Exact message:

```text
report_artifact_id must match RIRA-#########
```

No normalization is permitted.

---

# 46. MANIFEST LOOKUP SYNTAX CONTRACT

The identifier must match:

```regex
^RIDMA-[0-9]{9}$
```

Invalid syntax raises:

```text
ValueError
```

Exact message:

```text
manifest_artifact_id must match RIDMA-#########
```

---

# 47. REPORT LOOKUP ZERO CONTRACT

The identifier:

```text
RIRA-000000000
```

must raise:

```text
ValueError
```

Exact message:

```text
report_artifact_id numeric component must be greater than zero
```

---

# 48. MANIFEST LOOKUP ZERO CONTRACT

The identifier:

```text
RIDMA-000000000
```

must raise:

```text
ValueError
```

Exact message:

```text
manifest_artifact_id numeric component must be greater than zero
```

---

# 49. LOOKUP PRESERVATION

When an identifier is present, lookup must return the exact stored wrapper object.

Required invariants:

```python
registry.get_report_artifact(identifier) is stored_report_artifact
```

```python
registry.get_manifest_artifact(identifier) is stored_manifest_artifact
```

---

# 50. LOOKUP ABSENCE

When a valid identifier is absent, lookup must raise:

```text
KeyError
```

The `KeyError` argument must be the supplied identifier.

Candidate behavior:

```python
raise KeyError(report_artifact_id)
```

or natural dictionary indexing behavior.

---

# 51. WRONG-NAMESPACE LOOKUP

Examples:

```text
RIDMA-000000001 passed to get_report_artifact
RIRA-000000001 passed to get_manifest_artifact
```

Expected:

```text
ValueError
```

The failure occurs during syntax validation before dictionary lookup.

---

# 52. LOOKUP NON-MUTATION

All lookup operations are read-only.

Lookup must not:

```text
insert
remove
replace
reorder
create result objects
change counts
emit output
```

---

# 53. COUNT PROPERTIES

The exact public read-only properties are:

```text
report_count
manifest_count
total_count
```

They must use `@property`.

They must not be assignable through service methods.

---

# 54. REPORT COUNT CONTRACT

Exact property:

```python
@property
def report_count(self) -> int:
```

Candidate implementation:

```python
return len(self._report_artifacts_by_id)
```

---

# 55. MANIFEST COUNT CONTRACT

Exact property:

```python
@property
def manifest_count(self) -> int:
```

Candidate implementation:

```python
return len(self._manifest_artifacts_by_id)
```

---

# 56. TOTAL COUNT CONTRACT

Exact property:

```python
@property
def total_count(self) -> int:
```

Candidate implementation:

```python
return self.report_count + self.manifest_count
```

No separate total counter is authorized.

---

# 57. COUNT SEMANTICS

Counts represent:

```text
current registry-instance membership
```

They do not represent:

```text
historical registration attempts
total registration results
persistent artifact totals
cross-process totals
```

Equal re-registration and collision do not change counts.

---

# 58. MONOTONIC MEMBERSHIP

During one registry instance lifetime:

```text
counts may increase
counts never decrease
stored values never change
stored values never disappear
```

The service exposes no method capable of reducing membership.

Boundary:

```text
Monotonic Membership
≠
Durable Append-Only History
```

---

# 59. NO REMOVAL API

The class must not define:

```text
remove
delete
clear
reset
remove_report_artifact
remove_manifest_artifact
```

---

# 60. NO UPDATE API

The class must not define:

```text
update
replace
overwrite
upsert
merge
update_report_artifact
update_manifest_artifact
```

---

# 61. NO ENUMERATION API

The class must not define:

```text
list_report_artifacts
list_manifest_artifacts
list_artifacts
all_artifacts
iter_artifacts
history
timeline
```

Enumeration and ordering remain outside scope.

---

# 62. NO CONTAINS API

The class must not define:

```text
contains_report_artifact
contains_manifest_artifact
contains
```

Lookup and `KeyError` remain the selected public behavior.

---

# 63. NO GENERIC REGISTRATION API

The class must not define:

```text
register
```

Only the two explicit typed registration methods are authorized.

---

# 64. NO GENERIC LOOKUP API

The class must not define:

```text
get_artifact
lookup
find
```

Only typed lookup methods are authorized.

---

# 65. NO ALLOCATION API

The class must not define:

```text
allocate_id
generate_id
next_id
next_report_artifact_id
next_manifest_artifact_id
```

The registry accepts already-constructed wrappers only.

---

# 66. NO REGISTRATION TIME

The service must not use a clock.

It must not record:

```text
registered_at
attempted_at
completed_at
```

No import from `datetime` is authorized.

---

# 67. NO REGISTRATION POSITION

The service must not allocate:

```text
append_position
sequence_number
registration_index
```

Dictionary insertion order is not a domain contract.

---

# 68. NO REGISTRY IDENTITY

The service contains no:

```text
registry_id
registry_instance_id
registry_version
```

A future persistent or receipt layer may require these.

---

# 69. NO SERIALIZATION

The class must not define:

```text
to_dict
to_json
to_bytes
serialize
deserialize
snapshot
restore
save
load
```

The registry stores Python objects directly.

---

# 70. NO FILESYSTEM ACCESS

The service must not use:

```text
pathlib
open
pickle
shelve
sqlite
filesystem reads
filesystem writes
```

No registry state survives process termination.

---

# 71. NO DATABASE ACCESS

The service must not connect to:

```text
SQLite
PostgreSQL
MySQL
Redis
document stores
external databases
```

Persistence remains NONE.

---

# 72. NO RECEIPT CREATION

The service returns an immutable result.

It does not create:

```text
receipt
receipt identifier
signature
registration digest
persistent event
```

Boundary:

```text
Registration Result
≠
Registration Receipt
```

---

# 73. NO PROVENANCE CLAIM

Registration does not establish:

```text
who created the artifact
who submitted the artifact
where the artifact came from
which method generated it
which environment produced it
```

---

# 74. NO CUSTODY CLAIM

In-memory retention does not establish:

```text
custodian
storage location
continuous possession
transfer history
tamper-free custody
```

---

# 75. NO LINEAGE CLAIM

The registry must not infer lineage from:

```text
adjacent identifiers
equal retained content
different artifact IDs
registration order
```

---

# 76. NO REPORT–MANIFEST ASSOCIATION

Registering a report artifact and manifest artifact in the same registry does not associate them.

The service contains no:

```text
associate
bind
link
pair
attach
```

method.

Boundary:

```text
Registry Co-Membership
≠
Artifact Association
```

---

# 77. NO HISTORICAL BINDING

The registry cannot establish:

```text
creation-time pairing
historical co-presence
replacement absence
custody continuity
external anchoring
```

Current membership is not historical evidence.

---

# 78. NO ADMISSION

A `REGISTERED` or `ALREADY_REGISTERED` result does not mean:

```text
admitted
approved
eligible
trusted
authentic
verified
```

---

# 79. NO AUTHORITY

The service must not:

```text
authorize execution
release HOLD
modify runtime records
publish artifacts
trigger workflows
admit evidence
grant permissions
```

Boundary:

```text
Registry Classification
≠
Authority
```

---

# 80. FRAMEWORK INDEPENDENCE

The module must not import:

```text
Streamlit
Flask
Django
FastAPI
Tkinter
PyQt
Pandas
NumPy
SQLAlchemy
```

The registry remains Runtime Kernel local.

---

# 81. OUTPUT SILENCE

Construction, registration, lookup, and count access must not print to:

```text
stdout
stderr
```

No logging dependency is authorized.

Boundary:

```text
Registry Operation
≠
Publication
```

---

# 82. EXCEPTION POSTURE

The service uses:

```text
TypeError
ValueError
KeyError
```

No custom exception is authorized.

Collision is represented by a result, not an exception.

---

# 83. FAILURE ATOMICITY

The following must leave state unchanged:

```text
wrong registration type
invalid lookup type
invalid lookup syntax
zero lookup identifier
missing lookup identifier
equal re-registration
identity collision
```

Only `REGISTERED` changes state.

---

# 84. NO PARTIAL REGISTRATION

The service must not insert a candidate before classification is complete.

Required ordering:

```text
inspect state
classify
insert only when absent
construct result
```

No failed result may leave a partial entry.

---

# 85. CONCURRENCY EXCLUSION

The service provides no guarantee of:

```text
thread safety
process safety
distributed consistency
atomicity across concurrent callers
locking
compare-and-set
```

The first foundation is single-process and ordinary synchronous use only.

---

# 86. DICTIONARY EXPOSURE

The private dictionaries must not be exposed directly through public properties.

The service must not return:

```text
internal dictionary
mutable mapping view
dictionary keys view
dictionary values view
```

No external caller may directly mutate registry state.

---

# 87. PRIVATE ATTRIBUTE POSTURE

The exact private attributes are:

```text
_report_artifacts_by_id
_manifest_artifacts_by_id
```

No additional mutable collection is required.

The service must not store:

```text
registration results
collision history
attempt history
sequence history
rejected candidates
```

---

# 88. RESULT RETENTION EXCLUSION

The registry returns registration results but does not retain them.

Boundary:

```text
Result Returned
≠
Result Registered
```

---

# 89. CANDIDATE RETENTION RULE

Candidate retention mapping:

```text
REGISTERED
→ candidate retained

ALREADY_REGISTERED
→ candidate not retained

IDENTITY_COLLISION
→ candidate not retained
```

The candidate remains referenced by the returned result, but not by registry storage.

---

# 90. EXISTING ARTIFACT RESULT RULE

Existing artifact mapping:

```text
REGISTERED
→ None

ALREADY_REGISTERED
→ original stored artifact

IDENTITY_COLLISION
→ original stored artifact
```

---

# 91. REPORT REGISTRATION CANDIDATE IMPLEMENTATION

Candidate:

```python
def register_report_artifact(
    self,
    artifact: RuntimeRecordInspectionReportArtifact,
) -> RuntimeRecordInspectionArtifactRegistrationResult:
    if not isinstance(
        artifact,
        RuntimeRecordInspectionReportArtifact,
    ):
        raise TypeError(
            "artifact must be a "
            "RuntimeRecordInspectionReportArtifact"
        )

    artifact_id = artifact.report_artifact_id
    existing = self._report_artifacts_by_id.get(
        artifact_id
    )

    if existing is None:
        self._report_artifacts_by_id[
            artifact_id
        ] = artifact

        return (
            RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="REPORT",
                artifact_id=artifact_id,
                status="REGISTERED",
                existing_artifact=None,
                candidate_artifact=artifact,
            )
        )

    if existing == artifact:
        return (
            RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="REPORT",
                artifact_id=artifact_id,
                status="ALREADY_REGISTERED",
                existing_artifact=existing,
                candidate_artifact=artifact,
            )
        )

    return RuntimeRecordInspectionArtifactRegistrationResult(
        artifact_kind="REPORT",
        artifact_id=artifact_id,
        status="IDENTITY_COLLISION",
        existing_artifact=existing,
        candidate_artifact=artifact,
    )
```

---

# 92. MANIFEST REGISTRATION CANDIDATE IMPLEMENTATION

Candidate:

```python
def register_manifest_artifact(
    self,
    artifact: RuntimeRecordInspectionDigestManifestArtifact,
) -> RuntimeRecordInspectionArtifactRegistrationResult:
    if not isinstance(
        artifact,
        RuntimeRecordInspectionDigestManifestArtifact,
    ):
        raise TypeError(
            "artifact must be a "
            "RuntimeRecordInspectionDigestManifestArtifact"
        )

    artifact_id = artifact.manifest_artifact_id
    existing = self._manifest_artifacts_by_id.get(
        artifact_id
    )

    if existing is None:
        self._manifest_artifacts_by_id[
            artifact_id
        ] = artifact

        return (
            RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="DIGEST_MANIFEST",
                artifact_id=artifact_id,
                status="REGISTERED",
                existing_artifact=None,
                candidate_artifact=artifact,
            )
        )

    if existing == artifact:
        return (
            RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="DIGEST_MANIFEST",
                artifact_id=artifact_id,
                status="ALREADY_REGISTERED",
                existing_artifact=existing,
                candidate_artifact=artifact,
            )
        )

    return RuntimeRecordInspectionArtifactRegistrationResult(
        artifact_kind="DIGEST_MANIFEST",
        artifact_id=artifact_id,
        status="IDENTITY_COLLISION",
        existing_artifact=existing,
        candidate_artifact=artifact,
    )
```

---

# 93. REPORT LOOKUP VALIDATION METHOD

The selected private method is:

```text
_validate_report_artifact_id
```

Candidate:

```python
def _validate_report_artifact_id(
    self,
    report_artifact_id: str,
) -> None:
    if not isinstance(report_artifact_id, str):
        raise TypeError(
            "report_artifact_id must be a string"
        )

    if not _REPORT_ARTIFACT_ID_PATTERN.fullmatch(
        report_artifact_id
    ):
        raise ValueError(
            "report_artifact_id must match RIRA-#########"
        )

    if int(report_artifact_id[5:]) <= 0:
        raise ValueError(
            "report_artifact_id numeric component must be "
            "greater than zero"
        )
```

---

# 94. MANIFEST LOOKUP VALIDATION METHOD

The selected private method is:

```text
_validate_manifest_artifact_id
```

Candidate:

```python
def _validate_manifest_artifact_id(
    self,
    manifest_artifact_id: str,
) -> None:
    if not isinstance(manifest_artifact_id, str):
        raise TypeError(
            "manifest_artifact_id must be a string"
        )

    if not _MANIFEST_ARTIFACT_ID_PATTERN.fullmatch(
        manifest_artifact_id
    ):
        raise ValueError(
            "manifest_artifact_id must match "
            "RIDMA-#########"
        )

    if int(manifest_artifact_id[6:]) <= 0:
        raise ValueError(
            "manifest_artifact_id numeric component must "
            "be greater than zero"
        )
```

---

# 95. REPORT LOOKUP CANDIDATE IMPLEMENTATION

Candidate:

```python
def get_report_artifact(
    self,
    report_artifact_id: str,
) -> RuntimeRecordInspectionReportArtifact:
    self._validate_report_artifact_id(
        report_artifact_id
    )

    return self._report_artifacts_by_id[
        report_artifact_id
    ]
```

---

# 96. MANIFEST LOOKUP CANDIDATE IMPLEMENTATION

Candidate:

```python
def get_manifest_artifact(
    self,
    manifest_artifact_id: str,
) -> RuntimeRecordInspectionDigestManifestArtifact:
    self._validate_manifest_artifact_id(
        manifest_artifact_id
    )

    return self._manifest_artifacts_by_id[
        manifest_artifact_id
    ]
```

---

# 97. COUNT CANDIDATE IMPLEMENTATION

Candidate:

```python
@property
def report_count(self) -> int:
    return len(self._report_artifacts_by_id)

@property
def manifest_count(self) -> int:
    return len(self._manifest_artifacts_by_id)

@property
def total_count(self) -> int:
    return self.report_count + self.manifest_count
```

---

# 98. COMPLETE CANDIDATE SERVICE

The complete candidate service is:

```python
import re

from models.runtime_record_inspection_artifact_registration_result import (
    RuntimeRecordInspectionArtifactRegistrationResult,
)
from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
)


_REPORT_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIRA-[0-9]{9}$"
)

_MANIFEST_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIDMA-[0-9]{9}$"
)


class RuntimeRecordInspectionArtifactRegistry:
    """
    Monotonic in-memory registry for typed runtime-record inspection
    artifacts.

    The service evaluates registry-local uniqueness, equal
    re-registration, and identity collision. It does not allocate,
    persist, receipt, admit, trust, authorize, or trigger side effects.
    """

    def __init__(self) -> None:
        self._report_artifacts_by_id: dict[
            str,
            RuntimeRecordInspectionReportArtifact,
        ] = {}

        self._manifest_artifacts_by_id: dict[
            str,
            RuntimeRecordInspectionDigestManifestArtifact,
        ] = {}

    def register_report_artifact(
        self,
        artifact: RuntimeRecordInspectionReportArtifact,
    ) -> RuntimeRecordInspectionArtifactRegistrationResult:
        if not isinstance(
            artifact,
            RuntimeRecordInspectionReportArtifact,
        ):
            raise TypeError(
                "artifact must be a "
                "RuntimeRecordInspectionReportArtifact"
            )

        artifact_id = artifact.report_artifact_id
        existing = self._report_artifacts_by_id.get(
            artifact_id
        )

        if existing is None:
            self._report_artifacts_by_id[
                artifact_id
            ] = artifact

            return (
                RuntimeRecordInspectionArtifactRegistrationResult(
                    artifact_kind="REPORT",
                    artifact_id=artifact_id,
                    status="REGISTERED",
                    existing_artifact=None,
                    candidate_artifact=artifact,
                )
            )

        if existing == artifact:
            return (
                RuntimeRecordInspectionArtifactRegistrationResult(
                    artifact_kind="REPORT",
                    artifact_id=artifact_id,
                    status="ALREADY_REGISTERED",
                    existing_artifact=existing,
                    candidate_artifact=artifact,
                )
            )

        return RuntimeRecordInspectionArtifactRegistrationResult(
            artifact_kind="REPORT",
            artifact_id=artifact_id,
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=artifact,
        )

    def register_manifest_artifact(
        self,
        artifact: RuntimeRecordInspectionDigestManifestArtifact,
    ) -> RuntimeRecordInspectionArtifactRegistrationResult:
        if not isinstance(
            artifact,
            RuntimeRecordInspectionDigestManifestArtifact,
        ):
            raise TypeError(
                "artifact must be a "
                "RuntimeRecordInspectionDigestManifestArtifact"
            )

        artifact_id = artifact.manifest_artifact_id
        existing = self._manifest_artifacts_by_id.get(
            artifact_id
        )

        if existing is None:
            self._manifest_artifacts_by_id[
                artifact_id
            ] = artifact

            return (
                RuntimeRecordInspectionArtifactRegistrationResult(
                    artifact_kind="DIGEST_MANIFEST",
                    artifact_id=artifact_id,
                    status="REGISTERED",
                    existing_artifact=None,
                    candidate_artifact=artifact,
                )
            )

        if existing == artifact:
            return (
                RuntimeRecordInspectionArtifactRegistrationResult(
                    artifact_kind="DIGEST_MANIFEST",
                    artifact_id=artifact_id,
                    status="ALREADY_REGISTERED",
                    existing_artifact=existing,
                    candidate_artifact=artifact,
                )
            )

        return RuntimeRecordInspectionArtifactRegistrationResult(
            artifact_kind="DIGEST_MANIFEST",
            artifact_id=artifact_id,
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=artifact,
        )

    def get_report_artifact(
        self,
        report_artifact_id: str,
    ) -> RuntimeRecordInspectionReportArtifact:
        self._validate_report_artifact_id(
            report_artifact_id
        )

        return self._report_artifacts_by_id[
            report_artifact_id
        ]

    def get_manifest_artifact(
        self,
        manifest_artifact_id: str,
    ) -> RuntimeRecordInspectionDigestManifestArtifact:
        self._validate_manifest_artifact_id(
            manifest_artifact_id
        )

        return self._manifest_artifacts_by_id[
            manifest_artifact_id
        ]

    @property
    def report_count(self) -> int:
        return len(
            self._report_artifacts_by_id
        )

    @property
    def manifest_count(self) -> int:
        return len(
            self._manifest_artifacts_by_id
        )

    @property
    def total_count(self) -> int:
        return (
            self.report_count
            + self.manifest_count
        )

    def _validate_report_artifact_id(
        self,
        report_artifact_id: str,
    ) -> None:
        if not isinstance(
            report_artifact_id,
            str,
        ):
            raise TypeError(
                "report_artifact_id must be a string"
            )

        if not _REPORT_ARTIFACT_ID_PATTERN.fullmatch(
            report_artifact_id
        ):
            raise ValueError(
                "report_artifact_id must match "
                "RIRA-#########"
            )

        if int(report_artifact_id[5:]) <= 0:
            raise ValueError(
                "report_artifact_id numeric component "
                "must be greater than zero"
            )

    def _validate_manifest_artifact_id(
        self,
        manifest_artifact_id: str,
    ) -> None:
        if not isinstance(
            manifest_artifact_id,
            str,
        ):
            raise TypeError(
                "manifest_artifact_id must be a string"
            )

        if not _MANIFEST_ARTIFACT_ID_PATTERN.fullmatch(
            manifest_artifact_id
        ):
            raise ValueError(
                "manifest_artifact_id must match "
                "RIDMA-#########"
            )

        if int(manifest_artifact_id[6:]) <= 0:
            raise ValueError(
                "manifest_artifact_id numeric component "
                "must be greater than zero"
            )
```

This candidate is frozen by contract but not yet authorized for implementation.

---

# 99. DOCSTRING CONTRACT

The class docstring must communicate:

```text
monotonic in-memory registry
typed artifact scope
registry-local uniqueness
equal re-registration
identity collision
non-allocation
non-persistence
non-admission
non-authority
```

Exact prose may vary only if all boundaries remain explicit.

---

# 100. REPORT NEW-REGISTRATION PRESSURE TEST

Input:

```text
empty registry
report artifact A
```

Expected:

```text
status = REGISTERED
report_count = 1
manifest_count = 0
total_count = 1
lookup is artifact A
```

---

# 101. MANIFEST NEW-REGISTRATION PRESSURE TEST

Input:

```text
empty registry
manifest artifact A
```

Expected:

```text
status = REGISTERED
report_count = 0
manifest_count = 1
total_count = 1
lookup is artifact A
```

---

# 102. REPORT EQUAL RE-REGISTRATION PRESSURE TEST

Input:

```text
stored artifact A
equal separate candidate A2
same RIRA identifier
```

Expected:

```text
status = ALREADY_REGISTERED
counts unchanged
lookup is original A
result.existing_artifact is A
result.candidate_artifact is A2
```

---

# 103. MANIFEST EQUAL RE-REGISTRATION PRESSURE TEST

Input:

```text
stored manifest artifact A
equal separate candidate A2
same RIDMA identifier
```

Expected:

```text
status = ALREADY_REGISTERED
counts unchanged
lookup is original A
```

---

# 104. REPORT COLLISION PRESSURE TEST

Input:

```text
stored report artifact A
unequal candidate B
same RIRA identifier
```

Expected:

```text
status = IDENTITY_COLLISION
counts unchanged
lookup is original A
candidate B not stored
```

---

# 105. MANIFEST COLLISION PRESSURE TEST

Input:

```text
stored manifest artifact A
unequal candidate B
same RIDMA identifier
```

Expected:

```text
status = IDENTITY_COLLISION
counts unchanged
lookup is original A
candidate B not stored
```

---

# 106. CONTENT REPETITION PRESSURE TEST

Input:

```text
different identifiers
equal retained subject values
```

Expected:

```text
both REGISTERED
count increases twice
```

---

# 107. CROSS-NAMESPACE PRESSURE TEST

Input:

```text
RIRA-000000001
RIDMA-000000001
```

Expected:

```text
both REGISTERED
no collision
total_count = 2
```

---

# 108. WRONG REPORT TYPE PRESSURE TEST

Input:

```text
manifest artifact passed to register_report_artifact
```

Expected:

```text
TypeError
registry unchanged
```

---

# 109. WRONG MANIFEST TYPE PRESSURE TEST

Input:

```text
report artifact passed to register_manifest_artifact
```

Expected:

```text
TypeError
registry unchanged
```

---

# 110. VALID MISSING LOOKUP PRESSURE TEST

Input:

```text
valid absent RIRA or RIDMA identifier
```

Expected:

```text
KeyError
registry unchanged
```

---

# 111. INVALID LOOKUP TYPE PRESSURE TEST

Input:

```text
None
integer
bytes
collection
```

Expected:

```text
TypeError
registry unchanged
```

---

# 112. INVALID LOOKUP SYNTAX PRESSURE TEST

Input:

```text
wrong prefix
wrong digit count
wrong case
whitespace
non-digit suffix
```

Expected:

```text
ValueError
registry unchanged
```

---

# 113. ZERO LOOKUP PRESSURE TEST

Input:

```text
RIRA-000000000
RIDMA-000000000
```

Expected:

```text
ValueError
registry unchanged
```

---

# 114. MULTIPLE INSTANCE PRESSURE TEST

Input:

```text
registry A registers ID with value A
registry B registers same ID with value B
```

Expected:

```text
both REGISTERED independently
```

No cross-instance collision detection exists.

---

# 115. RESTART PRESSURE TEST

Input:

```text
populate registry
construct new registry
```

Expected:

```text
new registry empty
```

---

# 116. NO-OVERWRITE PRESSURE TEST

After collision:

```text
lookup returns original object
```

This must remain true after repeated collision attempts.

---

# 117. MONOTONIC COUNT PRESSURE TEST

Across valid operations:

```text
REGISTERED
→ count increases

ALREADY_REGISTERED
→ count unchanged

IDENTITY_COLLISION
→ count unchanged

lookup
→ count unchanged
```

Counts never decrease.

---

# 118. NO SIDE-EFFECT PRESSURE TEST

Registry operations must not:

```text
create files
modify environment variables
connect to external systems
print output
modify runtime records
modify retained reports
modify retained manifests
```

---

# 119. TEST CONTRACT REQUIREMENTS

A future registry test contract must verify:

```text
module import
class import
constructor shape
empty initialization
private storage separation
new report registration
new manifest registration
result fields
result derived properties
exact-object retention
equal re-registration
identity collision
content repetition
cross-namespace coexistence
wrong-type failures
typed lookup
lookup validation order
missing lookup
count properties
monotonic membership
no overwrite
no removal API
no update API
no generic APIs
no enumeration
no allocation
no serialization
no persistence
no output
framework independence
process-local scope
authority exclusion
```

---

# 120. IMPLEMENTATION BOUNDARY

This contract does not authorize creation of:

```text
services/runtime_record_inspection_artifact_registry.py
```

Implementation remains HOLD until:

```text
result model contract frozen
registry service contract frozen
result test contract frozen
registry test contract frozen
tests written first
expected missing-module failures observed
```

---

# 121. NEXT AUTHORIZED DOCUMENTS

The next authorized documents are:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_ARTIFACT_REGISTRATION_RESULT_TEST_CONTRACT_001.md
```

and:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_ARTIFACT_REGISTRY_TEST_CONTRACT_001.md
```

The result test contract should be frozen first.

---

# 122. CONTRACT DECISION

The registry service is:

```text
RuntimeRecordInspectionArtifactRegistry
```

with:

```text
two separate typed dictionaries
two explicit registration methods
two explicit lookup methods
three observational count properties
monotonic instance-local membership
result-based collision classification
```

It remains non-persisting and non-authorizing.

---

# 123. FINAL STATUS

```text
Service name: FROZEN
Module name: FROZEN
Constructor: FROZEN

Report storage attribute: FROZEN
Manifest storage attribute: FROZEN
Separate-map design: FROZEN

Report registration method: FROZEN
Manifest registration method: FROZEN
Generic registration method: NONE

Report type validation: FROZEN
Manifest type validation: FROZEN

New registration behavior: FROZEN
Equal re-registration behavior: FROZEN
Identity-collision behavior: FROZEN
Structural classification: FROZEN
Original-object retention: FROZEN
Candidate retention mapping: FROZEN
Overwrite: REJECTED

Report lookup method: FROZEN
Manifest lookup method: FROZEN
Generic lookup: NONE
Lookup type validation: FROZEN
Lookup syntax validation: FROZEN
Lookup zero validation: FROZEN
Lookup absence: KeyError

Report count: FROZEN
Manifest count: FROZEN
Total count: FROZEN
Monotonic membership: FROZEN

Removal: NONE
Update: NONE
Enumeration: NONE
Contains methods: NONE
Allocation: NONE
Registration time: NONE
Registration position: NONE
Registry identity: NONE
Result retention: NONE
Receipt: NONE
Serialization: NONE
Persistence: NONE
Concurrency guarantees: NONE

Provenance: NONE
Custody: NONE
Lineage: NONE
Association: NONE
Historical binding: NONE
Admission: NONE
Trust: NONE
Authority: NONE

Result test contract: AUTHORIZED
Registry test contract: AUTHORIZED AFTER RESULT TEST CONTRACT
Implementation: HOLD
```

```text
UNKNOWN → HOLD
```

```text
No proof → No bind → No side effect.
```
