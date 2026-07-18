import hmac
from pathlib import Path
from unittest.mock import patch

import pytest

from services.runtime_record_inspection_digest_manifest_digest_verification_service import (
    RuntimeRecordInspectionDigestManifestDigestVerificationService,
)


PRODUCTION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_digest_verification_service.py"
)

MANIFEST_HASHER_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_sha256_digest_service.py"
)

INSPECTION_REPORT_HASHER_PATH = (
    Path("services")
    / "runtime_record_inspection_sha256_digest_service.py"
)

MANIFEST_MODEL_PATH = (
    Path("models")
    / "runtime_record_inspection_digest_manifest.py"
)

MANIFEST_SERVICE_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_service.py"
)

MANIFEST_REPRESENTATION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_representation_service.py"
)

MANIFEST_JSON_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_json_encoding_service.py"
)

MANIFEST_BYTE_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py"
)

MATCHING_DIGEST = (
    "ba7816bf8f01cfea414140de5dae2223"
    "b00361a396177a9cb410ff61f20015ad"
)

DIFFERENT_DIGEST = (
    "ca7816bf8f01cfea414140de5dae2223"
    "b00361a396177a9cb410ff61f20015ad"
)

COMPUTED_TYPE_ERROR = "computed_digest must be an exact str"
EXPECTED_TYPE_ERROR = "expected_digest must be an exact str"

COMPUTED_VALUE_ERROR = (
    "computed_digest must be a lowercase "
    "64-character SHA-256 hexadecimal string"
)

EXPECTED_VALUE_ERROR = (
    "expected_digest must be a lowercase "
    "64-character SHA-256 hexadecimal string"
)

PROHIBITED_PUBLIC_METHODS = {
    "compare",
    "compare_digests",
    "matches",
    "is_valid",
    "validate",
    "hash",
    "digest",
    "to_sha256_hexdigest",
    "verify_manifest",
    "verify_bytes",
    "verify_report_digest",
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
    "register",
    "inspect",
    "health",
    "status",
    "verify_collection",
    "create_receipt",
    "admit",
    "approve",
    "trust",
}


class DerivedString(str):
    pass


@pytest.fixture
def service() -> RuntimeRecordInspectionDigestManifestDigestVerificationService:
    return RuntimeRecordInspectionDigestManifestDigestVerificationService()


def test_service_can_be_constructed() -> None:
    service = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestDigestVerificationService
    )


def test_service_instances_are_independent() -> None:
    first = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )
    second = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )

    assert first is not second


def test_constructor_requires_no_arguments() -> None:
    service = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestDigestVerificationService
    )


def test_service_exposes_required_method(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    assert callable(service.verify_digest)


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_service_exposes_no_prohibited_public_method(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    method_name: str,
) -> None:
    assert not hasattr(service, method_name)


def test_valid_equal_digests_are_accepted(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    result = service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert result is True


def test_valid_unequal_digests_are_accepted(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    result = service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    assert result is False


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        True,
        False,
        0,
        1,
        1.5,
        b"",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        {},
        object(),
        Path("digest.txt"),
    ],
)
def test_invalid_computed_digest_types_are_rejected(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{COMPUTED_TYPE_ERROR}$",
    ):
        service.verify_digest(  # type: ignore[arg-type]
            invalid_value,
            MATCHING_DIGEST,
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
        b"",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        {},
        object(),
        Path("digest.txt"),
    ],
)
def test_invalid_expected_digest_types_are_rejected(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{EXPECTED_TYPE_ERROR}$",
    ):
        service.verify_digest(  # type: ignore[arg-type]
            MATCHING_DIGEST,
            invalid_value,
        )


def test_computed_digest_string_subclass_is_rejected(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{COMPUTED_TYPE_ERROR}$",
    ):
        service.verify_digest(
            DerivedString(MATCHING_DIGEST),
            MATCHING_DIGEST,
        )


def test_expected_digest_string_subclass_is_rejected(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{EXPECTED_TYPE_ERROR}$",
    ):
        service.verify_digest(
            MATCHING_DIGEST,
            DerivedString(MATCHING_DIGEST),
        )


def test_computed_type_validation_occurs_first(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{COMPUTED_TYPE_ERROR}$",
    ):
        service.verify_digest(  # type: ignore[arg-type]
            None,
            None,
        )


@pytest.mark.parametrize(
    "valid_digest",
    [
        "0" * 64,
        "f" * 64,
        "0123456789abcdef" * 4,
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    ],
)
def test_valid_sha256_hexadecimal_syntax_is_accepted(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    valid_digest: str,
) -> None:
    result = service.verify_digest(
        valid_digest,
        valid_digest,
    )

    assert result is True


@pytest.mark.parametrize(
    "invalid_digest",
    [
        "",
        "a" * 63,
        "a" * 65,
        "A" * 64,
        ("a" * 63) + "A",
        "sha256:" + ("a" * 64),
        "SHA256:" + ("a" * 64),
        "0x" + ("a" * 64),
        " " + ("a" * 63),
        ("a" * 63) + " ",
        ("a" * 31) + " " + ("a" * 32),
        ("a" * 31) + "\t" + ("a" * 32),
        ("a" * 63) + "\n",
        ("a" * 63) + "\r",
        ":".join(["a" * 16] * 4),
        "-".join(["a" * 16] * 4),
        ("a" * 63) + "g",
        ("a" * 63) + "é",
    ],
)
def test_invalid_computed_digest_syntax_is_rejected(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    invalid_digest: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=f"^{COMPUTED_VALUE_ERROR}$",
    ):
        service.verify_digest(
            invalid_digest,
            MATCHING_DIGEST,
        )


@pytest.mark.parametrize(
    "invalid_digest",
    [
        "",
        "a" * 63,
        "a" * 65,
        "A" * 64,
        ("a" * 63) + "A",
        "sha256:" + ("a" * 64),
        "SHA256:" + ("a" * 64),
        "0x" + ("a" * 64),
        " " + ("a" * 63),
        ("a" * 63) + " ",
        ("a" * 31) + " " + ("a" * 32),
        ("a" * 31) + "\t" + ("a" * 32),
        ("a" * 63) + "\n",
        ("a" * 63) + "\r",
        ":".join(["a" * 16] * 4),
        "-".join(["a" * 16] * 4),
        ("a" * 63) + "g",
        ("a" * 63) + "é",
    ],
)
def test_invalid_expected_digest_syntax_is_rejected(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    invalid_digest: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=f"^{EXPECTED_VALUE_ERROR}$",
    ):
        service.verify_digest(
            MATCHING_DIGEST,
            invalid_digest,
        )


def test_computed_syntax_validation_occurs_first(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with pytest.raises(
        ValueError,
        match=f"^{COMPUTED_VALUE_ERROR}$",
    ):
        service.verify_digest(
            "invalid",
            "invalid",
        )


def test_invalid_syntax_does_not_collapse_into_mismatch(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with pytest.raises(
        ValueError,
        match=f"^{COMPUTED_VALUE_ERROR}$",
    ):
        service.verify_digest(
            "invalid",
            MATCHING_DIGEST,
        )


def test_valid_mismatch_returns_false(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    result = service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    assert result is False
    assert type(result) is bool


def test_valid_match_returns_true(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    result = service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert result is True
    assert type(result) is bool


def test_result_is_exact_bool_for_match(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    result = service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert type(result) is bool


def test_result_is_exact_bool_for_mismatch(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    result = service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    assert type(result) is bool


def test_comparison_delegates_to_hmac_compare_digest(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with patch(
        "services."
        "runtime_record_inspection_digest_manifest_digest_verification_service."
        "hmac.compare_digest",
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


def test_compare_digest_return_value_is_returned_directly(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with patch(
        "services."
        "runtime_record_inspection_digest_manifest_digest_verification_service."
        "hmac.compare_digest",
        return_value=False,
    ) as compare_digest:
        result = service.verify_digest(
            MATCHING_DIGEST,
            MATCHING_DIGEST,
        )

    compare_digest.assert_called_once_with(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert result is False


def test_comparison_not_called_for_invalid_computed_type(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with patch(
        "services."
        "runtime_record_inspection_digest_manifest_digest_verification_service."
        "hmac.compare_digest",
    ) as compare_digest:
        with pytest.raises(TypeError):
            service.verify_digest(  # type: ignore[arg-type]
                None,
                MATCHING_DIGEST,
            )

    compare_digest.assert_not_called()


def test_comparison_not_called_for_invalid_expected_type(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with patch(
        "services."
        "runtime_record_inspection_digest_manifest_digest_verification_service."
        "hmac.compare_digest",
    ) as compare_digest:
        with pytest.raises(TypeError):
            service.verify_digest(  # type: ignore[arg-type]
                MATCHING_DIGEST,
                None,
            )

    compare_digest.assert_not_called()


def test_comparison_not_called_for_invalid_computed_syntax(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with patch(
        "services."
        "runtime_record_inspection_digest_manifest_digest_verification_service."
        "hmac.compare_digest",
    ) as compare_digest:
        with pytest.raises(ValueError):
            service.verify_digest(
                "invalid",
                MATCHING_DIGEST,
            )

    compare_digest.assert_not_called()


def test_comparison_not_called_for_invalid_expected_syntax(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with patch(
        "services."
        "runtime_record_inspection_digest_manifest_digest_verification_service."
        "hmac.compare_digest",
    ) as compare_digest:
        with pytest.raises(ValueError):
            service.verify_digest(
                MATCHING_DIGEST,
                "invalid",
            )

    compare_digest.assert_not_called()


@pytest.mark.parametrize(
    "computed_digest,expected_digest",
    [
        ("A" * 64, "a" * 64),
        (" " + ("a" * 63), "a" * 64),
        ("a" * 64, ("a" * 63) + " "),
        ("sha256:" + ("a" * 64), "a" * 64),
        ("0x" + ("a" * 64), "a" * 64),
        (("a" * 63) + "\n", "a" * 64),
        (":".join(["a" * 16] * 4), "a" * 64),
        ("-".join(["a" * 16] * 4), "a" * 64),
    ],
)
def test_invalid_values_are_rejected_without_normalization(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    computed_digest: str,
    expected_digest: str,
) -> None:
    with pytest.raises(ValueError):
        service.verify_digest(
            computed_digest,
            expected_digest,
        )


def test_repeated_match_calls_are_deterministic(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    first = service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )
    second = service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert first is True
    assert second is True
    assert first is second


def test_repeated_mismatch_calls_are_deterministic(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    first = service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )
    second = service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    assert first is False
    assert second is False
    assert first is second


def test_cross_instance_match_is_deterministic() -> None:
    first = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )
    second = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )

    assert first.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    ) is second.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )


def test_cross_instance_mismatch_is_deterministic() -> None:
    first = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )
    second = (
        RuntimeRecordInspectionDigestManifestDigestVerificationService()
    )

    assert first.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    ) is second.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )


def test_service_is_stateless_before_and_after_match(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    assert service.__dict__ == {}

    service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert service.__dict__ == {}


def test_service_is_stateless_before_and_after_mismatch(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    assert service.__dict__ == {}

    service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    assert service.__dict__ == {}


def test_service_is_stateless_after_rejected_input(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    with pytest.raises(ValueError):
        service.verify_digest(
            "invalid",
            MATCHING_DIGEST,
        )

    assert service.__dict__ == {}


def test_prior_mismatch_does_not_affect_later_match(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    assert service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    ) is True


def test_prior_match_does_not_affect_later_mismatch(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
) -> None:
    service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )

    assert service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    ) is False


def test_verification_creates_no_files(
    service: RuntimeRecordInspectionDigestManifestDigestVerificationService,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(
        path.relative_to(tmp_path)
        for path in tmp_path.rglob("*")
    )

    service.verify_digest(
        MATCHING_DIGEST,
        MATCHING_DIGEST,
    )
    service.verify_digest(
        MATCHING_DIGEST,
        DIFFERENT_DIGEST,
    )

    after = sorted(
        path.relative_to(tmp_path)
        for path in tmp_path.rglob("*")
    )

    assert after == before


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_imports_only_hmac() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")
    import_lines = [
        line.strip()
        for line in source.splitlines()
        if line.strip().startswith(("import ", "from "))
    ]

    assert import_lines == ["import hmac"]


def test_production_source_contains_exact_type_checks() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "type(computed_digest) is not str" in source
    assert "type(expected_digest) is not str" in source
    assert "isinstance(computed_digest, str)" not in source
    assert "isinstance(expected_digest, str)" not in source


def test_production_source_contains_exact_error_messages() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert COMPUTED_TYPE_ERROR in source
    assert EXPECTED_TYPE_ERROR in source
    assert COMPUTED_VALUE_ERROR in source
    assert EXPECTED_VALUE_ERROR in source


def test_production_source_contains_hmac_compare_digest() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "hmac.compare_digest(" in source
    assert "hmac.new" not in source
    assert "hmac.digest" not in source
    assert "digestmod" not in source


def test_production_source_contains_no_digest_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import hashlib",
        "hashlib.sha256",
        "hexdigest",
        "RuntimeRecordInspectionDigestManifestSha256DigestService",
        "runtime_record_inspection_digest_manifest_sha256_digest_service",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_manifest_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "from models" not in source
    assert "runtime_record_inspection_digest_manifest import" not in source


def test_production_source_contains_no_prohibited_dependencies() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import hashlib",
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
        "import json",
        "from json",
        "import codecs",
        "from codecs",
        "import io",
        "from io",
        "import socket",
        "import requests",
        "import urllib",
        "import sqlite3",
        "RuntimeRecordInspectionDigestManifestSha256DigestService",
        "RuntimeRecordRegistry",
        "RuntimeRecordInspector",
        "Inspectable",
        "EventEngine",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_hmac_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hmac.new",
        "hmac.digest",
        "digestmod",
        "key=",
        "secret",
        "nonce",
        "salt",
        "pepper",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_result_model() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "VerificationResult",
        "verification_receipt",
        "status_enum",
        "reason_model",
        "comparison_artifact",
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


def test_production_source_contains_no_subject_binding() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "manifest_id",
        "record_id",
        "subject_id",
        "source_ref",
        "registry_ref",
        "execution_ref",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_provenance() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "provenance",
        "issuer",
        "producer",
        "authority_ref",
        "created_at",
        "verified_at",
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
        "verification_id",
        "result_id",
        "created_at",
        "verified_at",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_event_or_logging_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "publish",
        "emit",
        "logger",
        "notification",
        "alert",
        "audit_event",
        "verification_event",
        "mismatch_event",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_collection_or_merkle_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "verify_collection",
        "verify_batch",
        "compare_many",
        "merkle",
        "hash_chain",
        "digest_chain",
        "aggregate_digest",
        "collection_digest",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_signature_verification() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "verify_signature",
        "load_key",
        "certificate",
        "attestation",
        "signer",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_hasher_remains_verification_unaware() -> None:
    source = MANIFEST_HASHER_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "verify_digest",
        "compare_digest",
        "expected_digest",
        "matches",
        "is_valid",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_inspection_report_hasher_remains_generation_only() -> None:
    source = INSPECTION_REPORT_HASHER_PATH.read_text(
        encoding="utf-8"
    )

    prohibited_fragments = [
        "verify_digest",
        "compare_digest",
        "expected_digest",
        "matches",
        "is_valid",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_model_remains_verification_unaware() -> None:
    source = MANIFEST_MODEL_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "computed_digest",
        "expected_digest",
        "verified",
        "matches",
        "verification_status",
        "verification_reason",
        "def verify",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


@pytest.mark.parametrize(
    "path",
    [
        MANIFEST_SERVICE_PATH,
        MANIFEST_REPRESENTATION_PATH,
        MANIFEST_JSON_PATH,
        MANIFEST_BYTE_PATH,
        MANIFEST_HASHER_PATH,
    ],
)
def test_frozen_pipeline_remains_verification_unaware(
    path: Path,
) -> None:
    source = path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "verify_digest",
        "compare_digest",
        "expected_digest",
        "verification_status",
        "verification_reason",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source