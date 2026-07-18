from dataclasses import dataclass
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from services.runtime_record_inspection_digest_manifest_representation_service import (
    RuntimeRecordInspectionDigestManifestRepresentationService,
)


PRODUCTION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_representation_service.py"
)

EXPECTED_KEYS = [
    "manifest_schema_version",
    "digest_algorithm",
    "sha256_digest",
    "byte_length",
    "codec",
    "bom_present",
]

PROHIBITED_PUBLIC_METHODS = {
    "from_primitive_dict",
    "from_dict",
    "to_manifest",
    "build_manifest",
    "create_manifest",
    "to_json",
    "to_json_text",
    "to_bytes",
    "serialize",
    "encode",
    "hash",
    "digest",
    "verify",
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
    "parse",
    "deserialize",
}

EXPECTED_ERROR = (
    "manifest must be an exact "
    "RuntimeRecordInspectionDigestManifest"
)


class DerivedString(str):
    pass


@dataclass(frozen=True)
class DerivedManifest(RuntimeRecordInspectionDigestManifest):
    pass


@dataclass(frozen=True)
class UnrelatedDataclass:
    manifest_schema_version: str
    digest_algorithm: str
    sha256_digest: str
    byte_length: int
    codec: str
    bom_present: bool


class DuckTypedManifest:
    manifest_schema_version = "1.0"
    digest_algorithm = "sha256"
    sha256_digest = "b" * 64
    byte_length = 257
    codec = "utf-8"
    bom_present = False


class ExplodingDuckTypedManifest:
    @property
    def manifest_schema_version(self) -> str:
        raise AssertionError("manifest fields must not be accessed")

    @property
    def digest_algorithm(self) -> str:
        raise AssertionError("manifest fields must not be accessed")

    @property
    def sha256_digest(self) -> str:
        raise AssertionError("manifest fields must not be accessed")

    @property
    def byte_length(self) -> int:
        raise AssertionError("manifest fields must not be accessed")

    @property
    def codec(self) -> str:
        raise AssertionError("manifest fields must not be accessed")

    @property
    def bom_present(self) -> bool:
        raise AssertionError("manifest fields must not be accessed")


@pytest.fixture
def manifest() -> RuntimeRecordInspectionDigestManifest:
    return RuntimeRecordInspectionDigestManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest="b" * 64,
        byte_length=257,
        codec="utf-8",
        bom_present=False,
    )


@pytest.fixture
def service() -> RuntimeRecordInspectionDigestManifestRepresentationService:
    return RuntimeRecordInspectionDigestManifestRepresentationService()


def test_service_can_be_constructed() -> None:
    service = RuntimeRecordInspectionDigestManifestRepresentationService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestRepresentationService
    )


def test_service_instances_are_independent() -> None:
    first = RuntimeRecordInspectionDigestManifestRepresentationService()
    second = RuntimeRecordInspectionDigestManifestRepresentationService()

    assert first is not second


def test_service_constructor_requires_no_arguments() -> None:
    service = RuntimeRecordInspectionDigestManifestRepresentationService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestRepresentationService
    )


def test_service_exposes_required_method(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
) -> None:
    assert callable(service.to_primitive_dict)


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_service_exposes_no_prohibited_public_method(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    method_name: str,
) -> None:
    assert not hasattr(service, method_name)


def test_valid_exact_manifest_is_accepted(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert type(result) is dict


@pytest.mark.parametrize(
    "invalid_manifest",
    [
        None,
        True,
        False,
        0,
        1,
        "manifest",
        b"manifest",
        [],
        (),
        {},
        object(),
        UnrelatedDataclass(
            manifest_schema_version="1.0",
            digest_algorithm="sha256",
            sha256_digest="b" * 64,
            byte_length=257,
            codec="utf-8",
            bom_present=False,
        ),
        DuckTypedManifest(),
        ExplodingDuckTypedManifest(),
    ],
)
def test_non_exact_manifest_values_are_rejected(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    invalid_manifest: object,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_primitive_dict(invalid_manifest)  # type: ignore[arg-type]


def test_manifest_subclass_is_rejected(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
) -> None:
    derived = DerivedManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest="c" * 64,
        byte_length=512,
        codec="utf-8",
        bom_present=False,
    )

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_primitive_dict(derived)


def test_runtime_record_inspection_report_is_rejected(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
) -> None:
    invalid_report = object.__new__(RuntimeRecordInspectionReport)

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_primitive_dict(invalid_report)


def test_invalid_input_is_rejected_before_field_access(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_primitive_dict(  # type: ignore[arg-type]
            ExplodingDuckTypedManifest()
        )


def test_result_is_exact_plain_dict(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert type(result) is dict


def test_result_contains_exact_key_count(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert len(result) == 6


def test_result_contains_exact_key_set(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert set(result) == set(EXPECTED_KEYS)


def test_result_preserves_exact_insertion_order(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert list(result.keys()) == EXPECTED_KEYS


def test_result_maps_every_value_directly(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert result == {
        "manifest_schema_version": manifest.manifest_schema_version,
        "digest_algorithm": manifest.digest_algorithm,
        "sha256_digest": manifest.sha256_digest,
        "byte_length": manifest.byte_length,
        "codec": manifest.codec,
        "bom_present": manifest.bom_present,
    }


def test_result_preserves_exact_value_types(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    result = service.to_primitive_dict(manifest)

    assert type(result["manifest_schema_version"]) is str
    assert type(result["digest_algorithm"]) is str
    assert type(result["sha256_digest"]) is str
    assert type(result["byte_length"]) is int
    assert type(result["codec"]) is str
    assert type(result["bom_present"]) is bool


def test_repeated_calls_return_equal_but_distinct_dicts(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    first = service.to_primitive_dict(manifest)
    second = service.to_primitive_dict(manifest)

    assert first == second
    assert first is not second


def test_result_mutation_is_isolated(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    first = service.to_primitive_dict(manifest)
    second = service.to_primitive_dict(manifest)

    first["sha256_digest"] = "0" * 64
    first["byte_length"] = 0

    third = service.to_primitive_dict(manifest)

    assert second["sha256_digest"] == "b" * 64
    assert second["byte_length"] == 257
    assert third["sha256_digest"] == "b" * 64
    assert third["byte_length"] == 257
    assert manifest.sha256_digest == "b" * 64
    assert manifest.byte_length == 257


def test_manifest_is_not_mutated(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    before = (
        manifest.manifest_schema_version,
        manifest.digest_algorithm,
        manifest.sha256_digest,
        manifest.byte_length,
        manifest.codec,
        manifest.bom_present,
    )

    service.to_primitive_dict(manifest)

    after = (
        manifest.manifest_schema_version,
        manifest.digest_algorithm,
        manifest.sha256_digest,
        manifest.byte_length,
        manifest.codec,
        manifest.bom_present,
    )

    assert after == before


def test_service_owns_no_mutable_instance_state(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    assert service.__dict__ == {}

    service.to_primitive_dict(manifest)

    assert service.__dict__ == {}


def test_independent_services_return_equal_results(
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    first_service = (
        RuntimeRecordInspectionDigestManifestRepresentationService()
    )
    second_service = (
        RuntimeRecordInspectionDigestManifestRepresentationService()
    )

    assert (
        first_service.to_primitive_dict(manifest)
        == second_service.to_primitive_dict(manifest)
    )


def test_prior_result_mutation_does_not_change_future_results(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> None:
    first = service.to_primitive_dict(manifest)
    first.clear()

    second = service.to_primitive_dict(manifest)

    assert list(second.keys()) == EXPECTED_KEYS
    assert second["sha256_digest"] == "b" * 64
    assert second["byte_length"] == 257


def test_representation_creates_no_files(
    service: RuntimeRecordInspectionDigestManifestRepresentationService,
    manifest: RuntimeRecordInspectionDigestManifest,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_primitive_dict(manifest)

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_contains_required_manifest_import() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert (
        "from models.runtime_record_inspection_digest_manifest import"
        in source
    )
    assert "RuntimeRecordInspectionDigestManifest" in source


def test_production_source_contains_exact_type_check() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert (
        "type(manifest) is not RuntimeRecordInspectionDigestManifest"
        in source
    )


def test_production_source_contains_exact_error_message() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert (
        "manifest must be an exact "
        in source
    )
    assert "RuntimeRecordInspectionDigestManifest" in source


def test_production_source_contains_no_prohibited_imports() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import json",
        "from json",
        "import pathlib",
        "from pathlib",
        "import os",
        "from os",
        "import tempfile",
        "from tempfile",
        "import hashlib",
        "from hashlib",
        "import datetime",
        "from datetime",
        "import time",
        "from time",
        "import random",
        "from random",
        "import uuid",
        "from uuid",
        "import secrets",
        "from secrets",
        "import dataclasses",
        "from dataclasses",
        "runtime_record_registry",
        "runtime_record_inspector",
        "event_engine",
        "runtime_record_inspection_json_encoding_service",
        "runtime_record_inspection_utf8_byte_encoding_service",
        "runtime_record_inspection_sha256_digest_service",
        "runtime_record_inspection_digest_manifest_service",
        "requests",
        "urllib",
        "http.client",
        "socket",
        "aiohttp",
        "manifest_registry",
        "artifact_registry",
        "platform_registry",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_automatic_conversion() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "dataclasses.asdict",
        "asdict(",
        "dataclasses.fields",
        "fields(",
        "vars(",
        ".__dict__",
        "getattr(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_current_time_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source
    assert "time.time" not in source


def test_production_source_contains_no_random_or_identifier_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "random" not in source
    assert "uuid" not in source
    assert "secrets" not in source


def test_production_source_contains_no_json_serialization() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "json.dumps",
        "json.dump",
        "to_json",
        "to_json_text",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_byte_encoding() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        ".encode(",
        "bytes(",
        "bytearray(",
        "memoryview(",
        "utf-8-sig",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_hashing() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib",
        "sha256(",
        "hexdigest(",
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


def test_manifest_model_still_exposes_no_representation_methods() -> None:
    prohibited_methods = {
        "to_dict",
        "to_primitive",
        "to_json",
        "to_json_text",
        "to_bytes",
        "serialize",
        "encode",
        "save",
        "persist",
        "export",
    }

    for method_name in prohibited_methods:
        assert not hasattr(
            RuntimeRecordInspectionDigestManifest,
            method_name,
        )


def test_existing_representation_service_remains_manifest_unaware() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_representation_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "RuntimeRecordInspectionDigestManifest" not in source
    assert "runtime_record_inspection_digest_manifest" not in source