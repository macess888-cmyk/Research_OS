# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST JSON ENCODING

# TEST CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** TEST CONTRACT
**Status:** TESTS AUTHORIZED / IMPLEMENTATION HOLD
**Operating Posture:** TEST-FIRST / DETERMINISTIC / IN-MEMORY / UNKNOWN → HOLD

---

# PURPOSE

Freeze the executable test contract for:

```text
RuntimeRecordInspectionDigestManifestJsonEncodingService
```

The capability performs exactly:

```text
one exact digest-manifest primitive dictionary
→
one deterministic compact JSON string
```

This test contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_JSON_ENCODING_EXISTING_ENCODER_REUSE_FORMATTING_BYTE_PERSISTENCE_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_JSON_ENCODING_VOCABULARY_INPUT_OWNERSHIP_FORMATTING_AND_SCOPE_REDUCTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_JSON_ENCODING_IMMUTABLE_SERVICE_CONTRACT_001.md
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
tests/runtime/test_runtime_record_inspection_digest_manifest_json_encoding_service.py
```

No other test file is required for the first capability.

---

# FUTURE PRODUCTION FILE

The exact future production location is:

```text
services/runtime_record_inspection_digest_manifest_json_encoding_service.py
```

This file must not exist when the expected test-first failure is first observed.

---

# FROZEN UPSTREAM FILES

The following files must remain unchanged:

```text
models/runtime_record_inspection_digest_manifest.py
services/runtime_record_inspection_digest_manifest_service.py
services/runtime_record_inspection_digest_manifest_representation_service.py
services/runtime_record_inspection_json_encoding_service.py
```

The first digest-manifest JSON encoding capability requires no modification to any frozen upstream component.

---

# REQUIRED TEST IMPORTS

The test module may import:

```python
import json
from collections import OrderedDict
from pathlib import Path
from types import MappingProxyType

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from services.runtime_record_inspection_digest_manifest_json_encoding_service import (
    RuntimeRecordInspectionDigestManifestJsonEncodingService,
)
```

Additional standard-library imports may be used only for source inspection, mutation comparison, or invalid-input construction.

---

# TEST FIXTURES

The test module should provide a valid digest-manifest primitive fixture equivalent to:

```python
{
    "manifest_schema_version": "1.0",
    "digest_algorithm": "sha256",
    "sha256_digest": "a" * 64,
    "byte_length": 128,
    "codec": "utf-8",
    "bom_present": False,
}
```

The exact insertion order must be:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

A service fixture may return:

```python
RuntimeRecordInspectionDigestManifestJsonEncodingService()
```

---

# REQUIRED SERVICE CONSTRUCTION TESTS

The test module must prove:

1. the service class can be instantiated
2. the runtime type is exactly `RuntimeRecordInspectionDigestManifestJsonEncodingService`
3. independent constructor calls produce independent service instances
4. construction requires no arguments
5. construction creates no files
6. construction creates no directories
7. construction does not generate identifiers
8. construction does not generate timestamps
9. construction does not retain configuration
10. construction does not access environment state

Required relation:

```text
first service is not second service
```

---

# REQUIRED PUBLIC SURFACE TESTS

The service must expose:

```text
to_json_text
```

The service must not expose unauthorized methods including:

```text
to_json
serialize
deserialize
from_json
decode_json
encode_bytes
to_utf8_bytes
dump
dumps
load
loads
save
persist
export
write
read
hash
digest
checksum
sign
verify
redact
mask
classify
publish
upload
download
inspect
health
status
encode_collection
to_json_list
build_manifest
create_manifest
to_primitive_dict
```

Dunder methods inherited from Python object semantics are outside this restriction.

---

# REQUIRED EXACT INPUT ACCEPTANCE TEST

The service must accept one exact plain dictionary.

Required operation:

```python
result = service.to_json_text(primitive)
```

must complete successfully for a valid digest-manifest primitive dictionary.

The method must not mutate the supplied dictionary.

---

# REQUIRED INVALID INPUT SURFACE

The service must reject every input whose exact runtime type is not:

```text
dict
```

The invalid-input surface must include at minimum:

```text
None
True
False
0
1
1.5
"{}"
b"{}"
bytearray()
memoryview(b"")
[]
()
set()
frozenset()
object()
OrderedDict()
MappingProxyType({})
dict subclass
RuntimeRecordInspectionDigestManifest
```

A collection containing dictionaries must also be rejected.

---

# DICTIONARY SUBCLASS REJECTION

The test module must define a dictionary subclass, for example:

```python
class DerivedDict(dict):
    pass
```

An instance must be rejected even when it contains a valid digest-manifest primitive representation.

Required reduction:

```text
Dictionary Compatibility
≠
Exact Plain Dictionary
```

---

# MAPPING REJECTION

The test module must prove that mapping compatibility is insufficient.

The following must be rejected:

```text
OrderedDict
MappingProxyType
custom Mapping implementation
```

Required reduction:

```text
Mapping-Like
≠
Accepted Runtime Type
```

---

# MANIFEST OBJECT REJECTION

The service must reject an exact:

```text
RuntimeRecordInspectionDigestManifest
```

The JSON encoder accepts a primitive dictionary, not the manifest model.

Required reduction:

```text
Manifest
≠
Manifest Primitive Representation
```

---

# EXACT ERROR CONTRACT

For every non-exact dictionary input, the service must raise exactly:

```text
TypeError
```

The exact message must be:

```text
primitive must be an exact dict
```

The test must use an exact or fully anchored match.

No alternate wording is authorized.

---

# VALIDATION ORDER

Exact input type validation must occur before:

```text
JSON encoding
value traversal
fallback conversion
dictionary reconstruction
key sorting
file access
network access
registry access
external-state access
```

A rejected mapping object whose iteration or item access raises an exception may be used to prove that non-exact inputs are rejected before traversal.

---

# REQUIRED OUTPUT TYPE TEST

For valid exact dictionary input, the result runtime type must be exactly:

```text
str
```

Required assertion:

```python
assert type(result) is str
```

The result must not be:

```text
bytes
bytearray
memoryview
dict
list
tuple
path
file
stream
generator
iterator
manifest
verification result
export result
```

---

# REQUIRED EXACT JSON-DUMPS CONTRACT TEST

The output must equal:

```python
json.dumps(
    primitive,
    ensure_ascii=False,
    sort_keys=False,
    separators=(",", ":"),
)
```

The test must compare the production result directly against this exact standard-library operation.

No weaker structural comparison is sufficient.

---

# REQUIRED EXACT MANIFEST JSON TEXT TEST

For the frozen representative input:

```python
{
    "manifest_schema_version": "1.0",
    "digest_algorithm": "sha256",
    "sha256_digest": "a" * 64,
    "byte_length": 128,
    "codec": "utf-8",
    "bom_present": False,
}
```

the output must equal:

```text
{"manifest_schema_version":"1.0","digest_algorithm":"sha256","sha256_digest":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","byte_length":128,"codec":"utf-8","bom_present":false}
```

This test must prove:

```text
exact field order
compact separators
integer preservation
Boolean preservation
no trailing newline
```

---

# REQUIRED INSERTION-ORDER PRESERVATION TEST

The service must preserve supplied dictionary insertion order.

The test should provide deliberately non-alphabetical keys, for example:

```python
{
    "z": 1,
    "a": 2,
    "m": 3,
}
```

Expected output:

```text
{"z":1,"a":2,"m":3}
```

The service must not alphabetize keys.

---

# REQUIRED DIGEST-MANIFEST FIELD-ORDER TEST

The test must prove that the frozen digest-manifest representation order is preserved:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

The encoded text must contain these keys in the same order.

---

# REQUIRED NO-SORTING TEST

Production behavior must use:

```python
sort_keys=False
```

The test must demonstrate that output differs from alphabetically sorted output when input insertion order is deliberately non-alphabetical.

Required reduction:

```text
Supplied Insertion Order
≠
Alphabetical Key Order
```

---

# REQUIRED UNICODE-PRESERVATION TEST

The service must preserve Unicode directly.

The test input should include characters such as:

```text
α
Δ
É
→
≠
```

The output must contain those characters directly.

The output must not contain forced ASCII escape forms for those characters.

Required contract:

```python
ensure_ascii=False
```

---

# REQUIRED COMPACT-SEPARATOR TEST

The returned JSON text must contain no formatting spaces after commas or colons.

For:

```python
{"a": 1, "b": 2}
```

the exact output must be:

```text
{"a":1,"b":2}
```

It must not be:

```text
{"a": 1, "b": 2}
```

---

# REQUIRED NO-INDENTATION TEST

The output must not contain pretty-print indentation.

Production source must not use:

```text
indent=2
indent=4
indent=
```

The result must remain compact.

---

# REQUIRED NO-TRAILING-NEWLINE TEST

The returned string must satisfy:

```python
not result.endswith("\n")
not result.endswith("\r")
```

The service must not append a platform newline.

---

# REQUIRED INTEGER-ENCODING TEST

A Python integer must remain a JSON number.

For:

```python
{"byte_length": 128}
```

the result must contain:

```text
"byte_length":128
```

It must not contain:

```text
"byte_length":"128"
```

---

# REQUIRED BOOLEAN-ENCODING TEST

Python:

```python
False
```

must encode as:

```text
false
```

For:

```python
{"bom_present": False}
```

the exact result must be:

```text
{"bom_present":false}
```

The result must not contain:

```text
"False"
"false"
0
null
```

as replacement representations.

---

# REQUIRED TRUE-BOOLEAN NATIVE-BEHAVIOR TEST

Although `True` is not valid for the frozen digest-manifest contract, an exact dictionary containing `True` may be encoded according to native `json.dumps` behavior because the encoder does not validate manifest semantics.

For:

```python
{"value": True}
```

the output should be:

```text
{"value":true}
```

This proves:

```text
Native JSON Encoding
≠
Manifest Semantic Validation
```

---

# REQUIRED SHAPE-NONVALIDATION TEST

The service must encode an exact plain dictionary with an unexpected but JSON-compatible shape.

Examples may include:

```python
{}
{"unexpected": "value"}
{"bom_present": True}
{"byte_length": -1}
```

The service must not reject these based on manifest semantics.

Required reduction:

```text
JSON Compatibility
≠
Manifest Contract Validity
```

---

# REQUIRED STRING-PRESERVATION TEST

The service must preserve:

```text
case
leading whitespace
trailing whitespace
Unicode
punctuation
identifier text
algorithm text
codec text
digest text
```

through normal `json.dumps` behavior.

The service must not trim, lowercase, uppercase, or normalize string values.

---

# REQUIRED SOURCE NON-MUTATION TEST

The test must capture the supplied dictionary before encoding and compare it afterward.

The service must not mutate:

```text
key set
key order
values
nested JSON-compatible values
```

The input must remain structurally equal before and after encoding.

---

# REQUIRED NESTED-VALUE NON-MUTATION TEST

An exact dictionary containing nested JSON-compatible lists or dictionaries may be encoded according to native JSON behavior.

The service must not mutate nested values.

The test should compare a deep copy before and after encoding.

This does not authorize collection input; only nested values inside one exact top-level dictionary are relevant.

---

# REQUIRED DETERMINISTIC REPEATED-OUTPUT TEST

Repeated calls using the same service and unchanged ordered dictionary must produce equal JSON strings.

Required assertion:

```python
first == second
```

String identity is not part of the contract.

---

# REQUIRED CROSS-INSTANCE DETERMINISM TEST

Two independent service instances receiving equal ordered dictionaries must return equal JSON text.

Required relation:

```text
same ordered input
+
different service instances
→
equal JSON text
```

---

# REQUIRED SERVICE STATE TEST

The service must own no mutable instance state.

The test should verify:

```python
service.__dict__ == {}
```

before and after encoding, or an equivalent exact statelessness assertion.

Calling `to_json_text` must not add state.

---

# REQUIRED PRIOR-CALL INDEPENDENCE TEST

A prior call with different input must not affect a later call.

Required relation:

```text
previous encoded input
≠
later output influence
```

The service must not retain:

```text
last input
last output
call count
cache
```

---

# REQUIRED UNSUPPORTED-VALUE FAILURE TEST

An exact dictionary containing a non-JSON-serializable object must allow the native `json.dumps` exception to propagate.

Example:

```python
{"unsupported": object()}
```

The expected exception is the native JSON serialization `TypeError`.

The service must not replace the object or return error JSON.

---

# REQUIRED NO-FALLBACK-STRINGIFICATION TEST

The service must not use:

```text
default=str
str(
repr(
```

as fallback conversion for unsupported values.

An unsupported object must not silently encode as its string representation.

---

# REQUIRED FILESYSTEM-ABSENCE TEST

Calling the service must create no files or directories.

The test should:

1. change into an empty temporary directory
2. capture directory contents
3. call `to_json_text`
4. capture directory contents again
5. assert equality

Production source must not contain filesystem behavior.

---

# REQUIRED PRODUCTION-FILE EXISTENCE TEST

After implementation, the authorized production file must exist exactly at:

```text
services/runtime_record_inspection_digest_manifest_json_encoding_service.py
```

No duplicate or alternate production location is authorized.

---

# REQUIRED PRODUCTION IMPORT TEST

Production source must contain:

```python
import json
```

No other import is required.

The test should inspect production source and confirm that no model or service import is present.

---

# REQUIRED PROHIBITED-IMPORT TEST

Production source must not contain imports or dependency references including:

```text
from models
from services
import pathlib
from pathlib
import os
from os
import sys
from sys
import tempfile
from tempfile
import hashlib
from hashlib
import datetime
from datetime
import time
from time
import uuid
from uuid
import random
from random
import secrets
from secrets
import pickle
import yaml
import sqlite3
RuntimeRecordInspectionDigestManifest
RuntimeRecordInspectionDigestManifestService
RuntimeRecordInspectionDigestManifestRepresentationService
RuntimeRecordInspectionJsonEncodingService
RuntimeRecordInspectionReport
RuntimeRecordInspectionRepresentationService
RuntimeRecordInspector
RuntimeRecordRegistry
Inspectable
EventEngine
requests
urllib
http.client
socket
aiohttp
```

The only authorized dependency is Python’s `json` module.

---

# REQUIRED EXACT TYPE-CHECK SOURCE TEST

Production source must contain:

```text
type(primitive) is not dict
```

The service must not use:

```text
isinstance(primitive, dict)
```

because dictionary subclasses are rejected.

---

# REQUIRED EXACT ERROR-MESSAGE SOURCE TEST

Production source must contain the complete message:

```text
primitive must be an exact dict
```

No alternate wording is authorized.

---

# REQUIRED EXACT JSON-ARGUMENT SOURCE TEST

Production source must contain the exact arguments:

```text
ensure_ascii=False
sort_keys=False
separators=(",", ":")
```

Production source must not contain:

```text
sort_keys=True
ensure_ascii=True
indent=
default=
```

---

# REQUIRED NO-BYTE-ENCODING TEST

Production source must not contain:

```text
.encode(
bytes(
bytearray(
memoryview(
utf-8-sig
```

The service must return JSON text only.

---

# REQUIRED NO-HASHING TEST

Production source must not contain or reference:

```text
hashlib
sha256(
hexdigest(
checksum
signature
```

The service must not hash the JSON output.

---

# REQUIRED NO-VERIFICATION TEST

Production source must not define or expose behavior for:

```text
verify
validation of digest syntax
digest comparison
byte-length comparison
source-byte inspection
codec verification
BOM verification
authenticity verification
integrity verification
```

The encoder performs no evidence verification.

---

# REQUIRED NO-FILESYSTEM-SOURCE TEST

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

The service must not read or write files.

---

# REQUIRED NO-TIME-GENERATION TEST

Production source must not contain:

```text
datetime.now
datetime.utcnow
time.time
```

The service must not generate timestamps.

---

# REQUIRED NO-IDENTIFIER-GENERATION TEST

Production source must not contain:

```text
uuid
random
secrets
manifest_id
artifact_id
encoded_at
created_at
```

The service must not add generated metadata.

---

# REQUIRED NO-PERSISTENCE-OR-EXPORT TEST

The service must expose no public methods and contain no source behavior for:

```text
save
load
persist
export
publish
upload
download
register
write
read
```

The capability ends when the JSON string is returned.

---

# REQUIRED NO-DESERIALIZATION TEST

The service must not expose:

```text
from_json
decode_json
loads
parse
restore
deserialize
```

JSON text must not be converted back into a manifest or primitive representation.

---

# REQUIRED NO-COLLECTION-ENCODING TEST

The service must reject top-level:

```text
list
tuple
set
frozenset
```

including collections of dictionaries.

It must expose no:

```text
encode_collection
to_json_list
```

---

# REQUIRED NO-REGISTRY-ACCESS TEST

Production source must not reference:

```text
RuntimeRecordRegistry
manifest_registry
artifact_registry
PlatformRegistry
MissionControl
ResearchKernel
```

The JSON encoder must not register output or inspect platform state.

---

# REQUIRED NO-NETWORK TEST

Production source must not import or reference:

```text
requests
urllib
http.client
socket
aiohttp
```

The service performs no network operations.

---

# REQUIRED NO-EVENT-PUBLICATION TEST

Production source must not reference:

```text
EventEngine
publish
emit
notification
audit_event
```

JSON encoding does not publish events.

---

# REQUIRED NO-REDACTION TEST

Production source must not expose or implement:

```text
redact
mask
classify
truncate
hide
```

The service preserves supplied values through normal JSON encoding.

---

# REQUIRED EXISTING-ENCODER PRESERVATION TEST

The frozen existing file:

```text
services/runtime_record_inspection_json_encoding_service.py
```

must remain digest-manifest-unaware.

Its source must not reference:

```text
RuntimeRecordInspectionDigestManifest
RuntimeRecordInspectionDigestManifestRepresentationService
RuntimeRecordInspectionDigestManifestJsonEncodingService
digest_manifest
```

---

# REQUIRED REPRESENTATION-SERVICE PRESERVATION TEST

The frozen file:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

must remain JSON-unaware.

Its source must not contain:

```text
import json
json.dumps
to_json
to_json_text
```

---

# REQUIRED MANIFEST-MODEL PRESERVATION TEST

The frozen model must continue to expose no methods including:

```text
to_dict
to_primitive
to_json
to_json_text
serialize
encode
```

JSON encoding must remain separately owned.

---

# EXPECTED TEST-FIRST FAILURE

After the test module is created and before the production service exists, running:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest_json_encoding_service.py -q
```

must fail during collection with an error equivalent to:

```text
ModuleNotFoundError:
No module named 'services.runtime_record_inspection_digest_manifest_json_encoding_service'
```

This failure is required evidence that tests precede implementation.

---

# TEST-FIRST CHECKPOINT CONTENT

The test-first commit must contain only:

```text
docs/runtime_kernel/READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_JSON_ENCODING_TEST_CONTRACT_001.md
tests/runtime/test_runtime_record_inspection_digest_manifest_json_encoding_service.py
```

It must not contain:

```text
services/runtime_record_inspection_digest_manifest_json_encoding_service.py
```

Production implementation remains:

```text
HOLD
```

until the test-first checkpoint is committed and synchronized.

---

# EXPECTED IMPLEMENTATION VALIDATION

After the minimum production service is added, run:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest_json_encoding_service.py -q
```

All isolated tests must pass.

Then run:

```powershell
python -m pytest -q
```

The full suite must pass.

Current full-suite baseline:

```text
2307 passed
```

No existing test may be removed, weakened, skipped, or rewritten merely to accommodate implementation.

---

# PROHIBITED TEST SHORTCUTS

The tests must not:

```text
mock the production service
define the production class inside the test module
create a placeholder production module
skip the missing-module failure
accept dictionary subclasses
accept partial error wording
omit exact json.dumps comparison
omit order preservation
omit Boolean encoding
omit source non-mutation
omit unsupported-value failure
omit source restrictions
omit frozen-upstream preservation
modify frozen upstream production files
create production implementation before the test-first commit
```

---

# AUTHORIZED IMPLEMENTATION AFTER CHECKPOINT

Only after the test-first checkpoint is committed and pushed may the following file be created:

```text
services/runtime_record_inspection_digest_manifest_json_encoding_service.py
```

The implementation must be the smallest code satisfying the frozen contract and executable tests.

No additional capability is authorized.

---

# TEST CONTRACT CONCLUSION

The executable test surface is frozen around:

```text
exact plain-dictionary input
exact subclass rejection
exact TypeError contract
exact error message
exact str output
exact json.dumps operation
digest-manifest field-order preservation
no key sorting
Unicode preservation
compact separators
no indentation
no trailing newline
integer preservation
Boolean preservation
shape non-validation
source non-mutation
deterministic repeated output
cross-instance equality
stateless service
native unsupported-value failure
no fallback stringification
no existing-encoder dependency
no representation-service dependency
no manifest-model dependency
no filesystem effects
no UTF-8 encoding
no hashing
no verification
no identity generation
no persistence
no export
no deserialization
no collection encoding
no registry access
no network access
no event publication
no redaction
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
Runtime Type Compatibility
≠
Semantic Ownership
```

```text
Manifest Primitive Representation
≠
Manifest JSON Encoding
```

```text
JSON Text
≠
UTF-8 Bytes
```

```text
JSON Encoding
≠
Verification
```

```text
JSON Encoded
≠
Publicly Disclosable
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
