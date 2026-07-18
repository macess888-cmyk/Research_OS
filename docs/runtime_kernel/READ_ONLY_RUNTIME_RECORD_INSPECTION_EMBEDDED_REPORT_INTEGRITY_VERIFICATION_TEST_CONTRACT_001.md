# READ-ONLY RUNTIME RECORD INSPECTION EMBEDDED REPORT INTEGRITY VERIFICATION

# TEST CONTRACT 001

**Date:** 2026-07-18
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** TEST CONTRACT
**Status:** SERVICE TESTS AUTHORIZED / IMPLEMENTATION HOLD
**Operating Posture:** TEST-FIRST / SUBJECT-FIRST / MEASUREMENT-FIRST / PARTIAL-RESULT-PRESERVING / CONSTANT-TIME / DETERMINISTIC / NON-ADMITTING / UNKNOWN → HOLD

---

# PURPOSE

Freeze the executable test contract for:

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
```

The capability performs exactly:

```text
one exact inspection-report bytes value
+
one exact RuntimeRecordInspectionDigestManifest
→
one RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
```

The result preserves:

```text
digest_matches
byte_length_matches
bom_matches
```

and derives:

```text
integrity_matches
```

This test contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_EXISTING_DIGEST_LENGTH_CODEC_BOM_PARTIAL_RESULT_SUBJECT_BINDING_ADMISSION_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_VOCABULARY_INPUT_OWNERSHIP_PARTIAL_RESULT_DIGEST_LENGTH_BOM_AND_SCOPE_REDUCTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_RESULT_IMMUTABLE_MODEL_CONTRACT_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_IMMUTABLE_SERVICE_CONTRACT_001.md
```

The immutable result model is already implemented and frozen.

Production service implementation remains:

```text
HOLD
```

until:

1. this test contract exists
2. the authorized service test module exists
3. the expected missing-module failure is observed
4. the service test-first checkpoint is committed and pushed

---

# AUTHORIZED TEST FILE

The exact authorized test location is:

```text
tests/runtime/test_runtime_record_inspection_embedded_report_integrity_verification_service.py
```

No alternative test file is authorized.

---

# FUTURE PRODUCTION FILE

The exact future production location is:

```text
services/runtime_record_inspection_embedded_report_integrity_verification_service.py
```

This file must not exist when the expected test-first failure is first observed.

---

# REQUIRED TEST IMPORTS

The test module may import:

```python
import hashlib
import hmac
from pathlib import Path
from unittest.mock import patch

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)
from services.runtime_record_inspection_embedded_report_integrity_verification_service import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
)
```

Additional standard-library imports may be used only for deterministic source inspection or subclass construction.

---

# REPRESENTATIVE REPORT BYTES

The test module should define representative values including:

```python
EMPTY_REPORT_BYTES = b""

REPORT_BYTES = b'{"status":"PASS"}'

DIFFERENT_REPORT_BYTES = b'{"status":"FAIL"}'

BOM_REPORT_BYTES = (
    b"\xef\xbb\xbf"
    b'{"status":"PASS"}'
)
```

Arbitrary non-text bytes should also be tested:

```python
BINARY_REPORT_BYTES = b"\x00\xff\x01"
```

---

# REPRESENTATIVE MANIFEST FACTORY

The test module should use a helper structurally equivalent to:

```python
def make_manifest(
    report_bytes: bytes,
    *,
    sha256_digest: str | None = None,
    byte_length: int | None = None,
    bom_present: bool = False,
) -> RuntimeRecordInspectionDigestManifest:
    return RuntimeRecordInspectionDigestManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest=(
            hashlib.sha256(report_bytes).hexdigest()
            if sha256_digest is None
            else sha256_digest
        ),
        byte_length=(
            len(report_bytes)
            if byte_length is None
            else byte_length
        ),
        codec="utf-8",
        bom_present=bom_present,
    )
```

The helper belongs to the test module only.

It must not be added to production code.

---

# REQUIRED SERVICE CONSTRUCTION TESTS

The test suite must prove:

1. the service can be instantiated
2. the exact runtime type is correct
3. independent constructor calls produce independent instances
4. construction requires no arguments
5. construction creates no files
6. construction creates no directories
7. construction generates no identifiers
8. construction generates no timestamps
9. construction reads no environment configuration
10. construction retains no mutable state

Required relation:

```text
first service is not second service
```

---

# REQUIRED PUBLIC SURFACE TESTS

The service must expose:

```text
verify_integrity
```

The service must not expose unauthorized capability methods including:

```text
verify
verify_report
verify_digest
verify_manifest
verify_bytes
compare
compare_digest
calculate_digest
calculate_length
inspect_bom
decode
parse
save
load
persist
export
write
read
publish
upload
download
register
inspect
health
status
verify_collection
create_receipt
admit
approve
trust
authorize
```

Standard object dunder methods are outside this restriction.

---

# REQUIRED EXACT REPORT-BYTES ACCEPTANCE

The service must accept one exact plain `bytes` value.

Accepted examples must include:

```text
empty bytes
ASCII-compatible bytes
arbitrary binary bytes
bytes beginning with UTF-8 BOM
bytes not beginning with UTF-8 BOM
```

The service must not require:

```text
valid UTF-8
valid JSON
valid report schema
non-empty bytes
```

---

# REQUIRED INVALID REPORT-BYTES TYPES

The service must reject values whose exact runtime type is not `bytes`.

The invalid surface must include:

```text
None
True
False
0
1
1.5
str
bytearray
memoryview
list
tuple
set
frozenset
dictionary
object
Path
file-like object
bytes subclass
manifest
```

Each invalid value must raise exactly:

```text
TypeError
```

with:

```text
report_bytes must be an exact bytes
```

---

# REQUIRED BYTES-SUBCLASS REJECTION

The test module must define:

```python
class DerivedBytes(bytes):
    pass
```

The service must reject:

```python
DerivedBytes(REPORT_BYTES)
```

with the exact report-bytes TypeError.

```text
Bytes Compatibility
≠
Exact Plain Bytes
```

---

# REQUIRED EXACT MANIFEST ACCEPTANCE

The service must accept exact:

```text
RuntimeRecordInspectionDigestManifest
```

No primitive representation or duck-typed substitute is accepted.

---

# REQUIRED INVALID MANIFEST TYPES

The service must reject:

```text
None
bool
int
float
str
bytes
bytearray
memoryview
list
tuple
set
frozenset
dictionary
mapping
object
Path
result model
duck-typed manifest
mock manifest
manifest subclass
```

Each invalid value must raise exactly:

```text
TypeError
```

with:

```text
manifest must be an exact RuntimeRecordInspectionDigestManifest
```

---

# REQUIRED MANIFEST-SUBCLASS REJECTION

The test module must define:

```python
class DerivedManifest(RuntimeRecordInspectionDigestManifest):
    pass
```

A derived manifest instance must be rejected.

```text
Manifest Compatibility
≠
Exact Manifest Ownership
```

---

# REQUIRED INPUT VALIDATION ORDER

The exact validation order is:

```text
report_bytes runtime type
→
manifest runtime type
→
SHA-256 measurement
→
digest comparison
→
byte-length comparison
→
BOM-prefix observation
→
result construction
```

When both inputs have invalid runtime types, the report-bytes TypeError must occur first.

No hashing, comparison, length check, BOM inspection, or result construction may occur before both types are valid.

---

# REQUIRED NO-MEASUREMENT-BEFORE-VALIDATION TESTS

When `report_bytes` is invalid:

```text
hashlib.sha256
hmac.compare_digest
```

must not be called.

When `manifest` is invalid:

```text
hashlib.sha256
hmac.compare_digest
```

must not be called.

The result model constructor must not be called for invalid inputs.

---

# REQUIRED EMPTY-BYTES TEST

The service must accept:

```python
b""
```

A matching manifest for empty bytes must produce:

```text
digest_matches = True
byte_length_matches = True
bom_matches = True
integrity_matches = True
```

---

# REQUIRED ARBITRARY-BYTES TESTS

The service must accept:

```python
b"\x00"
b"\xff"
b"\x00\xff\x01"
b"\xef\xbb"
b"\xef\xbb\xbf"
```

No decoding or parsing may be required.

---

# REQUIRED SHA-256 SUBJECT TEST

The digest must be calculated from exactly:

```text
report_bytes
```

The service must not hash:

```text
manifest
manifest representation
manifest JSON
manifest bytes
report object
string representation
```

A patch or spy should prove that `hashlib.sha256` receives the exact supplied bytes.

Representative form:

```python
with patch(
    "services."
    "runtime_record_inspection_embedded_report_integrity_verification_service."
    "hashlib.sha256"
) as sha256:
    hash_object = sha256.return_value
    hash_object.hexdigest.return_value = "a" * 64

    service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

sha256.assert_called_once_with(REPORT_BYTES)
hash_object.hexdigest.assert_called_once_with()
```

---

# REQUIRED SHA-256 HEXDIGEST TEST

The service must call:

```text
hexdigest
```

exactly once on the SHA-256 object.

It must not use:

```text
digest()
digest_size
block_size
```

as the comparison value.

---

# REQUIRED CONSTANT-TIME DIGEST COMPARISON TEST

The service must delegate digest comparison to:

```python
hmac.compare_digest(
    computed_digest,
    manifest.sha256_digest,
)
```

Tests must prove:

1. `hmac.compare_digest` is called exactly once
2. the computed digest is the first argument
3. the manifest digest is the second argument
4. its Boolean result becomes `digest_matches`

Representative form:

```python
with patch(
    "services."
    "runtime_record_inspection_embedded_report_integrity_verification_service."
    "hmac.compare_digest",
    return_value=False,
) as compare_digest:
    result = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

compare_digest.assert_called_once_with(
    hashlib.sha256(REPORT_BYTES).hexdigest(),
    manifest.sha256_digest,
)

assert result.digest_matches is False
```

---

# REQUIRED NO-PLAIN-EQUALITY DIGEST TEST

Production source must not use:

```python
computed_digest == manifest.sha256_digest
```

or an equivalent plain equality operation for digest comparison.

The executable `hmac.compare_digest` delegation test is authoritative.

---

# REQUIRED DIGEST FULL-MATCH TEST

For matching report bytes and manifest digest:

```text
digest_matches is True
```

The exact runtime type must be:

```text
bool
```

---

# REQUIRED DIGEST-ONLY MISMATCH TEST

Create a valid manifest whose digest differs while:

```text
byte_length matches
BOM state matches
```

The result must be:

```text
digest_matches = False
byte_length_matches = True
bom_matches = True
integrity_matches = False
```

The operation must not raise an exception.

---

# REQUIRED BYTE-LENGTH COMPARISON TEST

The service must compare:

```python
len(report_bytes)
```

with:

```python
manifest.byte_length
```

Tests must prove that matching values produce:

```text
byte_length_matches is True
```

and differing values produce:

```text
byte_length_matches is False
```

---

# REQUIRED LENGTH-ONLY MISMATCH TEST

Create a valid manifest with:

```text
matching digest
incorrect byte_length
matching BOM state
```

The result must be:

```text
digest_matches = True
byte_length_matches = False
bom_matches = True
integrity_matches = False
```

No exception is authorized.

---

# REQUIRED UTF-8 BOM-PREFIX OBSERVATION TEST

The service must inspect whether the bytes begin exactly with:

```python
b"\xef\xbb\xbf"
```

Tests must cover:

```text
exact BOM prefix
BOM followed by content
partial EF prefix
partial EF BB prefix
BOM bytes appearing later in content
no BOM
empty bytes
```

Only a prefix at index zero counts as observed BOM presence.

---

# REQUIRED BOM-NOT-PRESENT MATCH TEST

For bytes not beginning with the UTF-8 BOM marker and a valid manifest declaring:

```text
bom_present = False
```

the result must contain:

```text
bom_matches is True
```

---

# REQUIRED BOM-ONLY MISMATCH TEST

For bytes beginning with:

```python
b"\xef\xbb\xbf"
```

and a valid manifest declaring:

```text
bom_present = False
```

while digest and byte length match those exact bytes, the result must be:

```text
digest_matches = True
byte_length_matches = True
bom_matches = False
integrity_matches = False
```

No exception is authorized.

---

# REQUIRED BOM-NON-PREFIX TEST

Bytes containing the BOM sequence after the first byte must not be treated as BOM-prefixed.

Representative value:

```python
b"x\xef\xbb\xbf"
```

Expected:

```text
observed BOM presence = False
bom_matches = True
```

for the valid manifest contract.

---

# REQUIRED NO-CODEC-CHECK TEST

The result must not contain:

```text
codec_matches
```

Production source must not:

```text
decode report bytes
inspect manifest.codec
claim UTF-8 provenance
```

The service must not call:

```python
report_bytes.decode("utf-8")
```

```text
UTF-8 Decodable
≠
Created By UTF-8 Encoder
```

---

# REQUIRED RESULT-TYPE TEST

The exact returned runtime type must be:

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
```

It must not return:

```text
bool
dict
tuple
list
string
enum
manifest
receipt
None
```

---

# REQUIRED RESULT-CONSTRUCTION TEST

The service must construct the result using exactly:

```text
digest_matches
byte_length_matches
bom_matches
```

The service must not pass:

```text
integrity_matches
```

to the result constructor.

A patch of the imported result model may prove the exact keyword arguments.

---

# REQUIRED RESULT-COMPONENT-PROPAGATION TEST

Tests must independently control or induce:

```text
digest_matches
byte_length_matches
bom_matches
```

and verify that the exact values appear in the returned result.

No component may be reordered or substituted.

---

# REQUIRED FULL-MATCH TEST

For bytes and manifest where all authorized facts match:

```text
digest_matches = True
byte_length_matches = True
bom_matches = True
integrity_matches = True
```

---

# REQUIRED PARTIAL-MISMATCH TEST MATRIX

The test suite must cover at minimum:

```text
False, True, True
True, False, True
True, True, False
False, False, True
False, True, False
True, False, False
```

Each must return a valid result.

Each must derive:

```text
integrity_matches = False
```

---

# REQUIRED COMPLETE-MISMATCH TEST

The suite must cover:

```text
digest_matches = False
byte_length_matches = False
bom_matches = False
integrity_matches = False
```

This remains a valid result.

It must not raise an exception.

---

# REQUIRED MISMATCH-NOT-EXCEPTION TEST

Digest, length, and BOM disagreement are valid outcomes.

The service must not raise for any valid mismatch combination.

```text
Integrity Mismatch
≠
Verification Execution Failure
```

---

# REQUIRED MALFORMED-INPUT DISTINCTION

Invalid runtime input must raise.

Valid input disagreement must return a result.

```text
Invalid Runtime Input
≠
Integrity Mismatch
```

---

# REQUIRED DETERMINISM TEST

Repeated calls with unchanged exact inputs must produce equal results.

Required relation:

```python
first == second
```

Object identity may differ:

```python
first is not second
```

---

# REQUIRED CROSS-INSTANCE DETERMINISM

Independent service instances must produce equal results for equal inputs.

---

# REQUIRED STATELESSNESS TEST

The service must own no mutable instance state.

The test should verify:

```python
service.__dict__ == {}
```

before and after:

```text
full match
partial mismatch
complete mismatch
invalid input
```

---

# REQUIRED PRIOR-CALL INDEPENDENCE

A prior mismatch must not affect a later full match.

A prior full match must not affect a later mismatch.

The service must retain no previous inputs or results.

---

# REQUIRED NO-FILESYSTEM-EFFECT TEST

Calling the service must create no files or directories.

The test should:

1. change into an empty temporary directory
2. capture directory contents
3. run a full match
4. run one or more mismatch cases
5. capture directory contents again
6. assert equality

---

# REQUIRED PRODUCTION-FILE EXISTENCE TEST

After implementation, the exact production file must exist at:

```text
services/runtime_record_inspection_embedded_report_integrity_verification_service.py
```

No duplicate or alternate production location is authorized.

---

# REQUIRED EXACT IMPORT TEST

Production source must import exactly:

```python
import hashlib
import hmac

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)
```

No other import is authorized.

---

# REQUIRED EXACT TYPE-CHECK SOURCE TEST

Production source must contain:

```text
type(report_bytes) is not bytes
```

and:

```text
type(manifest) is not RuntimeRecordInspectionDigestManifest
```

It must not use:

```text
isinstance(report_bytes, bytes)
isinstance(manifest, RuntimeRecordInspectionDigestManifest)
```

---

# REQUIRED EXACT ERROR-MESSAGE SOURCE TEST

Production source must contain the complete exact messages:

```text
report_bytes must be an exact bytes
manifest must be an exact RuntimeRecordInspectionDigestManifest
```

---

# REQUIRED SHA-256 SOURCE TEST

Production source must contain:

```text
hashlib.sha256(
```

and:

```text
.hexdigest()
```

The service must not expose a public digest method.

---

# REQUIRED HMAC SOURCE TEST

Production source must contain:

```text
hmac.compare_digest(
```

It must not contain:

```text
hmac.new
hmac.digest
digestmod
key=
secret
salt
nonce
pepper
```

---

# REQUIRED BYTE-LENGTH SOURCE TEST

Production source must contain:

```text
len(report_bytes)
```

and:

```text
manifest.byte_length
```

---

# REQUIRED BOM SOURCE TEST

Production source must contain:

```text
report_bytes.startswith(
```

and the exact byte literal:

```text
b"\xef\xbb\xbf"
```

Production source must compare the observed result against:

```text
manifest.bom_present
```

---

# REQUIRED RESULT-CONSTRUCTION SOURCE TEST

Production source must contain:

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
```

with keyword assignments:

```text
digest_matches=digest_matches
byte_length_matches=byte_length_matches
bom_matches=bom_matches
```

It must not contain constructor assignment for:

```text
integrity_matches=
```

---

# REQUIRED NO-CODEC SOURCE TEST

Production source must not contain:

```text
codec_matches
report_bytes.decode(
manifest.codec
decode("utf-8")
decode('utf-8')
```

---

# REQUIRED NO-PARSING TEST

Production source must not contain:

```text
json.loads
json.dumps
parse
from_dict
from_json
RuntimeRecordInspectionRepresentationService
RuntimeRecordInspectionJsonEncodingService
```

The service verifies exact supplied bytes only.

---

# REQUIRED NO-UPSTREAM-SERVICE-DEPENDENCY TEST

Production source must not import or instantiate:

```text
RuntimeRecordInspectionSha256DigestService
RuntimeRecordInspectionDigestManifestDigestVerificationService
RuntimeRecordInspectionDigestManifestService
RuntimeRecordInspectionUtf8ByteEncodingService
```

Internal measurement uses the standard library directly.

---

# REQUIRED PROHIBITED-DEPENDENCY TEST

Production source must not contain unauthorized dependency fragments including:

```text
import pathlib
from pathlib
import os
from os
import sys
from sys
import tempfile
from tempfile
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
import json
from json
import codecs
from codecs
import io
from io
import sqlite3
import requests
import urllib
import socket
Inspectable
EventEngine
RuntimeRecordRegistry
```

The two frozen model imports remain authorized.

---

# REQUIRED NO-FILESYSTEM SOURCE TEST

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
```

---

# REQUIRED NO-TIME-GENERATION TEST

Production source must not contain:

```text
datetime.now
datetime.utcnow
time.time
```

---

# REQUIRED NO-IDENTIFIER-GENERATION TEST

Production source must not contain:

```text
uuid
random
secrets
verification_id
result_id
created_at
verified_at
```

---

# REQUIRED NO-PERSISTENCE TEST

The service must expose no:

```text
save
load
persist
write
read
register
create_receipt
```

---

# REQUIRED NO-EVENT-OR-LOGGING TEST

Production source must not contain:

```text
publish
emit
logger
notification
alert
audit_event
verification_event
mismatch_event
```

---

# REQUIRED NO-EXPORT-OR-TRANSPORT TEST

The service must expose no:

```text
export
upload
download
stream
send
transfer
```

Production source must not reference:

```text
socket
requests
urllib
http.client
aiohttp
```

---

# REQUIRED NO-COLLECTION-VERIFICATION TEST

The service must reject top-level collection inputs through exact type checks.

It must expose no:

```text
verify_collection
verify_batch
compare_many
```

---

# REQUIRED NO-MERKLE-OR-HASH-CHAIN TEST

Production source must not contain:

```text
merkle
hash_chain
digest_chain
aggregate_digest
collection_digest
```

---

# REQUIRED NO-SIGNATURE-VERIFICATION TEST

Production source must not contain:

```text
verify_signature
load_key
certificate
attestation
signer
```

---

# REQUIRED RESULT-MODEL PRESERVATION

The frozen result model must remain measurement-unaware.

Its source must not gain:

```text
hashlib
hmac
report_bytes
manifest
computed_digest
verify_integrity
len(
startswith(
```

---

# REQUIRED MANIFEST-MODEL PRESERVATION

The frozen manifest model must not gain:

```text
verify_integrity
digest_matches
byte_length_matches
bom_matches
integrity_matches
report_bytes
```

---

# REQUIRED FROZEN-UPSTREAM PRESERVATION

The following components must remain unchanged and embedded-integrity-service-unaware:

```text
models/runtime_record_inspection_digest_manifest.py
models/runtime_record_inspection_embedded_report_integrity_verification_result.py
services/runtime_record_inspection_digest_manifest_service.py
services/runtime_record_inspection_representation_service.py
services/runtime_record_inspection_json_encoding_service.py
services/runtime_record_inspection_utf8_byte_encoding_service.py
services/runtime_record_inspection_sha256_digest_service.py
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

---

# EXPECTED TEST-FIRST FAILURE

After the test module is created and before the production service exists, running:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_embedded_report_integrity_verification_service.py -q
```

must fail during collection with an error equivalent to:

```text
ModuleNotFoundError:
No module named 'services.runtime_record_inspection_embedded_report_integrity_verification_service'
```

This failure is required evidence that tests precede implementation.

---

# TEST-FIRST CHECKPOINT CONTENT

The test-first commit must contain only:

```text
docs/runtime_kernel/READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_TEST_CONTRACT_001.md
tests/runtime/test_runtime_record_inspection_embedded_report_integrity_verification_service.py
```

It must not contain:

```text
services/runtime_record_inspection_embedded_report_integrity_verification_service.py
```

---

# EXPECTED IMPLEMENTATION VALIDATION

After the minimum production service is added, run:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_embedded_report_integrity_verification_service.py -q
```

All isolated service tests must pass.

Then run:

```powershell
python -m pytest -q
```

The full suite must pass.

Current full-suite baseline:

```text
2998 passed
```

No existing test may be removed, weakened, skipped, or rewritten merely to accommodate implementation.

---

# PROHIBITED TEST SHORTCUTS

The tests must not:

```text
define the production service inside the test module
mock the production service itself
create a placeholder production module
skip the missing-module failure
accept bytes subclasses
accept manifest subclasses
accept partial error wording
omit validation order
omit hashing subject checks
omit constant-time comparison
use plain equality as authoritative digest comparison
omit length-only mismatch
omit BOM-only mismatch
omit partial combinations
collapse result into bool
permit codec claims
permit decoding or parsing
omit statelessness
omit source restrictions
omit frozen-upstream preservation
create production implementation before the test-first commit
```

---

# AUTHORIZED IMPLEMENTATION AFTER CHECKPOINT

Only after the service test-first checkpoint is committed and pushed may the following file be created:

```text
services/runtime_record_inspection_embedded_report_integrity_verification_service.py
```

The implementation must be the smallest code satisfying the frozen contract and executable tests.

No additional capability is authorized.

---

# TEST CONTRACT CONCLUSION

The executable service-test surface is frozen around:

```text
exact service location
exact service class
constructor requires no arguments
exact public method
exact report-bytes runtime type
bytes-subclass rejection
exact manifest runtime type
manifest-subclass rejection
exact TypeError messages
fixed validation order
empty bytes acceptance
arbitrary bytes acceptance
SHA-256 measurement of exact report bytes
hexdigest use
constant-time digest comparison
byte-length comparison
UTF-8 BOM-prefix observation
BOM comparison against manifest
no codec claim
no decoding
no parsing
exact result type
exact component propagation
derived aggregate ownership
full match
all partial mismatch classes
complete mismatch
mismatch not exception
determinism
statelessness
no filesystem effects
no persistence
no events or logging
no export or transport
no collection verification
no Merkle or hash-chain verification
no signature verification
exact import boundary
frozen result-model preservation
frozen manifest-model preservation
frozen upstream preservation
```

The next authorized action is:

```text
create the service test module
observe the expected missing-module failure
commit and push the service test-first checkpoint
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
Observed Byte Subject
≠
Expected Claim Container
```

```text
Internal Digest Measurement
≠
New Public Digest Capability
```

```text
Digest Value Equality
≠
Constant-Time Digest Comparison
```

```text
Combined Verification Bool
≠
Preserved Partial Evidence
```

```text
Invalid Runtime Input
≠
Integrity Mismatch
```

```text
Partial Mismatch
≠
Verification Execution Failure
```

```text
UTF-8 Decodable
≠
Created By UTF-8 Encoder
```

```text
Digest Mismatch
≠
Tampering Proof
```

```text
Length Mismatch
≠
Cause Attribution
```

```text
Call-Local Pairing
≠
Historical Subject Binding
```

```text
Integrity Facts Match
≠
Identity Established
```

```text
Integrity Match
≠
Integrity Admission
```

```text
Integrity Match
≠
Trust
```

```text
Integrity Match
≠
Authority Granted
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
