from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from services.runtime_record_inspection_digest_manifest_service import (
    RuntimeRecordInspectionDigestManifestService,
)


VALID_DIGEST = (
    "e3b0c44298fc1c149afbf4c8996fb924"
    "27ae41e4649b934ca495991b7852b855"
)

PROHIBITED_METHODS = {
    "build",
    "generate",
    "derive",
    "calculate",
    "calculate_digest",
    "calculate_byte_length",
    "verify",
    "verify_digest",
    "verify_byte_length",
    "matches",
    "compare",
    "serialize",
    "to_dict",
    "to_json",
    "encode",
    "hash_manifest",
    "sign",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "register",
    "publish",
    "inspect",
    "health",
    "status",
}


@pytest.fixture
def service() -> RuntimeRecordInspectionDigestManifestService:
    return RuntimeRecordInspectionDigestManifestService()


def valid_arguments() -> dict[str, object]:
    return {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": VALID_DIGEST,
        "byte_length": 0,
        "codec": "utf-8",
        "bom_present": False,
    }


def test_service_constructs_without_arguments() -> None:
    service = RuntimeRecordInspectionDigestManifestService()

    assert type(service) is RuntimeRecordInspectionDigestManifestService


def test_service_has_no_required_state() -> None:
    first = RuntimeRecordInspectionDigestManifestService()
    second = RuntimeRecordInspectionDigestManifestService()

    assert vars(first) == {}
    assert vars(second) == {}


def test_create_manifest_returns_exact_model_type(
    service: RuntimeRecordInspectionDigestManifestService,
) -> None:
    result = service.create_manifest(**valid_arguments())  # type: ignore[arg-type]

    assert type(result) is RuntimeRecordInspectionDigestManifest


def test_create_manifest_propagates_all_fields_exactly(
    service: RuntimeRecordInspectionDigestManifestService,
) -> None:
    arguments = valid_arguments()
    arguments["byte_length"] = 123

    result = service.create_manifest(**arguments)  # type: ignore[arg-type]

    assert result.manifest_schema_version == "1.0"
    assert result.digest_algorithm == "sha256"
    assert result.sha256_digest == VALID_DIGEST
    assert result.byte_length == 123
    assert result.codec == "utf-8"
    assert result.bom_present is False


def test_create_manifest_requires_keyword_only_arguments(
    service: RuntimeRecordInspectionDigestManifestService,
) -> None:
    with pytest.raises(TypeError):
        service.create_manifest(  # type: ignore[misc]
            "1.0",
            "sha256",
            VALID_DIGEST,
            0,
            "utf-8",
            False,
        )


@pytest.mark.parametrize(
    "missing_name",
    [
        "manifest_schema_version",
        "digest_algorithm",
        "sha256_digest",
        "byte_length",
        "codec",
        "bom_present",
    ],
)
def test_create_manifest_rejects_missing_argument(
    service: RuntimeRecordInspectionDigestManifestService,
    missing_name: str,
) -> None:
    arguments = valid_arguments()
    del arguments[missing_name]

    with pytest.raises(TypeError):
        service.create_manifest(**arguments)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "extra_name",
    [
        "manifest_id",
        "artifact_id",
        "record_id",
        "created_at",
        "source_commit",
        "verified",
        "authorized",
        "public",
    ],
)
def test_create_manifest_rejects_extra_argument(
    service: RuntimeRecordInspectionDigestManifestService,
    extra_name: str,
) -> None:
    arguments = valid_arguments()
    arguments[extra_name] = "unexpected"

    with pytest.raises(TypeError):
        service.create_manifest(**arguments)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "field_name,invalid_value,error_type,error_message",
    [
        (
            "manifest_schema_version",
            None,
            TypeError,
            "manifest_schema_version must be an exact str",
        ),
        (
            "manifest_schema_version",
            "2.0",
            ValueError,
            "manifest_schema_version must be exactly '1.0'",
        ),
        (
            "digest_algorithm",
            None,
            TypeError,
            "digest_algorithm must be an exact str",
        ),
        (
            "digest_algorithm",
            "sha512",
            ValueError,
            "digest_algorithm must be exactly 'sha256'",
        ),
        (
            "sha256_digest",
            None,
            TypeError,
            "sha256_digest must be an exact str",
        ),
        (
            "sha256_digest",
            "invalid",
            ValueError,
            (
                "sha256_digest must be exactly 64 lowercase "
                "hexadecimal characters"
            ),
        ),
        (
            "byte_length",
            None,
            TypeError,
            "byte_length must be an exact int",
        ),
        (
            "byte_length",
            -1,
            ValueError,
            "byte_length must be non-negative",
        ),
        (
            "codec",
            None,
            TypeError,
            "codec must be an exact str",
        ),
        (
            "codec",
            "ascii",
            ValueError,
            "codec must be exactly 'utf-8'",
        ),
        (
            "bom_present",
            None,
            TypeError,
            "bom_present must be an exact bool",
        ),
        (
            "bom_present",
            True,
            ValueError,
            "bom_present must be False",
        ),
    ],
)
def test_service_propagates_model_validation_errors(
    service: RuntimeRecordInspectionDigestManifestService,
    field_name: str,
    invalid_value: object,
    error_type: type[Exception],
    error_message: str,
) -> None:
    arguments = valid_arguments()
    arguments[field_name] = invalid_value

    with pytest.raises(error_type, match=error_message):
        service.create_manifest(**arguments)  # type: ignore[arg-type]


def test_equal_arguments_produce_equal_manifests(
    service: RuntimeRecordInspectionDigestManifestService,
) -> None:
    first = service.create_manifest(**valid_arguments())  # type: ignore[arg-type]
    second = service.create_manifest(**valid_arguments())  # type: ignore[arg-type]

    assert first == second


def test_service_exposes_no_prohibited_methods(
    service: RuntimeRecordInspectionDigestManifestService,
) -> None:
    for method_name in PROHIBITED_METHODS:
        assert not hasattr(service, method_name)


def test_service_does_not_inherit_platform_inspectable() -> None:
    from src.services.inspectable import Inspectable

    assert not issubclass(
        RuntimeRecordInspectionDigestManifestService,
        Inspectable,
    )


def test_service_source_imports_only_manifest_model() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_digest_manifest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "runtime_record_inspection_digest_manifest" in source

    prohibited_fragments = [
        "import hashlib",
        "from hashlib",
        "import json",
        "from json",
        "import re",
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
        "runtime_record_inspection_sha256_digest_service",
        "runtime_record_inspection_utf8_byte_encoding_service",
        "runtime_record_inspection_json_encoding_service",
        "runtime_record_inspection_representation_service",
        "runtime_record_inspection_report",
        "runtime_record_inspector",
        "runtime_record_registry",
        "src.services.inspectable",
        "event_engine",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_service_source_contains_no_derivation() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_digest_manifest_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib",
        "sha256(",
        "hexdigest(",
        ".digest(",
        '.encode("utf-8")',
        ".decode(",
        "len(content_bytes)",
        "datetime.now",
        "datetime.utcnow",
        "uuid4",
        "setdefault(",
        ".lower(",
        ".strip(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_construction_creates_no_files(
    service: RuntimeRecordInspectionDigestManifestService,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.create_manifest(**valid_arguments())  # type: ignore[arg-type]

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before