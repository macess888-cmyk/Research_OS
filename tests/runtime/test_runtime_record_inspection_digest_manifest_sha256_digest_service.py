import hashlib
from dataclasses import fields
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from services.runtime_record_inspection_digest_manifest_sha256_digest_service import (
    RuntimeRecordInspectionDigestManifestSha256DigestService,
)


PRODUCTION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_sha256_digest_service.py"
)

EXISTING_HASHER_PATH = (
    Path("services")
    / "runtime_record_inspection_sha256_digest_service.py"
)

MANIFEST_BYTE_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py"
)

MANIFEST_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_service.py"
)

MANIFEST_REPRESENTATION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_representation_service.py"
)

MANIFEST_JSON_ENCODER_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_json_encoding_service.py"
)

EXPECTED_ERROR = "content_bytes must be an exact bytes"

REPRESENTATIVE_CONTENT_BYTES = (
    b'{"manifest_schema_version":"1.0",'
    b'"digest_algorithm":"sha256",'
    b'"sha256_digest":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",'
    b'"byte_length":128,'
    b'"codec":"utf-8",'
    b'"bom_present":false}'
)

EXPECTED_ABC_DIGEST = (
    "ba7816bf8f01cfea414140de5dae2223"
    "b00361a396177a9cb410ff61f20015ad"
)

EXPECTED_MANIFEST_FIELDS = (
    "manifest_schema_version",
    "digest_algorithm",
    "sha256_digest",
    "byte_length",
    "codec",
    "bom_present",
)

PROHIBITED_PUBLIC_METHODS = {
    "hash",
    "digest",
    "to_digest",
    "to_raw_digest",
    "verify",
    "verify_digest",
    "compare_digest",
    "matches",
    "is_valid",
    "sign",
    "verify_signature",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "publish",
    "upload",
    "download",
    "inspect",
    "health",
    "status",
    "hash_collection",
    "to_merkle_root",
    "create_manifest",
    "build_manifest",
    "to_utf8_bytes",
    "to_json_text",
    "to_primitive_dict",
    "content_address",
    "register",
}


class DerivedBytes(bytes):
    pass


class ExplodingByteLike:
    def __bytes__(self) -> bytes:
        raise AssertionError("invalid input must not be converted")

    def __iter__(self):
        raise AssertionError("invalid input must not be traversed")


@pytest.fixture
def content_bytes() -> bytes:
    return REPRESENTATIVE_CONTENT_BYTES


@pytest.fixture
def service() -> RuntimeRecordInspectionDigestManifestSha256DigestService:
    return RuntimeRecordInspectionDigestManifestSha256DigestService()


def test_service_can_be_constructed() -> None:
    service = RuntimeRecordInspectionDigestManifestSha256DigestService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestSha256DigestService
    )


def test_service_instances_are_independent() -> None:
    first = RuntimeRecordInspectionDigestManifestSha256DigestService()
    second = RuntimeRecordInspectionDigestManifestSha256DigestService()

    assert first is not second


def test_service_constructor_requires_no_arguments() -> None:
    service = RuntimeRecordInspectionDigestManifestSha256DigestService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestSha256DigestService
    )


def test_service_exposes_required_method(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    assert callable(service.to_sha256_hexdigest)


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_service_exposes_no_prohibited_public_method(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    method_name: str,
) -> None:
    assert not hasattr(service, method_name)


def test_exact_plain_bytes_are_accepted(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert type(result) is str


@pytest.mark.parametrize(
    "invalid_content",
    [
        None,
        True,
        False,
        0,
        1,
        1.5,
        "",
        "abc",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        {},
        object(),
        Path("manifest.json"),
        [b"abc"],
        (b"abc",),
        hashlib.sha256(),
        ExplodingByteLike(),
    ],
)
def test_non_exact_bytes_values_are_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    invalid_content: object,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(  # type: ignore[arg-type]
            invalid_content
        )


def test_bytes_subclass_is_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(DerivedBytes(content_bytes))


def test_bytearray_is_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(  # type: ignore[arg-type]
            bytearray(content_bytes)
        )


def test_memoryview_is_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(  # type: ignore[arg-type]
            memoryview(content_bytes)
        )


def test_manifest_model_is_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    manifest = RuntimeRecordInspectionDigestManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest="a" * 64,
        byte_length=128,
        codec="utf-8",
        bom_present=False,
    )

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(manifest)  # type: ignore[arg-type]


def test_manifest_primitive_dictionary_is_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    primitive = {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": "a" * 64,
        "byte_length": 128,
        "codec": "utf-8",
        "bom_present": False,
    }

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(primitive)  # type: ignore[arg-type]


def test_manifest_json_text_is_rejected(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    json_text = REPRESENTATIVE_CONTENT_BYTES.decode("utf-8")

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(json_text)  # type: ignore[arg-type]


def test_invalid_input_is_rejected_before_conversion(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_sha256_hexdigest(  # type: ignore[arg-type]
            ExplodingByteLike()
        )


def test_result_is_exact_string(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert type(result) is str


def test_matches_exact_hashlib_sha256_hexdigest(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert result == hashlib.sha256(content_bytes).hexdigest()


def test_representative_manifest_bytes_hash_exactly(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert result == hashlib.sha256(content_bytes).hexdigest()
    assert len(result) == 64
    assert result == result.lower()
    assert not result.endswith("\n")
    assert not result.endswith("\r")


def test_empty_bytes_hash_exactly(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    assert service.to_sha256_hexdigest(b"") == (
        hashlib.sha256(b"").hexdigest()
    )


def test_known_abc_sha256_vector(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    assert service.to_sha256_hexdigest(b"abc") == EXPECTED_ABC_DIGEST


@pytest.mark.parametrize(
    "value",
    [
        b"\x00",
        b"\xff",
        b"\x00\xff\x10",
        b"not-json",
        b" leading",
        b"trailing ",
        b"a\nb",
        b"a\r\nb",
        b"\xef\xbb\xbftext",
    ],
)
def test_arbitrary_bytes_hash_exactly(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    value: bytes,
) -> None:
    assert service.to_sha256_hexdigest(value) == (
        hashlib.sha256(value).hexdigest()
    )


def test_null_byte_hashes_exactly(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    assert service.to_sha256_hexdigest(b"\x00") == (
        hashlib.sha256(b"\x00").hexdigest()
    )


def test_result_contains_only_lowercase_hexadecimal(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert result == result.lower()
    assert all(character in "0123456789abcdef" for character in result)


def test_result_has_exact_length(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert len(result) == 64


def test_result_contains_no_prefix(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert not result.startswith("sha256:")
    assert not result.startswith("SHA256:")
    assert not result.startswith("0x")


def test_result_contains_no_trailing_newline(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert not result.endswith("\n")
    assert not result.endswith("\r")


def test_result_is_not_raw_digest_bytes(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content_bytes)

    assert result != hashlib.sha256(content_bytes).digest()
    assert type(result) is str


def test_repeated_calls_are_deterministic(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    first = service.to_sha256_hexdigest(content_bytes)
    second = service.to_sha256_hexdigest(content_bytes)

    assert first == second


def test_independent_services_return_equal_results(
    content_bytes: bytes,
) -> None:
    first = RuntimeRecordInspectionDigestManifestSha256DigestService()
    second = RuntimeRecordInspectionDigestManifestSha256DigestService()

    assert first.to_sha256_hexdigest(content_bytes) == (
        second.to_sha256_hexdigest(content_bytes)
    )


def test_service_owns_no_mutable_instance_state(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    assert service.__dict__ == {}

    service.to_sha256_hexdigest(content_bytes)

    assert service.__dict__ == {}


def test_prior_call_does_not_affect_later_output(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
) -> None:
    service.to_sha256_hexdigest(b"previous")

    result = service.to_sha256_hexdigest(content_bytes)

    assert result == hashlib.sha256(content_bytes).hexdigest()


def test_semantic_digest_subject_is_not_validated(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
) -> None:
    for value in (b"", b"not-json", b"\xff"):
        assert service.to_sha256_hexdigest(value) == (
            hashlib.sha256(value).hexdigest()
        )


def test_hashing_creates_no_files(
    service: RuntimeRecordInspectionDigestManifestSha256DigestService,
    content_bytes: bytes,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_sha256_hexdigest(content_bytes)

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_imports_only_hashlib() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")
    import_lines = [
        line.strip()
        for line in source.splitlines()
        if line.strip().startswith(("import ", "from "))
    ]

    assert import_lines == ["import hashlib"]


def test_production_source_contains_exact_type_check() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "type(content_bytes) is not bytes" in source
    assert "isinstance(content_bytes, bytes)" not in source


def test_production_source_contains_exact_error_message() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert EXPECTED_ERROR in source


def test_production_source_contains_exact_hash_operation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "hashlib.sha256(" in source
    assert ").hexdigest()" in source
    assert "hashlib.new" not in source
    assert ".digest()" not in source


def test_production_source_contains_no_existing_hasher_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "RuntimeRecordInspectionSha256DigestService" not in source
    assert "runtime_record_inspection_sha256_digest_service" not in source


def test_production_source_contains_no_byte_service_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert (
        "RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService"
        not in source
    )
    assert (
        "runtime_record_inspection_digest_manifest_utf8_byte_encoding_service"
        not in source
    )


def test_production_source_contains_no_manifest_model_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "from models" not in source
    assert (
        "runtime_record_inspection_digest_manifest import"
        not in source
    )


def test_production_source_contains_no_prohibited_dependencies() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "from models",
        "from services",
        "import pathlib",
        "from pathlib",
        "import os",
        "from os",
        "import sys",
        "from sys",
        "import tempfile",
        "from tempfile",
        "import datetime",
        "from datetime",
        "import time",
        "from time",
        "import uuid",
        "from uuid",
        "import random",
        "from random",
        "import secrets",
        "from secrets",
        "import hmac",
        "from hmac",
        "import json",
        "from json",
        "import codecs",
        "from codecs",
        "import io",
        "from io",
        "import gzip",
        "import zlib",
        "import bz2",
        "import lzma",
        "import socket",
        "import requests",
        "import urllib",
        "import sqlite3",
        "RuntimeRecordInspectionSha256DigestService",
        "RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService",
        "RuntimeRecordRegistry",
        "RuntimeRecordInspector",
        "Inspectable",
        "EventEngine",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_algorithm_selection() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib.new",
        "algorithm_name",
        "hash_name",
        "selected_algorithm",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_salt_key_or_hmac() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hmac",
        "salt",
        "nonce",
        "pepper",
        "secret",
        "key=",
        "digestmod",
        "pbkdf",
        "scrypt",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_verification() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "verify",
        "verify_digest",
        "compare_digest",
        "matches",
        "is_valid",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_embedded_report_verification() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "sha256_digest",
        "byte_length",
        "bom_present",
        "inspection_report",
        "report_bytes",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_content_addressing() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "content_address",
        "artifact_id",
        "manifest_id",
        "digest_id",
        "registry_key",
        "storage_path",
        "file_name",
        "dedup",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_filesystem_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "open(",
        "Path(",
        "write_text",
        "write_bytes",
        "mkdir",
        "touch(",
        "unlink(",
        "rename(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_time_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source
    assert "time.time" not in source


def test_production_source_contains_no_identifier_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "uuid",
        "random",
        "secrets",
        "manifest_id",
        "artifact_id",
        "digest_id",
        "hashed_at",
        "created_at",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_framing_or_compression() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "length_prefix",
        "delimiter",
        "record_separator",
        "framing",
        "gzip",
        "zlib",
        "bz2",
        "lzma",
        "brotli",
        "zipfile",
        "compress",
        "decompress",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_existing_hasher_remains_digest_manifest_unaware() -> None:
    source = EXISTING_HASHER_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "RuntimeRecordInspectionDigestManifest",
        "RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService",
        "RuntimeRecordInspectionDigestManifestSha256DigestService",
        "digest_manifest",
        "manifest_hash",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_byte_service_remains_hash_unaware() -> None:
    source = MANIFEST_BYTE_SERVICE_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import hashlib",
        "hashlib.sha256",
        "hexdigest",
        "to_sha256_hexdigest",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_model_remains_exactly_six_fields() -> None:
    assert tuple(
        field.name
        for field in fields(RuntimeRecordInspectionDigestManifest)
    ) == EXPECTED_MANIFEST_FIELDS


def test_manifest_model_remains_self_digest_free() -> None:
    prohibited_attributes = {
        "manifest_sha256_digest",
        "digest_manifest_sha256_digest",
        "manifest_hash",
        "self_digest",
        "content_address",
        "to_sha256_hexdigest",
        "hash_self",
        "verify_self",
    }

    for attribute_name in prohibited_attributes:
        assert not hasattr(
            RuntimeRecordInspectionDigestManifest,
            attribute_name,
        )


def test_manifest_service_remains_hash_unaware() -> None:
    source = MANIFEST_SERVICE_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib",
        "sha256(",
        "hexdigest(",
        "manifest_hash",
        "self_digest",
        "content_address",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


@pytest.mark.parametrize(
    "path",
    [
        MANIFEST_REPRESENTATION_PATH,
        MANIFEST_JSON_ENCODER_PATH,
    ],
)
def test_representation_and_json_services_remain_hash_unaware(
    path: Path,
) -> None:
    source = path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib",
        "sha256(",
        "hexdigest(",
        "manifest_hash",
        "self_digest",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source