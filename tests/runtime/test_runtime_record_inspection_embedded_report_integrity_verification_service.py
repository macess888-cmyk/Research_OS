import hashlib
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


PRODUCTION_PATH = (
    Path("services")
    / "runtime_record_inspection_embedded_report_integrity_verification_service.py"
)

RESULT_MODEL_PATH = (
    Path("models")
    / "runtime_record_inspection_embedded_report_integrity_verification_result.py"
)

MANIFEST_MODEL_PATH = (
    Path("models")
    / "runtime_record_inspection_digest_manifest.py"
)

MANIFEST_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_service.py"
)

REPRESENTATION_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_representation_service.py"
)

JSON_ENCODING_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_json_encoding_service.py"
)

UTF8_BYTE_ENCODING_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_utf8_byte_encoding_service.py"
)

SHA256_DIGEST_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_sha256_digest_service.py"
)

DIGEST_MANIFEST_VERIFICATION_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_digest_verification_service.py"
)

EMPTY_REPORT_BYTES = b""
REPORT_BYTES = b'{"status":"PASS"}'
DIFFERENT_REPORT_BYTES = b'{"status":"FAIL"}'
BINARY_REPORT_BYTES = b"\x00\xff\x01"
BOM_REPORT_BYTES = b"\xef\xbb\xbf" + REPORT_BYTES

REPORT_BYTES_TYPE_ERROR = "report_bytes must be an exact bytes"
MANIFEST_TYPE_ERROR = (
    "manifest must be an exact RuntimeRecordInspectionDigestManifest"
)

PROHIBITED_PUBLIC_METHODS = {
    "verify",
    "verify_report",
    "verify_digest",
    "verify_manifest",
    "verify_bytes",
    "compare",
    "compare_digest",
    "calculate_digest",
    "calculate_length",
    "inspect_bom",
    "decode",
    "parse",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "publish",
    "upload",
    "download",
    "register",
    "inspect",
    "health",
    "status",
    "verify_collection",
    "create_receipt",
    "admit",
    "approve",
    "trust",
    "authorize",
}


class DerivedBytes(bytes):
    pass


class DerivedManifest(RuntimeRecordInspectionDigestManifest):
    pass


class DuckManifest:
    manifest_schema_version = "1.0"
    digest_algorithm = "sha256"
    sha256_digest = "a" * 64
    byte_length = 0
    codec = "utf-8"
    bom_present = False


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


@pytest.fixture
def service() -> RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService:
    return RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()


def test_service_can_be_constructed() -> None:
    service = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
    )

    assert (
        type(service)
        is RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
    )


def test_service_instances_are_independent() -> None:
    first = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
    )
    second = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
    )

    assert first is not second


def test_constructor_requires_no_arguments() -> None:
    service = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
    )

    assert (
        type(service)
        is RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
    )


def test_service_exposes_verify_integrity(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    assert callable(service.verify_integrity)


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_service_exposes_no_prohibited_public_method(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    method_name: str,
) -> None:
    assert not hasattr(service, method_name)


@pytest.mark.parametrize(
    "report_bytes",
    [
        EMPTY_REPORT_BYTES,
        REPORT_BYTES,
        DIFFERENT_REPORT_BYTES,
        BINARY_REPORT_BYTES,
        b"\x00",
        b"\xff",
        b"\xef\xbb",
        b"\xef\xbb\xbf",
        BOM_REPORT_BYTES,
    ],
)
def test_exact_bytes_values_are_accepted(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    report_bytes: bytes,
) -> None:
    manifest = make_manifest(report_bytes)

    result = service.verify_integrity(
        report_bytes,
        manifest,
    )

    assert (
        type(result)
        is RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
    )


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        True,
        False,
        0,
        1,
        1.5,
        "",
        "report",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        {},
        object(),
        Path("report.json"),
        DuckManifest(),
    ],
)
def test_invalid_report_bytes_types_are_rejected(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    invalid_value: object,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    with pytest.raises(
        TypeError,
        match=f"^{REPORT_BYTES_TYPE_ERROR}$",
    ):
        service.verify_integrity(  # type: ignore[arg-type]
            invalid_value,
            manifest,
        )


def test_report_bytes_subclass_is_rejected(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    with pytest.raises(
        TypeError,
        match=f"^{REPORT_BYTES_TYPE_ERROR}$",
    ):
        service.verify_integrity(
            DerivedBytes(REPORT_BYTES),
            manifest,
        )


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        True,
        False,
        0,
        1,
        1.5,
        "",
        b"",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        {},
        object(),
        Path("manifest.json"),
        DuckManifest(),
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=True,
            byte_length_matches=True,
            bom_matches=True,
        ),
    ],
)
def test_invalid_manifest_types_are_rejected(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{MANIFEST_TYPE_ERROR}$",
    ):
        service.verify_integrity(  # type: ignore[arg-type]
            REPORT_BYTES,
            invalid_value,
        )


def test_manifest_subclass_is_rejected(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = DerivedManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest=hashlib.sha256(REPORT_BYTES).hexdigest(),
        byte_length=len(REPORT_BYTES),
        codec="utf-8",
        bom_present=False,
    )

    with pytest.raises(
        TypeError,
        match=f"^{MANIFEST_TYPE_ERROR}$",
    ):
        service.verify_integrity(
            REPORT_BYTES,
            manifest,
        )


def test_report_bytes_type_validation_occurs_first(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{REPORT_BYTES_TYPE_ERROR}$",
    ):
        service.verify_integrity(  # type: ignore[arg-type]
            None,
            None,
        )


def test_no_measurement_for_invalid_report_bytes(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    with (
        patch(
            "services."
            "runtime_record_inspection_embedded_report_integrity_verification_service."
            "hashlib.sha256",
        ) as sha256,
        patch(
            "services."
            "runtime_record_inspection_embedded_report_integrity_verification_service."
            "hmac.compare_digest",
        ) as compare_digest,
    ):
        with pytest.raises(TypeError):
            service.verify_integrity(  # type: ignore[arg-type]
                None,
                None,
            )

    sha256.assert_not_called()
    compare_digest.assert_not_called()


def test_no_measurement_for_invalid_manifest(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    with (
        patch(
            "services."
            "runtime_record_inspection_embedded_report_integrity_verification_service."
            "hashlib.sha256",
        ) as sha256,
        patch(
            "services."
            "runtime_record_inspection_embedded_report_integrity_verification_service."
            "hmac.compare_digest",
        ) as compare_digest,
    ):
        with pytest.raises(TypeError):
            service.verify_integrity(  # type: ignore[arg-type]
                REPORT_BYTES,
                None,
            )

    sha256.assert_not_called()
    compare_digest.assert_not_called()


def test_empty_bytes_full_match(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(EMPTY_REPORT_BYTES)

    result = service.verify_integrity(
        EMPTY_REPORT_BYTES,
        manifest,
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is True
    assert result.bom_matches is True
    assert result.integrity_matches is True


@pytest.mark.parametrize(
    "report_bytes",
    [
        b"\x00",
        b"\xff",
        BINARY_REPORT_BYTES,
        b"\xef\xbb",
        b"\xef\xbb\xbf",
    ],
)
def test_arbitrary_bytes_do_not_require_decoding(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    report_bytes: bytes,
) -> None:
    manifest = make_manifest(report_bytes)

    result = service.verify_integrity(
        report_bytes,
        manifest,
    )

    assert type(result.digest_matches) is bool
    assert type(result.byte_length_matches) is bool
    assert type(result.bom_matches) is bool


def test_sha256_receives_exact_report_bytes(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    with patch(
        "services."
        "runtime_record_inspection_embedded_report_integrity_verification_service."
        "hashlib.sha256",
    ) as sha256:
        hash_object = sha256.return_value
        hash_object.hexdigest.return_value = manifest.sha256_digest

        service.verify_integrity(
            REPORT_BYTES,
            manifest,
        )

    sha256.assert_called_once_with(REPORT_BYTES)
    hash_object.hexdigest.assert_called_once_with()


def test_compare_digest_receives_computed_and_manifest_digests(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)
    computed_digest = "a" * 64

    with (
        patch(
            "services."
            "runtime_record_inspection_embedded_report_integrity_verification_service."
            "hashlib.sha256",
        ) as sha256,
        patch(
            "services."
            "runtime_record_inspection_embedded_report_integrity_verification_service."
            "hmac.compare_digest",
            return_value=True,
        ) as compare_digest,
    ):
        sha256.return_value.hexdigest.return_value = computed_digest

        result = service.verify_integrity(
            REPORT_BYTES,
            manifest,
        )

    compare_digest.assert_called_once_with(
        computed_digest,
        manifest.sha256_digest,
    )
    assert result.digest_matches is True


def test_compare_digest_false_is_propagated(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

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

    compare_digest.assert_called_once()
    assert result.digest_matches is False


def test_full_match(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    result = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is True
    assert result.bom_matches is True
    assert result.integrity_matches is True


def test_digest_only_mismatch(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(
        REPORT_BYTES,
        sha256_digest="0" * 64,
    )

    result = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert result.digest_matches is False
    assert result.byte_length_matches is True
    assert result.bom_matches is True
    assert result.integrity_matches is False


def test_length_only_mismatch(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(
        REPORT_BYTES,
        byte_length=len(REPORT_BYTES) + 1,
    )

    result = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is False
    assert result.bom_matches is True
    assert result.integrity_matches is False


def test_bom_only_mismatch(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(
        BOM_REPORT_BYTES,
        bom_present=False,
    )

    result = service.verify_integrity(
        BOM_REPORT_BYTES,
        manifest,
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is True
    assert result.bom_matches is False
    assert result.integrity_matches is False


@pytest.mark.parametrize(
    "report_bytes,expected_bom_matches",
    [
        (b"", True),
        (b"\xef", True),
        (b"\xef\xbb", True),
        (b"\xef\xbb\xbf", False),
        (b"\xef\xbb\xbfabc", False),
        (b"x\xef\xbb\xbf", True),
        (b"abc\xef\xbb\xbf", True),
    ],
)
def test_bom_prefix_observation(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    report_bytes: bytes,
    expected_bom_matches: bool,
) -> None:
    manifest = make_manifest(
        report_bytes,
        bom_present=False,
    )

    result = service.verify_integrity(
        report_bytes,
        manifest,
    )

    assert result.bom_matches is expected_bom_matches


@pytest.mark.parametrize(
    "sha256_digest,byte_length,report_bytes,expected",
    [
        (
            "0" * 64,
            len(REPORT_BYTES) + 1,
            REPORT_BYTES,
            (False, False, True),
        ),
        (
            "0" * 64,
            len(BOM_REPORT_BYTES),
            BOM_REPORT_BYTES,
            (False, True, False),
        ),
        (
            hashlib.sha256(BOM_REPORT_BYTES).hexdigest(),
            len(BOM_REPORT_BYTES) + 1,
            BOM_REPORT_BYTES,
            (True, False, False),
        ),
        (
            "0" * 64,
            len(BOM_REPORT_BYTES) + 1,
            BOM_REPORT_BYTES,
            (False, False, False),
        ),
    ],
)
def test_multiple_mismatch_combinations(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    sha256_digest: str,
    byte_length: int,
    report_bytes: bytes,
    expected: tuple[bool, bool, bool],
) -> None:
    manifest = make_manifest(
        report_bytes,
        sha256_digest=sha256_digest,
        byte_length=byte_length,
        bom_present=False,
    )

    result = service.verify_integrity(
        report_bytes,
        manifest,
    )

    assert (
        result.digest_matches,
        result.byte_length_matches,
        result.bom_matches,
    ) == expected
    assert result.integrity_matches is False


def test_exact_result_type(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    result = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert (
        type(result)
        is RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
    )


def test_result_contains_no_codec_fact(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    result = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert not hasattr(result, "codec")
    assert not hasattr(result, "codec_matches")


def test_repeated_calls_are_deterministic(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    first = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )
    second = service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert first == second
    assert first is not second


def test_cross_instance_results_are_deterministic() -> None:
    first_service = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
    )
    second_service = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
    )
    manifest = make_manifest(REPORT_BYTES)

    first = first_service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )
    second = second_service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert first == second


def test_service_is_stateless_before_and_after_full_match(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(REPORT_BYTES)

    assert service.__dict__ == {}

    service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert service.__dict__ == {}


def test_service_is_stateless_after_mismatch(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    manifest = make_manifest(
        REPORT_BYTES,
        sha256_digest="0" * 64,
    )

    service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )

    assert service.__dict__ == {}


def test_service_is_stateless_after_invalid_input(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    with pytest.raises(TypeError):
        service.verify_integrity(  # type: ignore[arg-type]
            None,
            None,
        )

    assert service.__dict__ == {}


def test_prior_mismatch_does_not_affect_later_match(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    mismatch_manifest = make_manifest(
        REPORT_BYTES,
        sha256_digest="0" * 64,
    )
    matching_manifest = make_manifest(REPORT_BYTES)

    service.verify_integrity(
        REPORT_BYTES,
        mismatch_manifest,
    )

    result = service.verify_integrity(
        REPORT_BYTES,
        matching_manifest,
    )

    assert result.integrity_matches is True


def test_prior_match_does_not_affect_later_mismatch(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
) -> None:
    matching_manifest = make_manifest(REPORT_BYTES)
    mismatch_manifest = make_manifest(
        REPORT_BYTES,
        byte_length=len(REPORT_BYTES) + 1,
    )

    service.verify_integrity(
        REPORT_BYTES,
        matching_manifest,
    )

    result = service.verify_integrity(
        REPORT_BYTES,
        mismatch_manifest,
    )

    assert result.integrity_matches is False


def test_verification_creates_no_files(
    service: RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = make_manifest(REPORT_BYTES)
    mismatch_manifest = make_manifest(
        REPORT_BYTES,
        sha256_digest="0" * 64,
    )

    monkeypatch.chdir(tmp_path)

    before = sorted(
        path.relative_to(tmp_path)
        for path in tmp_path.rglob("*")
    )

    service.verify_integrity(
        REPORT_BYTES,
        manifest,
    )
    service.verify_integrity(
        REPORT_BYTES,
        mismatch_manifest,
    )

    after = sorted(
        path.relative_to(tmp_path)
        for path in tmp_path.rglob("*")
    )

    assert after == before


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_contains_exact_imports() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "import hashlib" in source
    assert "import hmac" in source
    assert (
        "from models.runtime_record_inspection_digest_manifest import ("
        in source
    )
    assert (
        "from models."
        "runtime_record_inspection_embedded_report_integrity_verification_result "
        "import ("
        in source
    )


def test_production_source_contains_exact_type_checks() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "type(report_bytes) is not bytes" in source
    assert (
        "type(manifest) is not RuntimeRecordInspectionDigestManifest"
        in source
    )
    assert "isinstance(report_bytes, bytes)" not in source
    assert (
        "isinstance(manifest, RuntimeRecordInspectionDigestManifest)"
        not in source
    )


def test_production_source_contains_exact_error_messages() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert REPORT_BYTES_TYPE_ERROR in source
    assert MANIFEST_TYPE_ERROR in source


def test_production_source_contains_sha256_measurement() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "hashlib.sha256(" in source
    assert ".hexdigest()" in source


def test_production_source_contains_constant_time_comparison() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "hmac.compare_digest(" in source
    assert "hmac.new" not in source
    assert "hmac.digest" not in source
    assert "digestmod" not in source


def test_production_source_contains_length_comparison() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "len(report_bytes)" in source
    assert "manifest.byte_length" in source


def test_production_source_contains_bom_observation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "report_bytes.startswith(" in source
    assert r'b"\xef\xbb\xbf"' in source
    assert "manifest.bom_present" in source


def test_production_source_constructs_exact_result() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert (
        "RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult("
        in source
    )
    assert "digest_matches=digest_matches" in source
    assert "byte_length_matches=byte_length_matches" in source
    assert "bom_matches=bom_matches" in source
    assert "integrity_matches=" not in source


def test_production_source_contains_no_codec_check() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "codec_matches",
        "report_bytes.decode(",
        "manifest.codec",
        'decode("utf-8")',
        "decode('utf-8')",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_parsing() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "json.loads",
        "json.dumps",
        "from_dict",
        "from_json",
        "RuntimeRecordInspectionRepresentationService",
        "RuntimeRecordInspectionJsonEncodingService",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_upstream_service_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "RuntimeRecordInspectionSha256DigestService",
        "RuntimeRecordInspectionDigestManifestDigestVerificationService",
        "RuntimeRecordInspectionDigestManifestService",
        "RuntimeRecordInspectionUtf8ByteEncodingService",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_prohibited_dependencies() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
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
        "import json",
        "from json",
        "import codecs",
        "from codecs",
        "import io",
        "from io",
        "import sqlite3",
        "import requests",
        "import urllib",
        "import socket",
        "Inspectable",
        "EventEngine",
        "RuntimeRecordRegistry",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_filesystem_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "open(",
        "Path(",
        "write_text",
        "write_bytes",
        "mkdir",
        "touch(",
        "unlink(",
        "rename(",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_time_or_identifier_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "datetime.now",
        "datetime.utcnow",
        "time.time",
        "uuid",
        "random",
        "secrets",
        "verification_id",
        "result_id",
        "created_at",
        "verified_at",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_event_or_logging_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "publish",
        "emit",
        "logger",
        "notification",
        "alert",
        "audit_event",
        "verification_event",
        "mismatch_event",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_export_or_transport_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "export",
        "upload",
        "download",
        "stream",
        "send",
        "transfer",
        "socket",
        "requests",
        "urllib",
        "http.client",
        "aiohttp",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_collection_or_merkle_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "verify_collection",
        "verify_batch",
        "compare_many",
        "merkle",
        "hash_chain",
        "digest_chain",
        "aggregate_digest",
        "collection_digest",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_production_source_contains_no_signature_verification() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited = [
        "verify_signature",
        "load_key",
        "certificate",
        "attestation",
        "signer",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_result_model_remains_measurement_unaware() -> None:
    source = RESULT_MODEL_PATH.read_text(encoding="utf-8")

    prohibited = [
        "hashlib",
        "hmac",
        "report_bytes",
        "manifest",
        "computed_digest",
        "verify_integrity",
        "len(",
        "startswith(",
    ]

    for fragment in prohibited:
        assert fragment not in source


def test_manifest_model_remains_verification_unaware() -> None:
    source = MANIFEST_MODEL_PATH.read_text(encoding="utf-8")

    prohibited = [
        "verify_integrity",
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
        "integrity_matches",
        "report_bytes",
    ]

    for fragment in prohibited:
        assert fragment not in source


@pytest.mark.parametrize(
    "path",
    [
        MANIFEST_SERVICE_PATH,
        REPRESENTATION_SERVICE_PATH,
        JSON_ENCODING_SERVICE_PATH,
        UTF8_BYTE_ENCODING_SERVICE_PATH,
        SHA256_DIGEST_SERVICE_PATH,
        DIGEST_MANIFEST_VERIFICATION_SERVICE_PATH,
    ],
)
def test_frozen_upstream_services_remain_embedded_integrity_unaware(
    path: Path,
) -> None:
    source = path.read_text(encoding="utf-8")

    prohibited = [
        "RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService",
        "verify_integrity",
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
        "integrity_matches",
    ]

    for fragment in prohibited:
        assert fragment not in source