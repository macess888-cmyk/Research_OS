import hashlib
from pathlib import Path

import pytest

from services.runtime_record_inspection_sha256_digest_service import (
    RuntimeRecordInspectionSha256DigestService,
)


PROHIBITED_METHODS = {
    "hash",
    "digest",
    "checksum",
    "fingerprint",
    "to_digest_bytes",
    "to_binary_digest",
    "verify",
    "matches",
    "compare",
    "sign",
    "validate",
    "to_manifest",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "update",
    "stream",
    "hash_stream",
    "hash_collection",
    "merkle_root",
    "redact",
    "mask",
    "classify",
    "publish",
    "upload",
    "download",
    "inspect",
    "health",
    "status",
}


@pytest.fixture
def service() -> RuntimeRecordInspectionSha256DigestService:
    return RuntimeRecordInspectionSha256DigestService()


def test_service_constructs_without_arguments() -> None:
    service = RuntimeRecordInspectionSha256DigestService()

    assert type(service) is RuntimeRecordInspectionSha256DigestService


def test_service_has_no_required_state() -> None:
    first = RuntimeRecordInspectionSha256DigestService()
    second = RuntimeRecordInspectionSha256DigestService()

    assert vars(first) == {}
    assert vars(second) == {}


@pytest.mark.parametrize(
    "invalid_content",
    [
        None,
        "",
        {},
        [],
        (),
        1,
        bytearray(b"abc"),
        memoryview(b"abc"),
        [b"abc"],
        (b"abc",),
    ],
)
def test_rejects_non_exact_bytes_inputs(
    service: RuntimeRecordInspectionSha256DigestService,
    invalid_content: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="content_bytes must be an exact bytes",
    ):
        service.to_sha256_hexdigest(invalid_content)  # type: ignore[arg-type]


def test_rejects_bytes_subclass(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    class DerivedBytes(bytes):
        pass

    with pytest.raises(
        TypeError,
        match="content_bytes must be an exact bytes",
    ):
        service.to_sha256_hexdigest(DerivedBytes(b"abc"))


def test_returns_exact_string(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    result = service.to_sha256_hexdigest(b"abc")

    assert type(result) is str


def test_matches_exact_hashlib_sha256_hexdigest(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    content = b'{"record_id":"RR-000000001"}'

    result = service.to_sha256_hexdigest(content)

    assert result == hashlib.sha256(content).hexdigest()


def test_empty_bytes_known_vector(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    assert service.to_sha256_hexdigest(b"") == (
        "e3b0c44298fc1c149afbf4c8996fb924"
        "27ae41e4649b934ca495991b7852b855"
    )


def test_abc_known_vector(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    assert service.to_sha256_hexdigest(b"abc") == (
        "ba7816bf8f01cfea414140de5dae2223"
        "b00361a396177a9cb410ff61f20015ad"
    )


@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"a",
        b"abc",
        b"\x00",
        b"\xff\x00\x01",
        bytes(range(256)),
    ],
)
def test_digest_is_exactly_64_characters(
    service: RuntimeRecordInspectionSha256DigestService,
    content: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content)

    assert len(result) == 64


@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"abc",
        b"Runtime inspection",
        b"\x00\x01\x02",
        bytes(range(256)),
    ],
)
def test_digest_contains_lowercase_hexadecimal_only(
    service: RuntimeRecordInspectionSha256DigestService,
    content: bytes,
) -> None:
    result = service.to_sha256_hexdigest(content)

    assert set(result) <= set("0123456789abcdef")


def test_digest_contains_no_uppercase_hexadecimal(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    result = service.to_sha256_hexdigest(b"abc")

    assert result == result.lower()


def test_digest_has_no_prefix(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    result = service.to_sha256_hexdigest(b"abc")

    assert not result.startswith("0x")
    assert not result.startswith("sha256:")
    assert not result.startswith("sha-256:")


def test_digest_contains_no_whitespace(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    result = service.to_sha256_hexdigest(b"abc")

    assert " " not in result
    assert "\t" not in result
    assert "\n" not in result
    assert "\r" not in result


def test_digest_contains_no_algorithm_metadata(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    result = service.to_sha256_hexdigest(b"abc")

    assert "sha" not in result
    assert ":" not in result


def test_repeated_calls_are_equal(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    content = b'{"value":"alpha"}'

    first = service.to_sha256_hexdigest(content)
    second = service.to_sha256_hexdigest(content)

    assert first == second


def test_two_service_instances_produce_equal_output() -> None:
    content = b'{"value":"alpha"}'
    first = RuntimeRecordInspectionSha256DigestService()
    second = RuntimeRecordInspectionSha256DigestService()

    assert first.to_sha256_hexdigest(content) == (
        second.to_sha256_hexdigest(content)
    )


def test_source_bytes_remain_unchanged(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    content = b"\x00Runtime\xff"
    before = content

    service.to_sha256_hexdigest(content)

    assert content == before


def test_output_is_not_binary_digest(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    result = service.to_sha256_hexdigest(b"abc")

    assert not isinstance(result, bytes)
    assert not isinstance(result, bytearray)
    assert not isinstance(result, memoryview)


@pytest.mark.parametrize(
    "collection",
    [
        [],
        (),
        [b"abc"],
        (b"abc",),
        [b"a", b"b"],
    ],
)
def test_rejects_collection_inputs(
    service: RuntimeRecordInspectionSha256DigestService,
    collection: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="content_bytes must be an exact bytes",
    ):
        service.to_sha256_hexdigest(collection)  # type: ignore[arg-type]


def test_service_exposes_no_prohibited_methods(
    service: RuntimeRecordInspectionSha256DigestService,
) -> None:
    for method_name in PROHIBITED_METHODS:
        assert not hasattr(service, method_name)


def test_service_does_not_inherit_platform_inspectable() -> None:
    from src.services.inspectable import Inspectable

    assert not issubclass(
        RuntimeRecordInspectionSha256DigestService,
        Inspectable,
    )


def test_production_source_uses_hashlib_sha256() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_sha256_digest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "import hashlib" in source
    assert "hashlib.sha256" in source
    assert ".hexdigest()" in source


def test_production_source_does_not_use_binary_digest() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_sha256_digest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert ".digest()" not in source


def test_production_source_contains_no_alternative_hash_algorithm() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_sha256_digest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_algorithms = [
        "hashlib.md5",
        "hashlib.sha1",
        "hashlib.sha224",
        "hashlib.sha384",
        "hashlib.sha512",
        "hashlib.blake2",
        "crc32",
        "hash(",
    ]

    for fragment in prohibited_algorithms:
        assert fragment not in source


def test_production_source_contains_only_expected_dependency() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_sha256_digest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import json",
        "from json",
        "import pathlib",
        "from pathlib",
        "import os",
        "from os",
        "import tempfile",
        "from tempfile",
        "import datetime",
        "from datetime",
        "import uuid",
        "import random",
        "import hmac",
        "import secrets",
        "import cryptography",
        "runtime_record_inspection_utf8_byte_encoding_service",
        "runtime_record_inspection_json_encoding_service",
        "runtime_record_inspection_representation_service",
        "runtime_record_inspection_report",
        "runtime_record_inspector",
        "runtime_record_registry",
        "src.services.inspectable",
        "event_engine",
        '.encode("utf-8")',
        ".decode(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_incremental_hashing() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_sha256_digest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert ".update(" not in source
    assert "hash_stream" not in source


def test_production_source_contains_no_current_time_generation() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_sha256_digest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source


def test_digest_generation_creates_no_files(
    service: RuntimeRecordInspectionSha256DigestService,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_sha256_hexdigest(b"abc")

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before