# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST DIGEST VERIFICATION

# TEST CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** TEST CONTRACT
**Status:** TESTS AUTHORIZED / IMPLEMENTATION HOLD
**Operating Posture:** TEST-FIRST / COMPARISON-FIRST / SYNTAX-FIRST / CONSTANT-TIME / DETERMINISTIC / NON-ADMITTING / UNKNOWN → HOLD

---

# PURPOSE

Freeze the executable test contract for:

```text
RuntimeRecordInspectionDigestManifestDigestVerificationService
```

The capability performs exactly:

```text
one valid computed digest-manifest SHA-256 hexadecimal string
+
one valid expected digest-manifest SHA-256 hexadecimal string
→
one deterministic Boolean constant-time comparison result
```

This test contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_DIGEST_VERIFICATION_EXISTING_COMPARISON_CONSTANT_TIME_SYNTAX_RESULT_MISMATCH_ADMISSION_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_DIGEST_VERIFICATION_VOCABULARY_INPUT_ROLES_SYNTAX_CONSTANT_TIME_BOOLEAN_RESULT_MISMATCH_AND_SCOPE_REDUCTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_DIGEST_VERIFICATION_IMMUTABLE_SERVICE_CONTRACT_001.md
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
tests/runtime/test_runtime_record_inspection_digest_manifest_digest_verification_service.py
```

No other test file is required for the first capability.

---

# FUTURE PRODUCTION FILE

The exact future production location is:

```text
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

This file must not exist when the expected test-first failure is first observed.

---

# FROZEN UPSTREAM FILES

The following files must remain unchanged:

```text
models/runtime_record_inspection_digest_manifest.py
services/runtime_record_inspection_digest_manifest_service.py
services/runtime_record_inspection_digest_manifest_representation_service.py
services/runtime_record_inspection_digest_manifest_json_encoding_service.py
services/runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py
services/runtime_record_inspection_digest_manifest_sha256_digest_service.py
services/runtime_record_inspection_sha256_digest_service.py
```

The first verification capability requires no modification to any frozen upstream component.

---

# REQUIRED TEST IMPORTS

The test module may import:

```python
import hmac
from pathlib import Path
from unittest.mock import patch

import pytest

from services.runtime_record_inspection_digest_manifest_digest_verification_service import (
    RuntimeRecordInspectionDigestManifestDigestVerificationService,
)
```

Additional standard-library imports may be used only for source inspection, invalid-input construction, or deterministic comparison.

---

# REPRESENTATIVE VALID DIGESTS

The test module should define:

```python
MATCHING_DIGEST = (
    "ba7816bf8f01cfea414140de5dae2223"
    "b00361a396177a9cb410ff61f20015ad"
)
```

```python
DIFFERENT_DIGEST = (
    "ca7816bf8f01cfea414140de5dae2223"
    "b00361a396177a9cb410ff61f20015ad"
)
```

Both values must satisfy:

```text
exactly 64 characters
lowercase hexadecimal only
```

---

# REQUIRED SERVICE CONSTRUCTION TESTS

The test module must prove:

1. the service can be instantiated
2. its exact runtime type is correct
3. independent constructor calls produce independent instances
4. construction requires no arguments
5. construction creates no files
6. construction creates no directories
7. construction generates no identifiers
8. construction generates no timestamps
9. construction reads no environment configuration
10. construction retains no comparison state

Required relation:

```text
first service is not second service
```

---

# REQUIRED PUBLIC SURFACE TESTS

The service must expose:

```text
verify_digest
```

The service must not expose unauthorized methods including:

```text
compare
compare_digests
matches
is_valid
validate
hash
digest
to_sha256_hexdigest
verify_manifest
verify_bytes
verify_report_digest
verify_signature
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
```

Dunder methods inherited from Python object semantics are outside this restriction.

---

# REQUIRED EXACT INPUT ACCEPTANCE

The service must accept:

```text
one exact plain computed-digest string
one exact plain expected-digest string
```

Required operations:

```python
result = service.verify_digest(
    MATCHING_DIGEST,
    MATCHING_DIGEST,
)
```

```python
result = service.verify_digest(
    MATCHING_DIGEST,
    DIFFERENT_DIGEST,
)
```

Both operations must complete successfully.

---

# REQUIRED INVALID COMPUTED-DIGEST TYPES

The service must reject computed-digest values whose exact runtime type is not `str`.

The invalid surface must include:

```text
None
True
False
0
1
1.5
bytes
bytearray
memoryview
list
tuple
set
frozenset
dictionary
object
Path
string subclass
```

The exact error must be:

```text
TypeError
```

with:

```text
computed_digest must be an exact str
```

---

# REQUIRED INVALID EXPECTED-DIGEST TYPES

The service must reject expected-digest values whose exact runtime type is not `str`.

The same invalid surface must be tested.

The exact error must be:

```text
TypeError
```

with:

```text
expected_digest must be an exact str
```

---

# STRING-SUBCLASS REJECTION

The test module must define:

```python
class DerivedString(str):
    pass
```

Both roles must reject `DerivedString`.

```text
String Compatibility
≠
Exact Plain String
```

---

# TYPE VALIDATION ORDER

The exact type-validation order is:

```text
computed digest type
→
expected digest type
```

When both values have invalid runtime types, the computed-digest TypeError must occur first.

No syntax validation or comparison may occur before both runtime types are valid.

---

# REQUIRED VALID SYNTAX TESTS

The test module must prove acceptance of valid strings containing only:

```text
0-9
a-f
```

with exact length:

```text
64
```

Representative valid values should include:

```python
"0" * 64
"f" * 64
"0123456789abcdef" * 4
```

---

# REQUIRED INVALID COMPUTED-DIGEST SYNTAX

The invalid computed-digest surface must include:

```text
empty string
63 characters
65 characters
uppercase hexadecimal
mixed-case hexadecimal
sha256: prefix
SHA256: prefix
0x prefix
leading space
trailing space
embedded space
tab
newline
carriage return
colon separator
hyphen separator
non-hexadecimal character
Unicode lookalike character
```

Each must raise exactly:

```text
ValueError
```

with:

```text
computed_digest must be a lowercase 64-character SHA-256 hexadecimal string
```

---

# REQUIRED INVALID EXPECTED-DIGEST SYNTAX

The same invalid syntax surface must be tested for `expected_digest`.

Each must raise exactly:

```text
ValueError
```

with:

```text
expected_digest must be a lowercase 64-character SHA-256 hexadecimal string
```

---

# SYNTAX VALIDATION ORDER

The exact syntax-validation order is:

```text
computed digest syntax
→
expected digest syntax
```

When both strings are malformed, the computed-digest ValueError must occur first.

Comparison must not occur if either syntax validation fails.

---

# INVALID SYNTAX VERSUS MISMATCH

Tests must prove:

```text
invalid syntax
→
exception
```

```text
valid unequal digests
→
False
```

Malformed input must never collapse into mismatch.

```text
Invalid Digest Syntax
≠
Digest Mismatch
```

---

# REQUIRED VALID MATCH TEST

For two valid equal digest strings:

```python
result = service.verify_digest(
    MATCHING_DIGEST,
    MATCHING_DIGEST,
)
```

the result must be:

```python
True
```

and:

```python
type(result) is bool
```

---

# REQUIRED VALID MISMATCH TEST

For two valid unequal digest strings:

```python
result = service.verify_digest(
    MATCHING_DIGEST,
    DIFFERENT_DIGEST,
)
```

the result must be:

```python
False
```

and:

```python
type(result) is bool
```

A valid mismatch must not raise an exception.

---

# REQUIRED EXACT OUTPUT TYPE

The service must return exact plain:

```text
bool
```

It must not return:

```text
integer
string
tuple
dictionary
enum
verification model
receipt
manifest
None
```

Required assertion:

```python
assert type(result) is bool
```

---

# REQUIRED CONSTANT-TIME DELEGATION TEST

The test suite must prove that production comparison delegates to:

```python
hmac.compare_digest(
    computed_digest,
    expected_digest,
)
```

A patch or spy may verify:

1. `hmac.compare_digest` is called exactly once
2. it receives the computed digest first
3. it receives the expected digest second
4. its Boolean return value is returned directly

Representative form:

```python
with patch(
    "services.runtime_record_inspection_digest_manifest_digest_verification_service.hmac.compare_digest",
    return_value=True,
) as compare_digest:
    result = service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

compare_digest.assert_called_once_with(
    MATCHING_DIGEST,
    MATCHING_DIGEST,
)

assert result is True
```

---

# REQUIRED NO-COMPARISON-BEFORE-VALIDATION TEST

When either input has invalid type or syntax:

```text
hmac.compare_digest
```

must not be called.

Tests should patch the function and assert:

```python
compare_digest.assert_not_called()
```

---

# REQUIRED NO-PLAIN-EQUALITY SOURCE TEST

Production source must not use plain digest equality as the result comparison.

The source must not contain a comparison equivalent to:

```python
computed_digest == expected_digest
```

Source checking should avoid falsely prohibiting equality used only inside unrelated validation expressions.

The executable delegation test to `hmac.compare_digest` is authoritative.

---

# REQUIRED NO-NORMALIZATION TESTS

The service must reject rather than normalize:

```text
uppercase digest
leading whitespace
trailing whitespace
sha256: prefix
0x prefix
newline
colon separators
hyphen separators
```

It must not:

```text
lowercase
strip
replace
remove prefixes
pad
truncate
```

---

# REQUIRED DETERMINISM TEST

Repeated calls with unchanged valid inputs must produce equal Boolean values.

```python
first = service.verify_digest(
    MATCHING_DIGEST,
    MATCHING_DIGEST,
)

second = service.verify_digest(
    MATCHING_DIGEST,
    MATCHING_DIGEST,
)

assert first is second
```

---

# REQUIRED CROSS-INSTANCE DETERMINISM

Independent service instances must return equal Boolean results for equal input pairs.

---

# REQUIRED STATELESSNESS TEST

The service must own no mutable instance state.

The test should verify:

```python
service.__dict__ == {}
```

before and after valid matches, valid mismatches, and rejected input.

---

# REQUIRED PRIOR-CALL INDEPENDENCE

A prior mismatch must not affect a later match.

A prior match must not affect a later mismatch.

The service must not retain:

```text
last computed digest
last expected digest
last result
call count
cache
history
```

---

# REQUIRED PRODUCTION-FILE EXISTENCE TEST

After implementation, the authorized production file must exist exactly at:

```text
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

No duplicate or alternate location is authorized.

---

# REQUIRED PRODUCTION IMPORT TEST

Production source must import exactly:

```python
import hmac
```

No other import is authorized.

---

# REQUIRED EXACT TYPE-CHECK SOURCE TEST

Production source must contain:

```text
type(computed_digest) is not str
```

and:

```text
type(expected_digest) is not str
```

It must not use:

```text
isinstance(computed_digest, str)
isinstance(expected_digest, str)
```

---

# REQUIRED EXACT ERROR-MESSAGE SOURCE TEST

Production source must contain all four exact messages:

```text
computed_digest must be an exact str
expected_digest must be an exact str
computed_digest must be a lowercase 64-character SHA-256 hexadecimal string
expected_digest must be a lowercase 64-character SHA-256 hexadecimal string
```

---

# REQUIRED HMAC COMPARISON SOURCE TEST

Production source must contain:

```text
hmac.compare_digest(
```

It must not contain:

```text
hmac.new
hmac.digest
digestmod
```

---

# REQUIRED NO-DIGEST-GENERATION TEST

Production source must not contain:

```text
import hashlib
hashlib.sha256
hexdigest
RuntimeRecordInspectionDigestManifestSha256DigestService
runtime_record_inspection_digest_manifest_sha256_digest_service
```

The service compares supplied digest strings only.

---

# REQUIRED NO-MANIFEST DEPENDENCY TEST

Production source must not contain:

```text
from models
RuntimeRecordInspectionDigestManifest
runtime_record_inspection_digest_manifest import
```

Care must be taken not to reject the required verification service class name merely because it contains `DigestManifest`.

---

# REQUIRED PROHIBITED-DEPENDENCY TEST

Production source must not contain dependency fragments including:

```text
import hashlib
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
import socket
import requests
import urllib
import sqlite3
RuntimeRecordInspectionDigestManifestSha256DigestService
RuntimeRecordRegistry
RuntimeRecordInspector
Inspectable
EventEngine
```

The required service class name and `hmac.compare_digest` must remain allowed.

---

# REQUIRED NO-HMAC-GENERATION TEST

Production source must not contain:

```text
hmac.new
hmac.digest
digestmod
key=
secret
nonce
salt
pepper
```

```text
hmac.compare_digest
≠
HMAC Generation
```

---

# REQUIRED NO-RESULT-MODEL TEST

The service must return exact `bool`.

Production source must not construct or reference:

```text
VerificationResult
verification receipt
status enum
reason model
comparison artifact
```

---

# REQUIRED NO-BYTES-INPUT TEST

The service must reject:

```text
bytes
bytearray
memoryview
```

for both roles.

It must not decode byte input.

---

# REQUIRED NO-EMBEDDED-REPORT-VERIFICATION TEST

Production source must not inspect or reference:

```text
sha256_digest
byte_length
codec
bom_present
inspection_report
report_bytes
```

The service compares two strings only.

---

# REQUIRED NO-SUBJECT-BINDING TEST

Production source must not contain:

```text
manifest_id
record_id
subject_id
source_ref
registry_ref
execution_ref
```

The comparison result does not establish digest ownership.

---

# REQUIRED NO-PROVENANCE TEST

Production source must not reference:

```text
provenance
origin
issuer
producer
authority_ref
created_at
verified_at
```

---

# REQUIRED NO-ADMISSION TEST

The service must expose no:

```text
admit
approve
promote
authorize
register
trust
```

A `True` result must remain a Boolean equality fact only.

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

# REQUIRED FILESYSTEM-ABSENCE TEST

Calling the service must create no files or directories.

The test should:

1. change into an empty temporary directory
2. capture directory contents
3. call a valid match
4. call a valid mismatch
5. capture directory contents again
6. assert equality

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
log
logger
notification
alert
audit_event
verification_event
mismatch_event
```

Source checks should avoid accidental matches inside required explanatory strings, if any.

---

# REQUIRED NO-EXPORT-OR-TRANSPORT TEST

The service must expose no:

```text
export
publish
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

The service must reject top-level:

```text
list
tuple
set
frozenset
dictionary
```

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

The service must expose no:

```text
verify_signature
load_key
certificate
attestation
signer
```

```text
Digest Match
≠
Signature Validity
```

---

# REQUIRED FROZEN HASHER PRESERVATION

The frozen digest-manifest SHA-256 service must remain verification-unaware.

Its source must not gain:

```text
verify_digest
compare_digest
expected_digest
matches
is_valid
```

---

# REQUIRED INSPECTION-REPORT HASHER PRESERVATION

The frozen inspection-report SHA-256 service must remain generation-only.

Its source must not gain verification behavior.

---

# REQUIRED MANIFEST-MODEL PRESERVATION

The frozen digest-manifest model must not gain:

```text
computed_digest
expected_digest
verified
matches
verification_status
verification_reason
verify
```

---

# REQUIRED PIPELINE PRESERVATION

The following frozen services must remain unchanged and verification-unaware:

```text
RuntimeRecordInspectionDigestManifestService
RuntimeRecordInspectionDigestManifestRepresentationService
RuntimeRecordInspectionDigestManifestJsonEncodingService
RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
RuntimeRecordInspectionDigestManifestSha256DigestService
```

---

# EXPECTED TEST-FIRST FAILURE

After the test module is created and before the production service exists, running:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest_digest_verification_service.py -q
```

must fail during collection with an error equivalent to:

```text
ModuleNotFoundError:
No module named 'services.runtime_record_inspection_digest_manifest_digest_verification_service'
```

This failure is required evidence that tests precede implementation.

---

# TEST-FIRST CHECKPOINT CONTENT

The test-first commit must contain only:

```text
docs/runtime_kernel/READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_DIGEST_VERIFICATION_TEST_CONTRACT_001.md
tests/runtime/test_runtime_record_inspection_digest_manifest_digest_verification_service.py
```

It must not contain:

```text
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
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
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest_digest_verification_service.py -q
```

All isolated tests must pass.

Then run:

```powershell
python -m pytest -q
```

The full suite must pass.

Current full-suite baseline:

```text
2643 passed
```

No existing test may be removed, weakened, skipped, or rewritten merely to accommodate implementation.

---

# PROHIBITED TEST SHORTCUTS

The tests must not:

```text
mock the production service itself
define the production class inside the test module
create a placeholder production module
skip the missing-module failure
accept string subclasses
accept partial error wording
collapse invalid syntax into mismatch
omit valid mismatch behavior
omit exact Boolean type
omit hmac.compare_digest delegation
allow comparison before validation
permit input normalization
omit deterministic equality
omit statelessness
omit source restrictions
omit frozen-upstream preservation
modify frozen production files
create production implementation before the test-first commit
```

---

# AUTHORIZED IMPLEMENTATION AFTER CHECKPOINT

Only after the test-first checkpoint is committed and pushed may the following file be created:

```text
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

The implementation must be the smallest code satisfying the frozen contract and executable tests.

No additional capability is authorized.

---

# TEST CONTRACT CONCLUSION

The executable test surface is frozen around:

```text
exact plain-string inputs
computed and expected semantic roles
string-subclass rejection
role-specific TypeError behavior
exact TypeError messages
lowercase 64-character SHA-256 syntax
role-specific ValueError behavior
exact ValueError messages
validation order
invalid syntax distinct from mismatch
valid match → True
valid mismatch → False
exact Boolean output
hmac.compare_digest delegation
no comparison before validation
no plain-equality ownership
no normalization
deterministic repeated output
cross-instance equality
stateless behavior
no digest generation
no bytes input
no manifest dependency
no embedded report-digest verification
no result model
no subject binding
no provenance verification
no admission
no trust
no filesystem effects
no persistence
no events or logging
no export or transport
no collection verification
no Merkle or hash-chain verification
no signature verification
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
Digest Generation
≠
Digest Verification
```

```text
Wrong Runtime Type
≠
Invalid Digest Syntax
```

```text
Invalid Digest Syntax
≠
Digest Mismatch
```

```text
Value Equality
≠
Constant-Time Digest Comparison
```

```text
Digest Match
≠
Integrity Admission
```

```text
Digest Match
≠
Trust
```

```text
Digest Match
≠
Subject Binding
```

```text
Digest Equality
≠
Complete Integrity Proof
```

```text
Digest Mismatch
≠
Tampering Proof
```

```text
Verification True
≠
Authority Granted
```

```text
Digest Match
≠
Publicly Disclosable
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
