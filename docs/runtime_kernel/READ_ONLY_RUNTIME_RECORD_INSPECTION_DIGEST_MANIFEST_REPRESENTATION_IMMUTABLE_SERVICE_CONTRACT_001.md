# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST REPRESENTATION

# IMMUTABLE SERVICE CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** IMMUTABLE SERVICE CONTRACT
**Status:** COMPLETE
**Operating Posture:** CONTRACT-FIRST / IMMUTABLE / DETERMINISTIC / IN-MEMORY / UNKNOWN → HOLD

---

# PURPOSE

Freeze the exact production location, service declaration, import boundary, accepted input type, method signature, output type, field order, value ownership, allocation semantics, deterministic behavior, error contract, prohibited dependencies, prohibited side effects, and test authorization for the first Read-Only Runtime Record Inspection Digest Manifest Representation capability.

This contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_EXISTING_REPRESENTATION_SERIALIZATION_PERSISTENCE_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

and:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_VOCABULARY_FIELD_ORDER_OWNERSHIP_AND_SCOPE_REDUCTION_001.md
```

Those documents established:

1. no manifest representation capability currently exists
2. the frozen manifest model must remain unchanged
3. the frozen inspection-report representation service must remain unchanged
4. a separate representation service is required
5. the service accepts only an exact manifest
6. the output is one new plain six-key primitive dictionary
7. field order is explicit and frozen
8. values are copied directly
9. automatic dataclass conversion is prohibited
10. serialization, encoding, hashing, verification, persistence, export, disclosure, and authority remain outside scope

This contract authorizes creation of a test contract.

Production implementation remains:

```text
HOLD
```

until tests exist, the expected missing-module failure is observed, and the test-first checkpoint is committed.

---

# CAPABILITY NAME

The frozen capability name is:

```text
Read-Only Runtime Record Inspection Digest Manifest Representation
```

---

# PRODUCTION LOCATION

The exact future production file is:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

No other production file may be created or modified for the first capability.

The frozen manifest model remains:

```text
models/runtime_record_inspection_digest_manifest.py
```

The frozen existing representation service remains:

```text
services/runtime_record_inspection_representation_service.py
```

Both must remain unchanged.

---

# SERVICE DECLARATION

The exact service declaration is:

```python
class RuntimeRecordInspectionDigestManifestRepresentationService:
```

The service requires no constructor arguments.

The service owns no mutable state.

No inheritance is required.

No protocol or abstract base class is required.

---

# REQUIRED IMPORT

The production service may import only:

```python
from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
```

No additional import is required for the minimum implementation.

---

# PROHIBITED IMPORTS

The production source must not import:

```text
json
pathlib
os
tempfile
hashlib
datetime
time
random
uuid
dataclasses
typing reflection helpers
runtime record registries
runtime record inspectors
event engines
serialization services
UTF-8 encoding services
digest services
manifest construction services
network libraries
database libraries
```

---

# METHOD DECLARATION

The exact public method declaration is:

```python
def to_primitive_dict(
    self,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> dict[str, object]:
```

The method is instance-owned.

No static method is required.

No class method is required.

No alternate public method is authorized.

---

# EXACT INPUT CONTRACT

The method accepts exactly:

```text
RuntimeRecordInspectionDigestManifest
```

The required validation is:

```python
if type(manifest) is not RuntimeRecordInspectionDigestManifest:
```

The exact exception type is:

```text
TypeError
```

The exact error message is:

```text
manifest must be an exact RuntimeRecordInspectionDigestManifest
```

The service must reject:

```text
None
bool
int
str
bytes
list
tuple
dict
RuntimeRecordInspectionReport
manifest subclasses
unrelated dataclasses
duck-typed objects
```

Validation must occur before any output allocation or field access.

---

# EXACT OUTPUT CONTRACT

For a valid manifest, the method returns exactly:

```python
dict[str, object]
```

The runtime output type must be exactly:

```python
dict
```

The output must not be:

```text
a dict subclass
a mapping proxy
a custom mapping
a dataclass
a tuple
a list
a JSON string
bytes
the original manifest
```

---

# EXACT KEY SET

The output must contain exactly six keys:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

No additional key is authorized.

No key may be omitted.

---

# EXACT INSERTION ORDER

The exact insertion order is:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

The service must declare this order explicitly in a dictionary literal.

The service must not derive order through:

```text
dataclasses.fields
dataclasses.asdict
vars
__dict__
reflection
sorting
schema discovery
iteration over model metadata
generic serializers
```

---

# EXACT VALUE MAPPING

The exact mapping is:

```python
{
    "manifest_schema_version": manifest.manifest_schema_version,
    "digest_algorithm": manifest.digest_algorithm,
    "sha256_digest": manifest.sha256_digest,
    "byte_length": manifest.byte_length,
    "codec": manifest.codec,
    "bom_present": manifest.bom_present,
}
```

No value transformation is authorized.

No value may be recalculated, reformatted, normalized, coerced, verified, or replaced.

---

# ALLOCATION CONTRACT

Each successful call must return a newly allocated dictionary.

For repeated calls using the same manifest:

```python
first == second
```

must be true.

```python
first is second
```

must be false.

The service must not cache returned dictionaries.

The service must not return a shared module-level object.

The service must not return internal mutable state.

---

# MUTATION ISOLATION

Mutation of a returned dictionary must not affect:

```text
the immutable manifest
another returned dictionary
a later returned dictionary
the service instance
another service instance
module state
global state
```

The service does not provide mutation methods.

The output dictionary remains caller-owned after return.

---

# DETERMINISM CONTRACT

For the same valid manifest, the service must return equal output regardless of:

```text
service instance
process clock
timezone
locale
filesystem state
environment variables
network state
registry state
platform
current directory
random state
```

The service must not generate current time.

The service must not generate random values.

The service must not generate identifiers.

---

# REPRESENTATION-ONLY CONTRACT

The service owns only:

```text
exact input acceptance
explicit six-field selection
explicit key insertion order
direct value copying
new dictionary allocation
deterministic return
```

The service does not own:

```text
manifest construction
manifest validation
digest generation
byte-length calculation
codec selection
BOM detection
JSON serialization
UTF-8 encoding
manifest hashing
digest verification
byte-length verification
source-byte inspection
source equality proof
authenticity verification
identity generation
timestamp generation
provenance binding
file naming
path generation
persistence
export
registry integration
publication
disclosure
trust evaluation
admission
authorization
execution
governance
orchestration
```

---

# SIDE-EFFECT CONTRACT

The method must create no files.

It must not read files.

It must not write files.

It must not create directories.

It must not modify registries.

It must not access network services.

It must not mutate the manifest.

It must not mutate service state.

It must not mutate global state.

The capability ends when the new dictionary is returned.

---

# SOURCE RESTRICTIONS

The production source must not contain:

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
import random
from random
import uuid
from uuid
dataclasses.asdict
dataclasses.fields
vars(
.__dict__
datetime.now
datetime.utcnow
time.time
open(
Path(
write_text
write_bytes
mkdir
```

The test contract may refine the exact executable source restrictions without widening capability scope.

---

# NO REVERSE CONVERSION

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

Dictionary-to-manifest construction remains outside scope.

---

# NO GENERIC REPRESENTATION

The service must not accept:

```text
object
dataclass instances generally
mapping-like values
arbitrary models
inspection reports
collections
```

The service is manifest-specific.

```text
Specific Representation Ownership
≠
Generic Serialization Framework
```

---

# NO SERIALIZATION

The service must not produce JSON or other text.

It must not choose:

```text
separators
key sorting
ASCII escaping
indentation
line endings
canonicalization
```

```text
Primitive Representation
≠
Serialization
```

---

# NO ENCODING

The service must not produce bytes.

It must not select:

```text
UTF-8
UTF-8-SIG
ASCII
binary framing
BOM behavior
```

```text
Primitive Dictionary
≠
Encoded Bytes
```

---

# NO HASHING OR VERIFICATION

The service must not calculate or compare:

```text
SHA-256 values
manifest hashes
dictionary hashes
source hashes
byte lengths
digest equality
source equality
```

```text
Representation
≠
Integrity Proof
```

---

# NO PERSISTENCE OR EXPORT

The service must not:

```text
save
load
persist
export
register
publish
write sidecars
create files
choose filenames
choose paths
choose content types
```

```text
Returned Dictionary
≠
Persisted Artifact
```

---

# NO AUTHORITY

The returned dictionary does not establish:

```text
trust
verification
admission
authorization
public disclosure
publication permission
execution permission
governance authority
```

```text
Machine-Readable
≠
Authorized For Use
```

---

# REQUIRED TEST SURFACE

The future test contract must cover at minimum:

1. service construction
2. independent service instances
3. exact method presence
4. prohibited alternate public methods
5. exact valid input acceptance
6. exact output type
7. exact key set
8. exact insertion order
9. exact direct value mapping
10. rejection of non-manifest values
11. rejection of manifest subclasses
12. exact exception type
13. exact error message
14. newly allocated result on each call
15. equal result for equal input
16. mutation isolation
17. deterministic behavior across service instances
18. no manifest mutation
19. no service state mutation
20. no file creation
21. no current-time generation
22. no prohibited imports
23. no `dataclasses.asdict`
24. no reflection-based expansion
25. no JSON serialization
26. no byte encoding
27. no hashing
28. no verification
29. no persistence
30. no export
31. no registry access
32. no frozen upstream modification

---

# AUTHORIZED TEST FILE

The exact future test file is:

```text
tests/runtime/test_runtime_record_inspection_digest_manifest_representation_service.py
```

No production implementation is authorized until:

1. the test contract document exists
2. the test file exists
3. the expected missing-module failure is observed
4. the test-first checkpoint is committed and pushed

---

# ACCEPTED MINIMUM IMPLEMENTATION SHAPE

The future minimum production behavior is reduced to:

```python
from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)


class RuntimeRecordInspectionDigestManifestRepresentationService:
    def to_primitive_dict(
        self,
        manifest: RuntimeRecordInspectionDigestManifest,
    ) -> dict[str, object]:
        if type(manifest) is not RuntimeRecordInspectionDigestManifest:
            raise TypeError(
                "manifest must be an exact "
                "RuntimeRecordInspectionDigestManifest"
            )

        return {
            "manifest_schema_version": manifest.manifest_schema_version,
            "digest_algorithm": manifest.digest_algorithm,
            "sha256_digest": manifest.sha256_digest,
            "byte_length": manifest.byte_length,
            "codec": manifest.codec,
            "bom_present": manifest.bom_present,
        }
```

This code is contractual reference only.

Production implementation remains:

```text
HOLD
```

---

# FROZEN OWNERSHIP MAP

```text
RuntimeRecordInspectionDigestManifest
→
owns immutable validated digest metadata
```

```text
RuntimeRecordInspectionDigestManifestService
→
owns validated caller-supplied fact binding
```

```text
RuntimeRecordInspectionDigestManifestRepresentationService
→
owns explicit manifest-to-primitive-dictionary transformation
```

No additional ownership is authorized.

---

# CONTRACT CONCLUSION

The immutable service contract is frozen as:

```text
exact RuntimeRecordInspectionDigestManifest
→
new plain six-key primitive dictionary
```

with:

```text
exact type boundary
explicit field selection
explicit insertion order
direct value copying
new allocation per call
deterministic behavior
no side effects
no serialization
no encoding
no hashing
no verification
no persistence
no authority
```

The next authorized artifact is:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_REPRESENTATION_TEST_CONTRACT_001.md
```

Tests are now authorized.

Production implementation remains:

```text
HOLD
```

---

# FINAL CONTRACT

```text
Manifest
≠
Manifest Representation
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
