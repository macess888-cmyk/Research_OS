from dataclasses import FrozenInstanceError, fields
from pathlib import Path

import pytest

from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)


PRODUCTION_PATH = (
    Path("models")
    / "runtime_record_inspection_embedded_report_integrity_verification_result.py"
)

DIGEST_MANIFEST_MODEL_PATH = (
    Path("models")
    / "runtime_record_inspection_digest_manifest.py"
)

DIGEST_MANIFEST_SERVICE_PATH = (
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

DIGEST_TYPE_ERROR = "digest_matches must be an exact bool"
BYTE_LENGTH_TYPE_ERROR = "byte_length_matches must be an exact bool"
BOM_TYPE_ERROR = "bom_matches must be an exact bool"

PROHIBITED_PUBLIC_METHODS = {
    "verify",
    "verify_again",
    "recalculate",
    "calculate_digest",
    "calculate_length",
    "inspect_bom",
    "save",
    "load",
    "persist",
    "publish",
    "export",
    "register",
    "admit",
    "approve",
    "trust",
    "authorize",
    "to_json",
    "to_bytes",
    "from_dict",
    "from_json",
}

PROHIBITED_FIELDS = {
    "integrity_matches",
    "report_bytes",
    "manifest",
    "computed_digest",
    "expected_digest",
    "observed_byte_length",
    "expected_byte_length",
    "observed_bom_present",
    "expected_bom_present",
    "codec",
    "codec_matches",
    "timestamp",
    "created_at",
    "verified_at",
    "identifier",
    "result_id",
    "verification_id",
    "subject_id",
    "record_id",
    "manifest_id",
    "registry_ref",
    "source_ref",
    "provenance",
    "path",
    "authority",
    "admission_status",
    "trust_status",
    "reason",
    "message",
    "error",
}

INVALID_BOOLEAN_VALUES = [
    None,
    0,
    1,
    -1,
    1.0,
    "true",
    "false",
    b"",
    bytearray(),
    memoryview(b""),
    [],
    (),
    set(),
    frozenset(),
    {},
    object(),
    Path("result.txt"),
]

BOOLEAN_COMBINATIONS = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (True, False, False),
    (False, True, True),
    (False, True, False),
    (False, False, True),
    (False, False, False),
]


def make_result(
    *,
    digest_matches: bool = True,
    byte_length_matches: bool = True,
    bom_matches: bool = True,
) -> RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult:
    return RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
        digest_matches=digest_matches,
        byte_length_matches=byte_length_matches,
        bom_matches=bom_matches,
    )


def test_result_can_be_constructed() -> None:
    result = make_result()

    assert (
        type(result)
        is RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
    )


def test_result_instances_are_independent() -> None:
    first = make_result()
    second = make_result()

    assert first is not second


def test_exact_field_order() -> None:
    field_names = [
        field.name
        for field in fields(
            RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
        )
    ]

    assert field_names == [
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    ]


def test_exact_field_annotations() -> None:
    assert (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
        .__annotations__
        == {
            "digest_matches": bool,
            "byte_length_matches": bool,
            "bom_matches": bool,
        }
    )


@pytest.mark.parametrize(
    "missing_field",
    [
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    ],
)
def test_all_fields_are_required(
    missing_field: str,
) -> None:
    arguments = {
        "digest_matches": True,
        "byte_length_matches": True,
        "bom_matches": True,
    }
    del arguments[missing_field]

    with pytest.raises(TypeError):
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            **arguments,
        )


@pytest.mark.parametrize(
    "digest_matches,byte_length_matches,bom_matches",
    BOOLEAN_COMBINATIONS,
)
def test_all_boolean_combinations_are_accepted(
    digest_matches: bool,
    byte_length_matches: bool,
    bom_matches: bool,
) -> None:
    result = make_result(
        digest_matches=digest_matches,
        byte_length_matches=byte_length_matches,
        bom_matches=bom_matches,
    )

    assert result.digest_matches is digest_matches
    assert result.byte_length_matches is byte_length_matches
    assert result.bom_matches is bom_matches


@pytest.mark.parametrize(
    "invalid_value",
    INVALID_BOOLEAN_VALUES,
)
def test_digest_matches_rejects_non_exact_bool(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{DIGEST_TYPE_ERROR}$",
    ):
        make_result(
            digest_matches=invalid_value,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "invalid_value",
    INVALID_BOOLEAN_VALUES,
)
def test_byte_length_matches_rejects_non_exact_bool(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{BYTE_LENGTH_TYPE_ERROR}$",
    ):
        make_result(
            byte_length_matches=invalid_value,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "invalid_value",
    INVALID_BOOLEAN_VALUES,
)
def test_bom_matches_rejects_non_exact_bool(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match=f"^{BOM_TYPE_ERROR}$",
    ):
        make_result(
            bom_matches=invalid_value,  # type: ignore[arg-type]
        )


def test_validation_order_checks_digest_matches_first() -> None:
    with pytest.raises(
        TypeError,
        match=f"^{DIGEST_TYPE_ERROR}$",
    ):
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=None,  # type: ignore[arg-type]
            byte_length_matches=None,  # type: ignore[arg-type]
            bom_matches=None,  # type: ignore[arg-type]
        )


def test_validation_order_checks_byte_length_matches_second() -> None:
    with pytest.raises(
        TypeError,
        match=f"^{BYTE_LENGTH_TYPE_ERROR}$",
    ):
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=True,
            byte_length_matches=None,  # type: ignore[arg-type]
            bom_matches=None,  # type: ignore[arg-type]
        )


def test_validation_order_checks_bom_matches_third() -> None:
    with pytest.raises(
        TypeError,
        match=f"^{BOM_TYPE_ERROR}$",
    ):
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=True,
            byte_length_matches=True,
            bom_matches=None,  # type: ignore[arg-type]
        )


def test_integer_zero_is_not_coerced_to_false() -> None:
    with pytest.raises(TypeError):
        make_result(
            digest_matches=0,  # type: ignore[arg-type]
        )


def test_integer_one_is_not_coerced_to_true() -> None:
    with pytest.raises(TypeError):
        make_result(
            digest_matches=1,  # type: ignore[arg-type]
        )


def test_full_match_derives_true() -> None:
    result = make_result(
        digest_matches=True,
        byte_length_matches=True,
        bom_matches=True,
    )

    assert result.integrity_matches is True
    assert type(result.integrity_matches) is bool


@pytest.mark.parametrize(
    "digest_matches,byte_length_matches,bom_matches",
    [
        combination
        for combination in BOOLEAN_COMBINATIONS
        if combination != (True, True, True)
    ],
)
def test_every_mismatch_combination_derives_false(
    digest_matches: bool,
    byte_length_matches: bool,
    bom_matches: bool,
) -> None:
    result = make_result(
        digest_matches=digest_matches,
        byte_length_matches=byte_length_matches,
        bom_matches=bom_matches,
    )

    assert result.integrity_matches is False
    assert type(result.integrity_matches) is bool


@pytest.mark.parametrize(
    "digest_matches,byte_length_matches,bom_matches",
    BOOLEAN_COMBINATIONS,
)
def test_integrity_matches_is_directly_derived(
    digest_matches: bool,
    byte_length_matches: bool,
    bom_matches: bool,
) -> None:
    result = make_result(
        digest_matches=digest_matches,
        byte_length_matches=byte_length_matches,
        bom_matches=bom_matches,
    )

    expected = (
        result.digest_matches
        and result.byte_length_matches
        and result.bom_matches
    )

    assert result.integrity_matches is expected


def test_integrity_matches_is_not_constructor_argument() -> None:
    with pytest.raises(TypeError):
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=True,
            byte_length_matches=True,
            bom_matches=True,
            integrity_matches=True,  # type: ignore[call-arg]
        )


def test_integrity_matches_is_not_stored() -> None:
    result = make_result()

    assert result.__dict__ == {
        "digest_matches": True,
        "byte_length_matches": True,
        "bom_matches": True,
    }
    assert "integrity_matches" not in result.__dict__


def test_integrity_matches_is_a_property() -> None:
    descriptor = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
        .__dict__["integrity_matches"]
    )

    assert type(descriptor) is property


def test_integrity_matches_has_no_setter() -> None:
    descriptor = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
        .__dict__["integrity_matches"]
    )

    assert descriptor.fset is None


def test_integrity_matches_assignment_fails() -> None:
    result = make_result()

    with pytest.raises(
        (FrozenInstanceError, AttributeError),
    ):
        result.integrity_matches = False  # type: ignore[misc]


@pytest.mark.parametrize(
    "field_name",
    [
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    ],
)
def test_stored_fields_are_immutable(
    field_name: str,
) -> None:
    result = make_result()

    with pytest.raises(FrozenInstanceError):
        setattr(result, field_name, False)


def test_equal_results_compare_equal() -> None:
    first = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )
    second = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )

    assert first == second
    assert first is not second


@pytest.mark.parametrize(
    "field_name",
    [
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    ],
)
def test_results_compare_unequal_when_one_field_differs(
    field_name: str,
) -> None:
    baseline_arguments = {
        "digest_matches": True,
        "byte_length_matches": True,
        "bom_matches": True,
    }
    changed_arguments = dict(baseline_arguments)
    changed_arguments[field_name] = False

    baseline = make_result(**baseline_arguments)
    changed = make_result(**changed_arguments)

    assert baseline != changed


def test_result_is_hashable() -> None:
    first = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )
    second = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )

    assert hash(first) == hash(second)
    assert len({first, second}) == 1


def test_standard_representation_contains_stored_fields() -> None:
    result = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )

    representation = repr(result)

    assert (
        "RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult"
        in representation
    )
    assert "digest_matches=False" in representation
    assert "byte_length_matches=True" in representation
    assert "bom_matches=False" in representation
    assert "integrity_matches=" not in representation


def test_result_exposes_required_public_facts() -> None:
    result = make_result()

    assert hasattr(result, "digest_matches")
    assert hasattr(result, "byte_length_matches")
    assert hasattr(result, "bom_matches")
    assert hasattr(result, "integrity_matches")


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_result_exposes_no_prohibited_public_method(
    method_name: str,
) -> None:
    result = make_result()

    assert not hasattr(result, method_name)


@pytest.mark.parametrize(
    "field_name",
    sorted(PROHIBITED_FIELDS),
)
def test_result_exposes_no_prohibited_field(
    field_name: str,
) -> None:
    result = make_result()

    if field_name == "integrity_matches":
        assert field_name not in result.__dict__
    else:
        assert not hasattr(result, field_name)


def test_result_contains_no_codec_fact() -> None:
    result = make_result()

    assert not hasattr(result, "codec")
    assert not hasattr(result, "codec_matches")


def test_result_retains_no_subject() -> None:
    result = make_result()

    prohibited = [
        "report_bytes",
        "manifest",
        "report",
        "record",
        "artifact",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_retains_no_digest_value() -> None:
    result = make_result()

    prohibited = [
        "computed_digest",
        "expected_digest",
        "sha256_digest",
        "digest_algorithm",
        "hash_object",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_retains_no_length_values() -> None:
    result = make_result()

    prohibited = [
        "observed_byte_length",
        "expected_byte_length",
        "byte_length_difference",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_retains_no_bom_values() -> None:
    result = make_result()

    prohibited = [
        "observed_bom_present",
        "expected_bom_present",
        "bom_bytes",
        "byte_prefix",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_retains_no_time() -> None:
    result = make_result()

    assert not hasattr(result, "timestamp")
    assert not hasattr(result, "created_at")
    assert not hasattr(result, "verified_at")


def test_result_retains_no_identifier() -> None:
    result = make_result()

    prohibited = [
        "identifier",
        "result_id",
        "verification_id",
        "subject_id",
        "record_id",
        "manifest_id",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_retains_no_provenance() -> None:
    result = make_result()

    prohibited = [
        "provenance",
        "origin",
        "issuer",
        "producer",
        "custody",
        "lineage",
        "source_ref",
        "registry_ref",
        "authority_ref",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_exposes_no_admission_state() -> None:
    result = make_result()

    prohibited = [
        "admit",
        "admitted",
        "approve",
        "approved",
        "promote",
        "promoted",
        "register",
        "registered",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_exposes_no_trust_state() -> None:
    result = make_result()

    prohibited = [
        "trust",
        "trusted",
        "authentic",
        "safe",
        "authoritative",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_result_exposes_no_authority_state() -> None:
    result = make_result()

    prohibited = [
        "authorize",
        "authorized",
        "authority",
        "permission",
        "execute",
        "publish_permission",
        "export_permission",
    ]

    for name in prohibited:
        assert not hasattr(result, name)


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_imports_only_dataclass() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")
    import_lines = [
        line.strip()
        for line in source.splitlines()
        if line.strip().startswith(("import ", "from "))
    ]

    assert import_lines == [
        "from dataclasses import dataclass",
    ]


def test_production_source_contains_frozen_dataclass() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "@dataclass(frozen=True)" in source
    assert (
        "class "
        "RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult:"
        in source
    )


def test_production_source_contains_exact_fields() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "digest_matches: bool" in source
    assert "byte_length_matches: bool" in source
    assert "bom_matches: bool" in source
    assert "integrity_matches: bool" not in source


def test_production_source_contains_exact_type_checks() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "type(self.digest_matches) is not bool" in source
    assert "type(self.byte_length_matches) is not bool" in source
    assert "type(self.bom_matches) is not bool" in source

    assert "bool(self.digest_matches)" not in source
    assert "bool(self.byte_length_matches)" not in source
    assert "bool(self.bom_matches)" not in source


def test_production_source_contains_exact_error_messages() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert DIGEST_TYPE_ERROR in source
    assert BYTE_LENGTH_TYPE_ERROR in source
    assert BOM_TYPE_ERROR in source


def test_production_source_contains_derived_property() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "@property" in source
    assert "def integrity_matches(self) -> bool:" in source
    assert "self.digest_matches" in source
    assert "self.byte_length_matches" in source
    assert "self.bom_matches" in source


def test_production_source_does_not_store_aggregate() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "integrity_matches: bool" not in source
    assert "self.integrity_matches =" not in source
    assert '"integrity_matches"' not in source
    assert "'integrity_matches'" not in source


def test_production_source_contains_no_prohibited_imports() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import hashlib",
        "import hmac",
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
        "import sqlite3",
        "import requests",
        "import urllib",
        "import socket",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_performs_no_comparison_execution() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib.sha256",
        "hmac.compare_digest",
        "len(",
        "startswith(",
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


def test_model_construction_creates_no_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)

    before = sorted(
        path.relative_to(tmp_path)
        for path in tmp_path.rglob("*")
    )

    make_result()

    after = sorted(
        path.relative_to(tmp_path)
        for path in tmp_path.rglob("*")
    )

    assert after == before


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
        "result_id",
        "verification_id",
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


def test_production_source_contains_no_export_or_transport_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
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

    for fragment in prohibited_fragments:
        assert fragment not in source


@pytest.mark.parametrize(
    "path",
    [
        DIGEST_MANIFEST_MODEL_PATH,
        DIGEST_MANIFEST_SERVICE_PATH,
        REPRESENTATION_SERVICE_PATH,
        JSON_ENCODING_SERVICE_PATH,
        UTF8_BYTE_ENCODING_SERVICE_PATH,
        SHA256_DIGEST_SERVICE_PATH,
        DIGEST_MANIFEST_VERIFICATION_SERVICE_PATH,
    ],
)
def test_frozen_upstream_components_remain_result_unaware(
    path: Path,
) -> None:
    source = path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult",
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
        "integrity_matches",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source