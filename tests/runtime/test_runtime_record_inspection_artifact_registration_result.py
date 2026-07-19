from dataclasses import (
    FrozenInstanceError,
    fields,
    is_dataclass,
)
from datetime import datetime, timezone
import importlib
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
)
from models.runtime_record_inspection_artifact_registration_result import (
    RuntimeRecordInspectionArtifactRegistrationResult,
)


RECORDED_AT = datetime(
    2026,
    7,
    19,
    12,
    0,
    tzinfo=timezone.utc,
)


def make_report(**overrides):
    values = {
        "record_id": "RR-000000001",
        "record_type": "RuntimeEventRecord",
        "record_category": "EVENT",
        "append_position": 1,
        "recorded_at": RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": "PRV-000000001",
        "external_id": None,
        "declared_fields": (
            ("event_type", "OBSERVED"),
            ("target_ref", None),
            ("actor_ref", None),
            ("source_ref", None),
            ("scope_ref", None),
            ("branch_ref", None),
            ("occurred_at", None),
            ("effective_at", None),
        ),
    }
    values.update(overrides)
    return RuntimeRecordInspectionReport(**values)


def make_manifest(**overrides):
    values = {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": "0" * 64,
        "byte_length": 0,
        "codec": "utf-8",
        "bom_present": False,
    }
    values.update(overrides)
    return RuntimeRecordInspectionDigestManifest(**values)


def make_report_artifact(**overrides):
    values = {
        "report_artifact_id": "RIRA-000000001",
        "report": make_report(),
    }
    values.update(overrides)
    return RuntimeRecordInspectionReportArtifact(**values)


def make_manifest_artifact(**overrides):
    values = {
        "manifest_artifact_id": "RIDMA-000000001",
        "manifest": make_manifest(),
    }
    values.update(overrides)
    return RuntimeRecordInspectionDigestManifestArtifact(**values)


def make_result(**overrides):
    candidate = make_report_artifact()

    values = {
        "artifact_kind": "REPORT",
        "artifact_id": candidate.report_artifact_id,
        "status": "REGISTERED",
        "existing_artifact": None,
        "candidate_artifact": candidate,
    }
    values.update(overrides)

    return RuntimeRecordInspectionArtifactRegistrationResult(
        **values
    )


def make_manifest_result(**overrides):
    candidate = make_manifest_artifact()

    values = {
        "artifact_kind": "DIGEST_MANIFEST",
        "artifact_id": candidate.manifest_artifact_id,
        "status": "REGISTERED",
        "existing_artifact": None,
        "candidate_artifact": candidate,
    }
    values.update(overrides)

    return RuntimeRecordInspectionArtifactRegistrationResult(
        **values
    )


def test_module_imports():
    module = importlib.import_module(
        "models.runtime_record_inspection_artifact_registration_result"
    )
    assert module is not None


def test_class_imports_from_selected_module():
    module = importlib.import_module(
        "models.runtime_record_inspection_artifact_registration_result"
    )

    assert (
        module.RuntimeRecordInspectionArtifactRegistrationResult
        is RuntimeRecordInspectionArtifactRegistrationResult
    )


def test_model_is_dataclass():
    assert is_dataclass(
        RuntimeRecordInspectionArtifactRegistrationResult
    )


def test_dataclass_field_order_is_exact():
    assert tuple(
        field.name
        for field in fields(
            RuntimeRecordInspectionArtifactRegistrationResult
        )
    ) == (
        "artifact_kind",
        "artifact_id",
        "status",
        "existing_artifact",
        "candidate_artifact",
    )


@pytest.mark.parametrize(
    "missing_field",
    [
        "artifact_kind",
        "artifact_id",
        "status",
        "existing_artifact",
        "candidate_artifact",
    ],
)
def test_constructor_requires_all_fields(missing_field):
    candidate = make_report_artifact()

    values = {
        "artifact_kind": "REPORT",
        "artifact_id": candidate.report_artifact_id,
        "status": "REGISTERED",
        "existing_artifact": None,
        "candidate_artifact": candidate,
    }
    values.pop(missing_field)

    with pytest.raises(TypeError):
        RuntimeRecordInspectionArtifactRegistrationResult(
            **values
        )


def test_positional_construction_is_supported():
    candidate = make_report_artifact()

    result = RuntimeRecordInspectionArtifactRegistrationResult(
        "REPORT",
        candidate.report_artifact_id,
        "REGISTERED",
        None,
        candidate,
    )

    assert result.artifact_kind == "REPORT"
    assert result.artifact_id == candidate.report_artifact_id
    assert result.status == "REGISTERED"
    assert result.existing_artifact is None
    assert result.candidate_artifact is candidate


def test_keyword_construction_is_supported():
    candidate = make_report_artifact()

    result = RuntimeRecordInspectionArtifactRegistrationResult(
        artifact_kind="REPORT",
        artifact_id=candidate.report_artifact_id,
        status="REGISTERED",
        existing_artifact=None,
        candidate_artifact=candidate,
    )

    assert result.candidate_artifact is candidate


@pytest.mark.parametrize(
    "artifact_kind",
    [
        "REPORT",
        "DIGEST_MANIFEST",
    ],
)
def test_valid_artifact_kinds_are_accepted(
    artifact_kind,
):
    if artifact_kind == "REPORT":
        result = make_result()
    else:
        result = make_manifest_result()

    assert result.artifact_kind == artifact_kind


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        b"REPORT",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_artifact_kind_rejects_non_string_values(
    value,
):
    with pytest.raises(
        TypeError,
        match="^artifact_kind must be a string$",
    ):
        make_result(
            artifact_kind=value,
        )


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "report",
        "Report",
        "MANIFEST",
        "ARTIFACT",
        "REPORT_ARTIFACT",
        "MANIFEST_ARTIFACT",
        "GENERIC",
        "UNKNOWN",
        " REPORT",
        "REPORT ",
    ],
)
def test_artifact_kind_rejects_invalid_values(
    value,
):
    with pytest.raises(
        ValueError,
        match=(
            "^artifact_kind must be REPORT or "
            "DIGEST_MANIFEST$"
        ),
    ):
        make_result(
            artifact_kind=value,
        )


def test_artifact_kind_string_subclass_is_accepted():
    class ArtifactKind(str):
        pass

    value = ArtifactKind("REPORT")

    result = make_result(
        artifact_kind=value,
    )

    assert result.artifact_kind is value


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        b"RIRA-000000001",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_artifact_id_rejects_non_string_values(
    value,
):
    with pytest.raises(
        TypeError,
        match="^artifact_id must be a string$",
    ):
        make_result(
            artifact_id=value,
        )


@pytest.mark.parametrize(
    "value",
    [
        "RIRA-000000001",
        "RIRA-000000002",
        "RIRA-000000010",
        "RIRA-000000100",
        "RIRA-000001000",
        "RIRA-999999999",
    ],
)
def test_valid_report_artifact_ids_are_accepted(
    value,
):
    candidate = make_report_artifact(
        report_artifact_id=value,
    )

    result = make_result(
        artifact_id=value,
        candidate_artifact=candidate,
    )

    assert result.artifact_id == value


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "RIRA",
        "RIRA-",
        "RIRA-1",
        "RIRA-00000001",
        "RIRA-0000000001",
        "RIRA_000000001",
        "RIDMA-000000001",
        "rira-000000001",
        " RIRA-000000001",
        "RIRA-000000001 ",
        "RIRA-00000000A",
    ],
)
def test_report_artifact_id_rejects_invalid_syntax(
    value,
):
    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id must match "
            "RIRA-######### for REPORT$"
        ),
    ):
        make_result(
            artifact_id=value,
        )


def test_zero_report_artifact_id_is_rejected():
    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id numeric component "
            "must be greater than zero$"
        ),
    ):
        make_result(
            artifact_id="RIRA-000000000",
        )


@pytest.mark.parametrize(
    "value",
    [
        "RIDMA-000000001",
        "RIDMA-000000002",
        "RIDMA-000000010",
        "RIDMA-000000100",
        "RIDMA-000001000",
        "RIDMA-999999999",
    ],
)
def test_valid_manifest_artifact_ids_are_accepted(
    value,
):
    candidate = make_manifest_artifact(
        manifest_artifact_id=value,
    )

    result = make_manifest_result(
        artifact_id=value,
        candidate_artifact=candidate,
    )

    assert result.artifact_id == value


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "RIDMA",
        "RIDMA-",
        "RIDMA-1",
        "RIDMA-00000001",
        "RIDMA-0000000001",
        "RIDMA_000000001",
        "RIRA-000000001",
        "ridma-000000001",
        " RIDMA-000000001",
        "RIDMA-000000001 ",
        "RIDMA-00000000A",
    ],
)
def test_manifest_artifact_id_rejects_invalid_syntax(
    value,
):
    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id must match "
            "RIDMA-######### for DIGEST_MANIFEST$"
        ),
    ):
        make_manifest_result(
            artifact_id=value,
        )


def test_zero_manifest_artifact_id_is_rejected():
    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id numeric component "
            "must be greater than zero$"
        ),
    ):
        make_manifest_result(
            artifact_id="RIDMA-000000000",
        )


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        b"REGISTERED",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_status_rejects_non_string_values(
    value,
):
    with pytest.raises(
        TypeError,
        match="^status must be a string$",
    ):
        make_result(
            status=value,
        )


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "registered",
        "Registered",
        "APPENDED",
        "DUPLICATE",
        "CONFLICT",
        "FAILED",
        "REJECTED",
        "UNCHANGED",
        "SUCCESS",
        "ERROR",
        " REGISTERED",
        "REGISTERED ",
    ],
)
def test_status_rejects_invalid_values(
    value,
):
    with pytest.raises(
        ValueError,
        match=(
            "^status must be REGISTERED, "
            "ALREADY_REGISTERED, or "
            "IDENTITY_COLLISION$"
        ),
    ):
        make_result(
            status=value,
        )


def test_status_string_subclass_is_accepted():
    class Status(str):
        pass

    value = Status("REGISTERED")

    result = make_result(
        status=value,
    )

    assert result.status is value


@pytest.mark.parametrize(
    "value",
    [
        None,
        {},
        [],
        (),
        "artifact",
        b"artifact",
        1,
        1.0,
        object(),
    ],
)
def test_candidate_artifact_rejects_invalid_types(
    value,
):
    with pytest.raises(
        TypeError,
        match=(
            "^candidate_artifact must be a supported "
            "runtime-record inspection artifact$"
        ),
    ):
        make_result(
            candidate_artifact=value,
        )


def test_candidate_artifact_rejects_report_value():
    with pytest.raises(
        TypeError,
        match="candidate_artifact",
    ):
        make_result(
            candidate_artifact=make_report(),
        )


def test_candidate_artifact_rejects_manifest_value():
    with pytest.raises(
        TypeError,
        match="candidate_artifact",
    ):
        make_result(
            candidate_artifact=make_manifest(),
        )


@pytest.mark.parametrize(
    "value",
    [
        {},
        [],
        (),
        "artifact",
        b"artifact",
        1,
        1.0,
        object(),
    ],
)
def test_existing_artifact_rejects_invalid_types(
    value,
):
    candidate = make_report_artifact()

    with pytest.raises(
        TypeError,
        match=(
            "^existing_artifact must be None or a "
            "supported runtime-record inspection artifact$"
        ),
    ):
        make_result(
            status="ALREADY_REGISTERED",
            existing_artifact=value,
            candidate_artifact=candidate,
        )


def test_report_kind_rejects_manifest_candidate():
    candidate = make_manifest_artifact()

    with pytest.raises(
        TypeError,
        match=(
            "^candidate_artifact must be a "
            "RuntimeRecordInspectionReportArtifact "
            "for REPORT$"
        ),
    ):
        make_result(
            candidate_artifact=candidate,
        )


def test_report_kind_rejects_manifest_existing():
    candidate = make_report_artifact()
    existing = make_manifest_artifact(
        manifest_artifact_id="RIDMA-000000001",
    )

    with pytest.raises(
        TypeError,
        match=(
            "^existing_artifact must be a "
            "RuntimeRecordInspectionReportArtifact "
            "for REPORT$"
        ),
    ):
        make_result(
            status="ALREADY_REGISTERED",
            existing_artifact=existing,
            candidate_artifact=candidate,
        )


def test_manifest_kind_rejects_report_candidate():
    candidate = make_report_artifact()

    with pytest.raises(
        TypeError,
        match=(
            "^candidate_artifact must be a "
            "RuntimeRecordInspectionDigestManifestArtifact "
            "for DIGEST_MANIFEST$"
        ),
    ):
        make_manifest_result(
            candidate_artifact=candidate,
        )


def test_manifest_kind_rejects_report_existing():
    candidate = make_manifest_artifact()
    existing = make_report_artifact(
        report_artifact_id="RIRA-000000001",
    )

    with pytest.raises(
        TypeError,
        match=(
            "^existing_artifact must be a "
            "RuntimeRecordInspectionDigestManifestArtifact "
            "for DIGEST_MANIFEST$"
        ),
    ):
        make_manifest_result(
            status="ALREADY_REGISTERED",
            existing_artifact=existing,
            candidate_artifact=candidate,
        )


def test_report_candidate_identifier_must_match():
    candidate = make_report_artifact(
        report_artifact_id="RIRA-000000002",
    )

    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id must match "
            "candidate_artifact identifier$"
        ),
    ):
        make_result(
            artifact_id="RIRA-000000001",
            candidate_artifact=candidate,
        )


def test_manifest_candidate_identifier_must_match():
    candidate = make_manifest_artifact(
        manifest_artifact_id="RIDMA-000000002",
    )

    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id must match "
            "candidate_artifact identifier$"
        ),
    ):
        make_manifest_result(
            artifact_id="RIDMA-000000001",
            candidate_artifact=candidate,
        )


def test_report_existing_identifier_must_match():
    existing = make_report_artifact(
        report_artifact_id="RIRA-000000002",
    )
    candidate = make_report_artifact(
        report_artifact_id="RIRA-000000001",
    )

    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id must match "
            "existing_artifact identifier$"
        ),
    ):
        make_result(
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=candidate,
        )


def test_manifest_existing_identifier_must_match():
    existing = make_manifest_artifact(
        manifest_artifact_id="RIDMA-000000002",
    )
    candidate = make_manifest_artifact(
        manifest_artifact_id="RIDMA-000000001",
    )

    with pytest.raises(
        ValueError,
        match=(
            "^artifact_id must match "
            "existing_artifact identifier$"
        ),
    ):
        make_manifest_result(
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=candidate,
        )


def test_registered_report_result_is_valid():
    candidate = make_report_artifact()

    result = make_result(
        candidate_artifact=candidate,
    )

    assert result.artifact_kind == "REPORT"
    assert result.artifact_id == candidate.report_artifact_id
    assert result.status == "REGISTERED"
    assert result.existing_artifact is None
    assert result.candidate_artifact is candidate
    assert result.registry_changed is True
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_registered_manifest_result_is_valid():
    candidate = make_manifest_artifact()

    result = make_manifest_result(
        candidate_artifact=candidate,
    )

    assert result.artifact_kind == "DIGEST_MANIFEST"
    assert result.artifact_id == candidate.manifest_artifact_id
    assert result.status == "REGISTERED"
    assert result.existing_artifact is None
    assert result.candidate_artifact is candidate
    assert result.registry_changed is True
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_registered_status_rejects_existing_artifact():
    candidate = make_report_artifact()

    with pytest.raises(
        ValueError,
        match=(
            "^existing_artifact must be None "
            "when status is REGISTERED$"
        ),
    ):
        make_result(
            existing_artifact=candidate,
            candidate_artifact=candidate,
        )


def test_already_registered_accepts_same_object():
    artifact = make_report_artifact()

    result = make_result(
        status="ALREADY_REGISTERED",
        existing_artifact=artifact,
        candidate_artifact=artifact,
    )

    assert result.existing_artifact is artifact
    assert result.candidate_artifact is artifact
    assert result.registry_changed is False
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_already_registered_accepts_equal_separate_objects():
    existing = make_report_artifact()
    candidate = make_report_artifact()

    assert existing == candidate
    assert existing is not candidate

    result = make_result(
        status="ALREADY_REGISTERED",
        existing_artifact=existing,
        candidate_artifact=candidate,
    )

    assert result.existing_artifact is existing
    assert result.candidate_artifact is candidate


def test_manifest_already_registered_accepts_equal_objects():
    existing = make_manifest_artifact()
    candidate = make_manifest_artifact()

    result = make_manifest_result(
        status="ALREADY_REGISTERED",
        existing_artifact=existing,
        candidate_artifact=candidate,
    )

    assert result.registry_changed is False
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_already_registered_requires_existing_artifact():
    candidate = make_report_artifact()

    with pytest.raises(
        ValueError,
        match=(
            "^existing_artifact is required when "
            "status is ALREADY_REGISTERED$"
        ),
    ):
        make_result(
            status="ALREADY_REGISTERED",
            existing_artifact=None,
            candidate_artifact=candidate,
        )


def test_already_registered_requires_equal_artifacts():
    existing = make_report_artifact(
        report=make_report(
            record_id="RR-000000001",
        )
    )
    candidate = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "^existing_artifact must equal "
            "candidate_artifact when status is "
            "ALREADY_REGISTERED$"
        ),
    ):
        make_result(
            status="ALREADY_REGISTERED",
            existing_artifact=existing,
            candidate_artifact=candidate,
        )


def test_report_identity_collision_is_valid():
    existing = make_report_artifact(
        report=make_report(
            record_id="RR-000000001",
        )
    )
    candidate = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )

    result = make_result(
        status="IDENTITY_COLLISION",
        existing_artifact=existing,
        candidate_artifact=candidate,
    )

    assert result.registry_changed is False
    assert result.registration_accepted is False
    assert result.collision_detected is True


def test_manifest_identity_collision_is_valid():
    existing = make_manifest_artifact(
        manifest=make_manifest(
            sha256_digest="0" * 64,
        )
    )
    candidate = make_manifest_artifact(
        manifest=make_manifest(
            sha256_digest="1" * 64,
        )
    )

    result = make_manifest_result(
        status="IDENTITY_COLLISION",
        existing_artifact=existing,
        candidate_artifact=candidate,
    )

    assert result.collision_detected is True


def test_collision_requires_existing_artifact():
    candidate = make_report_artifact()

    with pytest.raises(
        ValueError,
        match=(
            "^existing_artifact is required when "
            "status is IDENTITY_COLLISION$"
        ),
    ):
        make_result(
            status="IDENTITY_COLLISION",
            existing_artifact=None,
            candidate_artifact=candidate,
        )


def test_collision_requires_unequal_artifacts():
    artifact = make_report_artifact()

    with pytest.raises(
        ValueError,
        match=(
            "^existing_artifact must differ from "
            "candidate_artifact when status is "
            "IDENTITY_COLLISION$"
        ),
    ):
        make_result(
            status="IDENTITY_COLLISION",
            existing_artifact=artifact,
            candidate_artifact=artifact,
        )


def test_validation_order_artifact_kind_type_first():
    with pytest.raises(
        TypeError,
        match="artifact_kind",
    ):
        make_result(
            artifact_kind=None,
            artifact_id=None,
            status=None,
            candidate_artifact=None,
        )


def test_validation_order_artifact_kind_value_before_id():
    with pytest.raises(
        ValueError,
        match="artifact_kind",
    ):
        make_result(
            artifact_kind="INVALID",
            artifact_id=None,
        )


def test_validation_order_artifact_id_type_before_status():
    with pytest.raises(
        TypeError,
        match="artifact_id",
    ):
        make_result(
            artifact_id=None,
            status=None,
        )


def test_validation_order_artifact_id_syntax_before_status():
    with pytest.raises(
        ValueError,
        match="artifact_id must match",
    ):
        make_result(
            artifact_id="invalid",
            status=None,
        )


def test_validation_order_zero_id_before_status():
    with pytest.raises(
        ValueError,
        match="numeric component",
    ):
        make_result(
            artifact_id="RIRA-000000000",
            status=None,
        )


def test_validation_order_status_before_candidate():
    with pytest.raises(
        ValueError,
        match="status",
    ):
        make_result(
            status="INVALID",
            candidate_artifact=None,
        )


def test_validation_order_candidate_before_existing():
    with pytest.raises(
        TypeError,
        match="candidate_artifact",
    ):
        make_result(
            candidate_artifact=None,
            existing_artifact=object(),
        )


def test_validation_order_existing_before_kind_consistency():
    with pytest.raises(
        TypeError,
        match="existing_artifact must be None",
    ):
        make_result(
            status="ALREADY_REGISTERED",
            existing_artifact=object(),
        )


def test_validation_order_kind_consistency_before_identifier():
    candidate = make_manifest_artifact()

    with pytest.raises(
        TypeError,
        match="for REPORT",
    ):
        make_result(
            artifact_id="RIRA-000000002",
            candidate_artifact=candidate,
        )


def test_validation_order_candidate_id_before_existing_id():
    candidate = make_report_artifact(
        report_artifact_id="RIRA-000000002",
    )
    existing = make_report_artifact(
        report_artifact_id="RIRA-000000003",
    )

    with pytest.raises(
        ValueError,
        match="candidate_artifact",
    ):
        make_result(
            artifact_id="RIRA-000000001",
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=candidate,
        )


def test_derived_properties_are_not_dataclass_fields():
    field_names = {
        field.name
        for field in fields(
            RuntimeRecordInspectionArtifactRegistrationResult
        )
    }

    assert "registry_changed" not in field_names
    assert "registration_accepted" not in field_names
    assert "collision_detected" not in field_names


def test_instance_dictionary_contains_only_contract_fields():
    result = make_result()

    assert set(result.__dict__) == {
        "artifact_kind",
        "artifact_id",
        "status",
        "existing_artifact",
        "candidate_artifact",
    }


@pytest.mark.parametrize(
    "attribute",
    [
        "registry_changed",
        "registration_accepted",
        "collision_detected",
    ],
)
def test_derived_properties_are_not_stored(
    attribute,
):
    result = make_result()

    assert attribute not in result.__dict__


@pytest.mark.parametrize(
    "field_name,new_value",
    [
        ("artifact_kind", "DIGEST_MANIFEST"),
        ("artifact_id", "RIRA-000000002"),
        ("status", "ALREADY_REGISTERED"),
        ("existing_artifact", object()),
        ("candidate_artifact", object()),
    ],
)
def test_fields_are_immutable(
    field_name,
    new_value,
):
    result = make_result()

    with pytest.raises(FrozenInstanceError):
        setattr(
            result,
            field_name,
            new_value,
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "artifact_kind",
        "artifact_id",
        "status",
        "existing_artifact",
        "candidate_artifact",
    ],
)
def test_fields_cannot_be_deleted(
    field_name,
):
    result = make_result()

    with pytest.raises(FrozenInstanceError):
        delattr(
            result,
            field_name,
        )


@pytest.mark.parametrize(
    "property_name",
    [
        "registry_changed",
        "registration_accepted",
        "collision_detected",
    ],
)
def test_derived_properties_cannot_be_assigned(
    property_name,
):
    result = make_result()

    with pytest.raises(
        (
            FrozenInstanceError,
            AttributeError,
        )
    ):
        setattr(
            result,
            property_name,
            False,
        )


def test_result_equals_itself():
    result = make_result()

    assert result == result


def test_equal_results_are_equal():
    first = make_result()
    second = make_result()

    assert first == second


def test_report_result_is_not_equal_to_manifest_result():
    assert make_result() != make_manifest_result()


def test_result_is_not_equal_to_candidate_artifact():
    result = make_result()

    assert result != result.candidate_artifact


def test_result_is_not_equal_to_tuple():
    result = make_result()

    assert result != (
        result.artifact_kind,
        result.artifact_id,
        result.status,
        result.existing_artifact,
        result.candidate_artifact,
    )


def test_result_is_not_equal_to_dictionary():
    result = make_result()

    assert result != {
        "artifact_kind": result.artifact_kind,
        "artifact_id": result.artifact_id,
        "status": result.status,
        "existing_artifact": result.existing_artifact,
        "candidate_artifact": result.candidate_artifact,
    }


def test_result_is_hashable():
    assert isinstance(
        hash(make_result()),
        int,
    )


def test_equal_results_have_equal_hashes():
    first = make_result()
    second = make_result()

    assert first == second
    assert hash(first) == hash(second)


def test_equal_results_collapse_in_set():
    first = make_result()
    second = make_result()

    assert len(
        {
            first,
            second,
        }
    ) == 1


def test_result_can_be_dictionary_key():
    result = make_result()

    mapping = {
        result: "stored",
    }

    assert mapping[result] == "stored"


@pytest.mark.parametrize(
    "operator",
    [
        lambda first, second: first < second,
        lambda first, second: first <= second,
        lambda first, second: first > second,
        lambda first, second: first >= second,
    ],
)
def test_result_has_no_ordering(
    operator,
):
    with pytest.raises(TypeError):
        operator(
            make_result(),
            make_result(),
        )


def test_class_defines_no_custom_bool():
    assert (
        "__bool__"
        not in (
            RuntimeRecordInspectionArtifactRegistrationResult
            .__dict__
        )
    )


def test_default_repr_exposes_contract_fields():
    representation = repr(
        make_result()
    )

    assert (
        "RuntimeRecordInspectionArtifactRegistrationResult"
        in representation
    )
    assert "artifact_kind" in representation
    assert "artifact_id" in representation
    assert "status" in representation
    assert "existing_artifact" in representation
    assert "candidate_artifact" in representation


@pytest.mark.parametrize(
    "method_name",
    [
        "__iter__",
        "__len__",
        "__getitem__",
        "to_dict",
        "to_json",
        "to_bytes",
        "serialize",
        "deserialize",
        "register",
        "lookup",
        "get_report_artifact",
        "get_manifest_artifact",
        "save",
        "load",
        "persist",
        "snapshot",
        "restore",
        "create_receipt",
        "sign",
        "compute_digest",
        "verify_signature",
        "admit",
        "approve",
        "trust",
        "authorize",
        "execute",
        "apply",
    ],
)
def test_class_excludes_unowned_methods(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionArtifactRegistrationResult,
        method_name,
    )


@pytest.mark.parametrize(
    "attribute",
    [
        "registered_at",
        "attempted_at",
        "completed_at",
        "observed_at",
        "created_at",
        "append_position",
        "sequence_number",
        "registration_index",
        "receipt_id",
        "registry_id",
        "registry_instance_id",
        "signature",
        "digest",
        "storage_ref",
        "actor_ref",
        "submitter_ref",
        "creator_ref",
        "source_ref",
        "method_ref",
        "environment_ref",
        "custody_ref",
        "custodian_ref",
        "transfer_ref",
        "storage_location",
        "parent_ref",
        "predecessor_ref",
        "supersedes_ref",
        "derived_from_ref",
        "version_ref",
        "association_ref",
        "binding_ref",
        "pair_ref",
        "admitted",
        "approved",
        "eligible",
        "trusted",
        "authentic",
        "verified",
        "authorized",
        "authority_ref",
        "permission",
        "execution_allowed",
    ],
)
def test_result_excludes_unowned_fields(
    attribute,
):
    assert not hasattr(
        make_result(),
        attribute,
    )


def test_private_constants_are_present():
    module = importlib.import_module(
        "models.runtime_record_inspection_artifact_registration_result"
    )

    assert module._ARTIFACT_KINDS == frozenset(
        {
            "REPORT",
            "DIGEST_MANIFEST",
        }
    )
    assert module._REGISTRATION_STATUSES == frozenset(
        {
            "REGISTERED",
            "ALREADY_REGISTERED",
            "IDENTITY_COLLISION",
        }
    )
    assert (
        module._REPORT_ARTIFACT_ID_PATTERN.pattern
        == r"^RIRA-[0-9]{9}$"
    )
    assert (
        module._MANIFEST_ARTIFACT_ID_PATTERN.pattern
        == r"^RIDMA-[0-9]{9}$"
    )


def test_private_constants_are_not_dataclass_fields():
    field_names = {
        field.name
        for field in fields(
            RuntimeRecordInspectionArtifactRegistrationResult
        )
    }

    assert "_ARTIFACT_KINDS" not in field_names
    assert "_REGISTRATION_STATUSES" not in field_names
    assert "_REPORT_ARTIFACT_ID_PATTERN" not in field_names
    assert "_MANIFEST_ARTIFACT_ID_PATTERN" not in field_names


@pytest.mark.parametrize(
    "method_name",
    [
        "_validate_artifact_kind",
        "_validate_artifact_id",
        "_validate_status",
        "_validate_candidate_artifact",
        "_validate_existing_artifact",
        "_validate_artifact_kind_consistency",
        "_validate_identifier_consistency",
        "_validate_status_consistency",
    ],
)
def test_required_validation_methods_are_present(
    method_name,
):
    assert callable(
        getattr(
            RuntimeRecordInspectionArtifactRegistrationResult,
            method_name,
        )
    )


@pytest.mark.parametrize(
    "method_name",
    [
        "_validate_registry",
        "_validate_receipt",
        "_validate_provenance",
        "_validate_custody",
        "_validate_authority",
        "_validate_association",
    ],
)
def test_unowned_validation_methods_are_absent(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionArtifactRegistrationResult,
        method_name,
    )


def test_class_has_boundary_docstring():
    docstring = (
        RuntimeRecordInspectionArtifactRegistrationResult
        .__doc__
        or ""
    ).lower()

    assert "immutable" in docstring
    assert "registration" in docstring
    assert "local" in docstring
    assert "persist" in docstring
    assert "receipt" in docstring
    assert "admit" in docstring
    assert "authorize" in docstring


def test_construction_emits_no_output(
    capsys,
):
    make_result()

    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""


def test_source_has_no_unowned_dependencies():
    source_path = (
        Path(__file__).resolve().parents[2]
        / "models"
        / (
            "runtime_record_inspection_"
            "artifact_registration_result.py"
        )
    )
    source = source_path.read_text(
        encoding="utf-8"
    ).lower()

    prohibited_terms = (
        "streamlit",
        "flask",
        "django",
        "fastapi",
        "tkinter",
        "pyqt",
        "pandas",
        "numpy",
        "sqlalchemy",
        "from services",
        "import services",
        "pathlib",
        "json",
        "pickle",
        "shelve",
        "sqlite3",
        "datetime",
        "import time",
        "hashlib",
        "uuid",
        "random",
        "secrets",
        "import os",
    )

    for term in prohibited_terms:
        assert term not in source