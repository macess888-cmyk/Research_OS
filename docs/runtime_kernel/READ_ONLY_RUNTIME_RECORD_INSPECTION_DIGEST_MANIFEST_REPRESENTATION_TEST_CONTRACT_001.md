# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST REPRESENTATION

# TEST CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** TEST CONTRACT
**Status:** TESTS AUTHORIZED / IMPLEMENTATION HOLD
**Operating Posture:** TEST-FIRST / IMMUTABLE / DETERMINISTIC / IN-MEMORY / UNKNOWN → HOLD

---

# PURPOSE

Freeze the executable test contract for:

```text
RuntimeRecordInspectionDigestManifestRepresentationService
```

The capability performs exactly:

```text
one exact RuntimeRecordInspectionDigestManifest
→
one newly allocated plain six-key primitive dictionary
```

This test contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_EXISTING_REPRESENTATION_SERIALIZATION_PERSISTENCE_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_VOCABULARY_FIELD_ORDER_OWNERSHIP_AND_SCOPE_REDUCTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_IMMUTABLE_SERVICE_CONTRACT_001.md
```

Production implementation remains:

```text
HOLD
```

until:

1. this test contract exists
2. the authorized test module exists
3. the expected missing-module failure is observed
4. the test-first checkpoint is committed and pushed

---

# AUTHORIZED TEST FILE

The exact authorized test location is:

```text
tests/runtime/test_runtime_record_inspection_digest_manifest_representation_service.py
```

No other test file is required for the first capability.

---

# FUTURE PRODUCTION FILE

The exact future production location is:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

This file must not exist when the test-first failure is first observed.

---

# FROZEN UPSTREAM FILES

The following upstream files must remain unchanged:

```text
models/runtime_record_inspection_digest_manifest.py
services/runtime_record_inspection_digest_manifest_service.py
services/runtime_record_inspection_representation_service.py
```

The first representation capability requires no modification to any frozen upstream model or service.

---

# REQUIRED TEST IMPORTS

The test module may import:

```python
from dataclasses import dataclass
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from services.runtime_record_inspection_digest_manifest_representation_service import (
    RuntimeRecordInspectionDigestManifestRepresentationService,
)
```

Additional standard-library imports may be used only when required for source inspection or immutable-state comparison.

---

# TEST FIXTURES

The test module should provide a valid manifest fixture or helper with values equivalent to:

```python
RuntimeRecordInspectionDigestManifest(
    manifest_schema_version="1.0",
    digest_algorithm="sha256",
    sha256_digest="a" * 64,
    byte_length=128,
    codec="utf-8",
    bom_present=False,
)
```

The exact valid digest character may differ, provided the value remains a valid 64-character lowercase hexadecimal string.

A service fixture may return:

```python
RuntimeRecordInspectionDigestManifestRepresentationService()
```

---

# REQUIRED SERVICE CONSTRUCTION TESTS

The test module must prove:

1. the service class can be instantiated
2. the runtime type is exactly `RuntimeRecordInspectionDigestManifestRepresentationService`
3. separate constructor calls produce separate service instances
4. the service constructor requires no arguments
5. service construction creates no files
6. service construction does not generate time, identifiers, or external state

Expected relation:

```text
first service is not second service
```

---

# REQUIRED PUBLIC SURFACE TESTS

The service must expose exactly one required public capability:

```text
to_primitive_dict
```

The test module must verify that the service does not expose unauthorized public conversion or side-effect methods including:

```text
from_primitive_dict
from_dict
to_manifest
build_manifest
create_manifest
to_json
to_json_text
to_bytes
serialize
encode
hash
digest
verify
save
load
persist
export
write
read
register
publish
inspect
health
status
```

Dunder methods inherited from Python object semantics are outside this surface restriction.

---

# REQUIRED VALID INPUT TEST

A valid exact manifest must be accepted.

The returned value must be produced without modifying the manifest.

The test must verify:

```python
result = service.to_primitive_dict(manifest)
```

completes successfully.

---

# REQUIRED EXACT INPUT TYPE TESTS

The service must reject every input whose exact runtime type is not:

```text
RuntimeRecordInspectionDigestManifest
```

The invalid-input test surface must include at minimum:

```text
None
True
False
0
1
"manifest"
b"manifest"
[]
()
{}
object()
```

It must also reject:

```text
RuntimeRecordInspectionReport
a manifest subclass
an unrelated dataclass
a duck-typed object with matching attributes
```

---

# MANIFEST SUBCLASS REJECTION

The test module must define a valid subclass boundary, for example:

```python
@dataclass(frozen=True)
class DerivedManifest(RuntimeRecordInspectionDigestManifest):
    pass
```

An instance of the subclass must be rejected even when all inherited field values are valid.

Required reduction:

```text
Subclass Compatibility
≠
Exact Type Acceptance
```

---

# DUCK-TYPED OBJECT REJECTION

The test module must prove that matching attributes are insufficient.

An unrelated object containing:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

must still be rejected.

Required reduction:

```text
Compatible Shape
≠
Accepted Manifest
```

---

# EXACT ERROR CONTRACT

For every invalid input, the service must raise exactly:

```text
TypeError
```

The exact error message must be:

```text
manifest must be an exact RuntimeRecordInspectionDigestManifest
```

The test must use an exact or fully anchored message match.

No partial alternative wording is authorized.

---

# VALIDATION ORDER

Input type validation must occur before:

```text
field access
dictionary construction
value copying
serialization
encoding
hashing
file access
external-state access
```

A duck-typed object whose attributes raise exceptions when accessed may be used to prove that rejected inputs are not inspected beyond the exact type check.

---

# REQUIRED OUTPUT TYPE TESTS

For valid input, the returned runtime type must be exactly:

```text
dict
```

The result must not be:

```text
a dict subclass
a mapping proxy
a custom mapping
a dataclass
a tuple
a list
a string
bytes
the original manifest
```

Required assertion:

```python
assert type(result) is dict
```

---

# REQUIRED EXACT KEY SET TEST

The result must contain exactly:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

No extra key is permitted.

No required key may be absent.

The exact key count must be:

```text
6
```

---

# REQUIRED INSERTION ORDER TEST

The exact key order must be:

```python
[
    "manifest_schema_version",
    "digest_algorithm",
    "sha256_digest",
    "byte_length",
    "codec",
    "bom_present",
]
```

The test must inspect:

```python
list(result.keys())
```

Field order is contractual and must not be inferred indirectly.

---

# REQUIRED DIRECT VALUE MAPPING TESTS

The output must map values exactly as follows:

```python
result["manifest_schema_version"] == manifest.manifest_schema_version
result["digest_algorithm"] == manifest.digest_algorithm
result["sha256_digest"] == manifest.sha256_digest
result["byte_length"] == manifest.byte_length
result["codec"] == manifest.codec
result["bom_present"] == manifest.bom_present
```

The runtime value types must remain:

```text
str
str
str
int
str
bool
```

No coercion or normalization is allowed.

---

# DISTINCT-VALUE TEST

The test module should use at least one valid manifest whose values make accidental substitution visible.

At minimum:

```text
sha256_digest
byte_length
```

must use values that cannot be confused with defaults, empty values, or each other.

The test must prove that every output field comes from its corresponding manifest field.

---

# REQUIRED NEW ALLOCATION TEST

Repeated calls using the same manifest must produce equal but distinct dictionaries.

Required assertions:

```python
first == second
first is not second
```

The service must not cache or reuse output objects.

---

# REQUIRED MUTATION ISOLATION TEST

After obtaining two results:

```python
first = service.to_primitive_dict(manifest)
second = service.to_primitive_dict(manifest)
```

mutating `first` must not affect:

```text
second
the manifest
a later third result
```

The test should modify one or more dictionary values and then verify isolation.

Required reduction:

```text
Equal Representation
≠
Shared Mutable Identity
```

---

# REQUIRED MANIFEST IMMUTABILITY TEST

The test must capture all six manifest fields before representation and compare them afterward.

Calling the service must not alter:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

The manifest remains frozen and unchanged.

---

# REQUIRED SERVICE STATE TEST

The service must own no mutable instance state.

The test should verify either:

```python
service.__dict__ == {}
```

or an equivalent exact state assertion.

Calling `to_primitive_dict` must not add state to the service.

---

# REQUIRED CROSS-INSTANCE DETERMINISM TEST

Two independent service instances receiving the same manifest must return equal dictionaries.

Required relation:

```text
same manifest
+
different service instances
→
equal output
```

Service instance identity must not influence representation.

---

# REQUIRED REPEATED-CALL DETERMINISM TEST

Multiple calls using the same service and same manifest must return equal results.

The test must prove that result content does not depend on:

```text
call count
prior result mutation
service history
process time
```

---

# REQUIRED CURRENT-TIME ABSENCE TEST

Production source must not contain:

```text
datetime.now
datetime.utcnow
time.time
```

The test may inspect the production source text after implementation.

The service must not generate timestamps.

---

# REQUIRED RANDOMNESS AND IDENTITY ABSENCE TEST

Production source must not contain or import:

```text
random
uuid
secrets
```

The service must not generate identifiers or random values.

---

# REQUIRED SOURCE IMPORT RESTRICTION TEST

The production source must not contain prohibited imports or dependency fragments including:

```text
import json
from json
import pathlib
from pathlib
import os
from os
import tempfile
from tempfile
import hashlib
from hashlib
import datetime
from datetime
import time
from time
import random
from random
import uuid
from uuid
import dataclasses
from dataclasses
runtime_record_registry
runtime_record_inspector
event_engine
runtime_record_inspection_json_encoding_service
runtime_record_inspection_utf8_byte_encoding_service
runtime_record_inspection_sha256_digest_service
runtime_record_inspection_digest_manifest_service
```

The only required production import is the frozen manifest model.

---

# REQUIRED AUTOMATIC-CONVERSION ABSENCE TEST

Production source must not contain:

```text
dataclasses.asdict
asdict(
dataclasses.fields
fields(
vars(
.__dict__
getattr(
```

This restriction applies to representation extraction behavior.

An exact reference to `service.__dict__` in tests does not authorize production use of `.__dict__`.

---

# REQUIRED JSON ABSENCE TEST

Production source must not:

```text
import JSON libraries
call json.dumps
call json.dump
produce JSON strings
```

The returned result must remain a plain dictionary.

Required reduction:

```text
Primitive Representation
≠
JSON Serialization
```

---

# REQUIRED BYTE-ENCODING ABSENCE TEST

Production source must not contain byte-encoding behavior including:

```text
.encode(
bytes(
bytearray(
memoryview(
utf-8-sig
```

The service must not produce bytes or select a codec.

---

# REQUIRED HASHING ABSENCE TEST

Production source must not import or use:

```text
hashlib
sha256(
hexdigest(
digest(
```

The service must copy the existing digest string without recalculating it.

---

# REQUIRED VERIFICATION ABSENCE TEST

Production source must not include behavior that:

```text
recomputes digest values
compares source bytes
calculates byte length
compares byte length
verifies codec
verifies BOM presence
verifies authenticity
verifies evidence
```

The method name and production source must not imply verification ownership.

---

# REQUIRED FILESYSTEM ABSENCE TEST

Calling the service must create no files or directories.

The test should:

1. change into an empty temporary directory
2. capture directory contents
3. call `to_primitive_dict`
4. capture directory contents again
5. assert equality

Production source must not contain:

```text
open(
Path(
write_text
write_bytes
mkdir
touch(
unlink(
rename(
replace(
```

---

# REQUIRED NETWORK ABSENCE TEST

Production source must not import or reference common network clients or protocols.

At minimum, prohibit:

```text
requests
urllib
http.client
socket
aiohttp
```

No network interaction is authorized.

---

# REQUIRED REGISTRY ABSENCE TEST

Production source must not reference:

```text
runtime_record_registry
manifest_registry
artifact_registry
platform_registry
```

Representation must not register output.

---

# REQUIRED PERSISTENCE AND EXPORT ABSENCE TEST

The service must expose no methods and contain no source behavior for:

```text
save
load
persist
export
publish
write
read
register
```

The capability ends at dictionary return.

---

# REQUIRED REVERSE-CONVERSION ABSENCE TEST

The service must not expose:

```text
from_primitive_dict
from_dict
to_manifest
build_manifest
create_manifest
parse
deserialize
load
```

Primitive dictionary input is outside scope.

---

# REQUIRED GENERIC-REPRESENTATION ABSENCE TEST

The method annotation and runtime checks must remain manifest-specific.

The service must not accept generic:

```text
object
dataclass
mapping
dictionary
iterable
protocol
```

The production source must not introduce a generic representation framework.

---

# REQUIRED FROZEN-UPSTREAM INTEGRITY TESTS

The test module should inspect frozen upstream source files and verify that the new representation capability did not add representation behavior to the manifest model.

At minimum, the manifest model must still not expose:

```text
to_dict
to_primitive
to_json
to_json_text
to_bytes
serialize
encode
save
persist
export
```

The existing inspection-report representation service must remain manifest-unaware.

Its production source must not reference:

```text
RuntimeRecordInspectionDigestManifest
runtime_record_inspection_digest_manifest
```

---

# REQUIRED PRODUCTION-FILE EXISTENCE TEST

After implementation, the authorized production file must exist exactly at:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

No alternate duplicate production location is authorized.

Before implementation, importing the service must fail with the expected missing-module error.

---

# EXPECTED TEST-FIRST FAILURE

After the test module is created and before production implementation exists, running:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest_representation_service.py -q
```

must fail during test collection with an error equivalent to:

```text
ModuleNotFoundError:
No module named 'services.runtime_record_inspection_digest_manifest_representation_service'
```

This failure is required evidence that tests precede implementation.

---

# TEST-FIRST CHECKPOINT CONTENT

The test-first commit must contain only:

```text
docs/runtime_kernel/READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_TEST_CONTRACT_001.md
tests/runtime/test_runtime_record_inspection_digest_manifest_representation_service.py
```

It must not contain:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

Production implementation remains:

```text
HOLD
```

until the test-first commit is complete and synchronized.

---

# EXPECTED IMPLEMENTATION VALIDATION

After the minimum production service is added, run:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest_representation_service.py -q
```

All isolated tests must pass.

Then run:

```powershell
python -m pytest -q
```

The full suite must pass.

No existing test may be weakened, removed, skipped, or rewritten to accommodate implementation.

---

# PROHIBITED TEST SHORTCUTS

The tests must not:

```text
mock the production service
define the production class inside the test module
skip missing-module failure
accept subclasses
accept partial error messages when exact wording is required
test only dictionary equality without testing key order
omit mutation isolation
omit source restrictions
omit side-effect restrictions
modify frozen upstream code
create production code before the test-first checkpoint
```

---

# AUTHORIZED IMPLEMENTATION AFTER CHECKPOINT

Only after the test-first checkpoint is committed and pushed may the following production file be created:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

The implementation must be the smallest code satisfying the frozen contract and executable tests.

No additional capability is authorized.

---

# TEST CONTRACT CONCLUSION

The executable test surface is frozen around:

```text
exact manifest input
exact type rejection
exact error contract
plain dictionary output
exact six-key set
exact key order
direct value mapping
new allocation per call
mutation isolation
manifest immutability
stateless service
determinism
no serialization
no encoding
no hashing
no verification
no filesystem effects
no persistence
no export
no registry access
no authority expansion
frozen upstream preservation
```

The next authorized action is:

```text
create the test module
observe the expected missing-module failure
commit and push the test-first checkpoint
```

Production implementation remains:

```text
HOLD
```

---

# FINAL TEST BOUNDARIES

```text
Tests
≠
Implementation
```

```text
Representation
≠
Serialization
```

```text
Representation
≠
Verification
```

```text
Equal Output
≠
Shared Mutable Identity
```

```text
Machine-Readable
≠
Authorized For Use
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
