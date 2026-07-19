from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timezone
import importlib
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
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


def make_artifact(**overrides):
    values = {
        "report_artifact_id": "RIRA-000000001",
        "report": make_report(),
    }
    values.update(overrides)
    return RuntimeRecordInspectionReportArtifact(**values)


def make_manifest():
    return RuntimeRecordInspectionDigestManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest="0" * 64,
        byte_length=0,
        codec="utf-8",
        bom_present=False,
    )


def test_module_imports():
    module = importlib.import_module(
        "models.runtime_record_inspection_report_artifact"
    )

    assert module is not None


def test_class_imports_from_selected_module():
    module = importlib.import_module(
        "models.runtime_record_inspection_report_artifact"
    )

    assert (
        module.RuntimeRecordInspectionReportArtifact
        is RuntimeRecordInspectionReportArtifact
    )


def test_model_is_dataclass():
    assert is_dataclass(
        RuntimeRecordInspectionReportArtifact
    )


def test_dataclass_field_order_is_exact():
    assert tuple(
        field.name
        for field in fields(
            RuntimeRecordInspectionReportArtifact
        )
    ) == (
        "report_artifact_id",
        "report",
    )


def test_constructor_requires_report_artifact_id():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionReportArtifact(
            report=make_report(),
        )


def test_constructor_requires_report():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionReportArtifact(
            report_artifact_id="RIRA-000000001",
        )


def test_positional_construction_is_supported():
    report = make_report()

    artifact = RuntimeRecordInspectionReportArtifact(
        "RIRA-000000001",
        report,
    )

    assert artifact.report_artifact_id == "RIRA-000000001"
    assert artifact.report is report


def test_keyword_construction_is_supported():
    report = make_report()

    artifact = RuntimeRecordInspectionReportArtifact(
        report_artifact_id="RIRA-000000001",
        report=report,
    )

    assert artifact.report_artifact_id == "RIRA-000000001"
    assert artifact.report is report


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
def test_valid_report_artifact_ids_are_preserved(value):
    artifact = make_artifact(
        report_artifact_id=value,
    )

    assert artifact.report_artifact_id == value


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
def test_report_artifact_id_rejects_non_string_values(
    value,
):
    with pytest.raises(
        TypeError,
        match="report_artifact_id",
    ):
        make_artifact(
            report_artifact_id=value,
        )


def test_report_artifact_id_type_error_message_is_exact():
    with pytest.raises(
        TypeError,
        match=(
            "^report_artifact_id must be a string$"
        ),
    ):
        make_artifact(
            report_artifact_id=None,
        )


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
        "RIR-000000001",
        "RIA-000000001",
        "RIDMA-000000001",
        "rira-000000001",
        "Rira-000000001",
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
        match="report_artifact_id",
    ):
        make_artifact(
            report_artifact_id=value,
        )


def test_report_artifact_id_syntax_error_message_is_exact():
    with pytest.raises(
        ValueError,
        match=(
            "^report_artifact_id must match "
            "RIRA-#########$"
        ),
    ):
        make_artifact(
            report_artifact_id="RIRA-1",
        )


def test_zero_report_artifact_id_is_rejected():
    with pytest.raises(
        ValueError,
        match=(
            "^report_artifact_id numeric component "
            "must be greater than zero$"
        ),
    ):
        make_artifact(
            report_artifact_id="RIRA-000000000",
        )


def test_maximum_report_artifact_id_is_accepted():
    artifact = make_artifact(
        report_artifact_id="RIRA-999999999",
    )

    assert (
        artifact.report_artifact_id
        == "RIRA-999999999"
    )


@pytest.mark.parametrize(
    "value",
    [
        "rira-000000001",
        "Rira-000000001",
        "rIRA-000000001",
    ],
)
def test_report_artifact_id_is_case_sensitive(
    value,
):
    with pytest.raises(ValueError):
        make_artifact(
            report_artifact_id=value,
        )


@pytest.mark.parametrize(
    "value",
    [
        " RIRA-000000001",
        "RIRA-000000001 ",
        "\tRIRA-000000001",
        "RIRA-000000001\n",
    ],
)
def test_report_artifact_id_rejects_whitespace(
    value,
):
    with pytest.raises(ValueError):
        make_artifact(
            report_artifact_id=value,
        )


def test_valid_string_subclass_identifier_is_accepted():
    class ReportArtifactId(str):
        pass

    value = ReportArtifactId(
        "RIRA-000000001"
    )

    artifact = make_artifact(
        report_artifact_id=value,
    )

    assert artifact.report_artifact_id is value


def test_valid_report_is_accepted():
    report = make_report()

    artifact = make_artifact(
        report=report,
    )

    assert artifact.report is report


def test_report_object_identity_is_preserved():
    report = make_report()

    artifact = make_artifact(
        report=report,
    )

    assert artifact.report is report


@pytest.mark.parametrize(
    "value",
    [
        None,
        {},
        [],
        (),
        "report",
        b"report",
        1,
        1.0,
        object(),
    ],
)
def test_report_rejects_invalid_types(
    value,
):
    with pytest.raises(
        TypeError,
        match="report",
    ):
        make_artifact(
            report=value,
        )


def test_report_rejects_digest_manifest():
    with pytest.raises(
        TypeError,
        match="report",
    ):
        make_artifact(
            report=make_manifest(),
        )


def test_report_type_error_message_is_exact():
    with pytest.raises(
        TypeError,
        match=(
            "^report must be a "
            "RuntimeRecordInspectionReport$"
        ),
    ):
        make_artifact(
            report=None,
        )


def test_report_subclass_is_accepted():
    class ReportSubclass(
        RuntimeRecordInspectionReport
    ):
        pass

    report = ReportSubclass(
        record_id="RR-000000001",
        record_type="RuntimeEventRecord",
        record_category="EVENT",
        append_position=1,
        recorded_at=RECORDED_AT,
        schema_version="1.0",
        provenance_ref=None,
        external_id=None,
        declared_fields=(
            ("event_type", "OBSERVED"),
            ("target_ref", None),
            ("actor_ref", None),
            ("source_ref", None),
            ("scope_ref", None),
            ("branch_ref", None),
            ("occurred_at", None),
            ("effective_at", None),
        ),
    )

    artifact = make_artifact(
        report=report,
    )

    assert artifact.report is report


def test_identifier_type_failure_precedes_report_failure():
    with pytest.raises(
        TypeError,
        match="report_artifact_id",
    ):
        make_artifact(
            report_artifact_id=None,
            report=None,
        )


def test_identifier_syntax_failure_precedes_report_failure():
    with pytest.raises(
        ValueError,
        match="report_artifact_id",
    ):
        make_artifact(
            report_artifact_id="invalid",
            report=None,
        )


def test_zero_identifier_failure_precedes_report_failure():
    with pytest.raises(
        ValueError,
        match=(
            "numeric component must be greater "
            "than zero"
        ),
    ):
        make_artifact(
            report_artifact_id="RIRA-000000000",
            report=None,
        )


def test_report_failure_occurs_after_valid_identifier():
    with pytest.raises(
        TypeError,
        match="report must be",
    ):
        make_artifact(
            report_artifact_id="RIRA-000000001",
            report=None,
        )


def test_instance_dictionary_contains_only_contract_fields():
    artifact = make_artifact()

    assert set(
        artifact.__dict__
    ) == {
        "report_artifact_id",
        "report",
    }


@pytest.mark.parametrize(
    "attribute",
    [
        "identifier_prefix",
        "numeric_component",
        "artifact_type",
        "validation_status",
    ],
)
def test_no_derived_identifier_state_is_stored(
    attribute,
):
    artifact = make_artifact()

    assert not hasattr(
        artifact,
        attribute,
    )


@pytest.mark.parametrize(
    "attribute",
    [
        "record_id",
        "record_type",
        "record_category",
        "append_position",
        "recorded_at",
        "schema_version",
        "provenance_ref",
        "external_id",
        "declared_fields",
    ],
)
def test_report_fields_are_not_duplicated_on_wrapper(
    attribute,
):
    artifact = make_artifact()

    assert not hasattr(
        artifact,
        attribute,
    )


def test_report_artifact_id_is_immutable():
    artifact = make_artifact()

    with pytest.raises(
        FrozenInstanceError,
    ):
        artifact.report_artifact_id = (
            "RIRA-000000002"
        )

    assert (
        artifact.report_artifact_id
        == "RIRA-000000001"
    )


def test_report_is_immutable_on_wrapper():
    artifact = make_artifact()
    original_report = artifact.report

    with pytest.raises(
        FrozenInstanceError,
    ):
        artifact.report = make_report(
            record_id="RR-000000002",
        )

    assert artifact.report is original_report


@pytest.mark.parametrize(
    "attribute",
    [
        "report_artifact_id",
        "report",
    ],
)
def test_fields_cannot_be_deleted(
    attribute,
):
    artifact = make_artifact()

    with pytest.raises(
        FrozenInstanceError,
    ):
        delattr(
            artifact,
            attribute,
        )


def test_wrapper_equals_itself():
    artifact = make_artifact()

    assert artifact == artifact


def test_same_id_and_equal_report_are_equal():
    first = make_artifact()
    second = make_artifact()

    assert first == second


def test_same_id_and_different_report_are_not_equal():
    first = make_artifact()
    second = make_artifact(
        report=make_report(
            record_id="RR-000000002",
        ),
    )

    assert first != second


def test_different_id_and_same_report_are_not_equal():
    report = make_report()

    first = make_artifact(
        report_artifact_id="RIRA-000000001",
        report=report,
    )
    second = make_artifact(
        report_artifact_id="RIRA-000000002",
        report=report,
    )

    assert first != second


def test_different_id_and_different_report_are_not_equal():
    first = make_artifact()

    second = make_artifact(
        report_artifact_id="RIRA-000000002",
        report=make_report(
            record_id="RR-000000002",
        ),
    )

    assert first != second


def test_wrapper_is_not_equal_to_retained_report():
    artifact = make_artifact()

    assert artifact != artifact.report


def test_wrapper_is_not_equal_to_tuple():
    artifact = make_artifact()

    assert artifact != (
        artifact.report_artifact_id,
        artifact.report,
    )


def test_wrapper_is_not_equal_to_dictionary():
    artifact = make_artifact()

    assert artifact != {
        "report_artifact_id": (
            artifact.report_artifact_id
        ),
        "report": artifact.report,
    }


def test_wrapper_is_not_equal_to_arbitrary_object():
    assert make_artifact() != object()


def test_wrapper_is_hashable():
    result = hash(
        make_artifact()
    )

    assert isinstance(
        result,
        int,
    )


def test_equal_wrappers_have_equal_hashes():
    first = make_artifact()
    second = make_artifact()

    assert first == second
    assert hash(first) == hash(second)


def test_equal_wrappers_collapse_in_set():
    first = make_artifact()
    second = make_artifact()

    assert len(
        {
            first,
            second,
        }
    ) == 1


def test_different_ids_remain_distinct_in_set():
    report = make_report()

    first = make_artifact(
        report_artifact_id="RIRA-000000001",
        report=report,
    )
    second = make_artifact(
        report_artifact_id="RIRA-000000002",
        report=report,
    )

    assert len(
        {
            first,
            second,
        }
    ) == 2


def test_wrapper_can_be_dictionary_key():
    artifact = make_artifact()

    values = {
        artifact: "stored",
    }

    assert values[artifact] == "stored"


@pytest.mark.parametrize(
    "operator",
    [
        lambda first, second: first < second,
        lambda first, second: first <= second,
        lambda first, second: first > second,
        lambda first, second: first >= second,
    ],
)
def test_wrapper_has_no_ordering(
    operator,
):
    with pytest.raises(TypeError):
        operator(
            make_artifact(),
            make_artifact(),
        )


def test_class_defines_no_custom_bool():
    assert (
        "__bool__"
        not in RuntimeRecordInspectionReportArtifact.__dict__
    )


def test_default_repr_exposes_contract_fields():
    representation = repr(
        make_artifact()
    )

    assert (
        "RuntimeRecordInspectionReportArtifact"
        in representation
    )
    assert "report_artifact_id" in representation
    assert "report=" in representation


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
        "compute_digest",
        "allocate_id",
        "next_id",
        "generate_id",
        "new_id",
        "register",
        "persist",
        "save",
        "load",
        "verify",
        "admit",
        "authorize",
    ],
)
def test_class_excludes_unowned_methods(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionReportArtifact,
        method_name,
    )


@pytest.mark.parametrize(
    "attribute",
    [
        "created_at",
        "observed_at",
        "registered_at",
        "effective_at",
        "source_ref",
        "creator_ref",
        "actor_ref",
        "method_ref",
        "environment_ref",
        "custody_ref",
        "custodian_ref",
        "transfer_ref",
        "storage_ref",
        "predecessor_ref",
        "parent_ref",
        "version_ref",
        "supersedes_ref",
        "derived_from_ref",
        "manifest_artifact_id",
        "manifest_ref",
        "association_ref",
        "binding_ref",
        "registry_ref",
        "append_position",
        "persisted",
        "admitted",
        "acceptable",
        "eligible",
        "approved",
        "trusted",
        "authorized",
        "authority_ref",
        "permission",
        "execution_allowed",
    ],
)
def test_wrapper_excludes_unowned_fields(
    attribute,
):
    artifact = make_artifact()

    assert not hasattr(
        artifact,
        attribute,
    )


def test_validation_methods_are_present():
    assert callable(
        RuntimeRecordInspectionReportArtifact
        ._validate_report_artifact_id
    )
    assert callable(
        RuntimeRecordInspectionReportArtifact
        ._validate_report
    )


@pytest.mark.parametrize(
    "method_name",
    [
        "_validate_registry",
        "_validate_provenance",
        "_validate_custody",
        "_validate_manifest",
    ],
)
def test_unowned_validation_methods_are_absent(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionReportArtifact,
        method_name,
    )


def test_class_has_boundary_docstring():
    docstring = (
        RuntimeRecordInspectionReportArtifact.__doc__
        or ""
    ).lower()

    assert "identity" in docstring
    assert "addressability" in docstring
    assert "persist" in docstring
    assert "authorize" in docstring


def test_report_artifact_id_is_independent_of_record_id():
    artifact = make_artifact(
        report_artifact_id="RIRA-000000001",
        report=make_report(
            record_id="RR-000000999",
        ),
    )

    assert (
        artifact.report_artifact_id
        == "RIRA-000000001"
    )
    assert (
        artifact.report.record_id
        == "RR-000000999"
    )


def test_same_record_can_have_different_artifact_ids():
    report = make_report(
        record_id="RR-000000999",
    )

    first = make_artifact(
        report_artifact_id="RIRA-000000001",
        report=report,
    )
    second = make_artifact(
        report_artifact_id="RIRA-000000002",
        report=report,
    )

    assert (
        first.report.record_id
        == second.report.record_id
    )
    assert first != second


def test_different_records_can_share_id_in_memory():
    first = make_artifact(
        report_artifact_id="RIRA-000000001",
        report=make_report(
            record_id="RR-000000001",
        ),
    )
    second = make_artifact(
        report_artifact_id="RIRA-000000001",
        report=make_report(
            record_id="RR-000000002",
        ),
    )

    assert first != second


def test_report_identity_is_independent_of_append_position():
    first = make_artifact(
        report=make_report(
            append_position=1,
        ),
    )
    second = make_artifact(
        report=make_report(
            append_position=2,
        ),
    )

    assert (
        first.report_artifact_id
        == second.report_artifact_id
    )
    assert first != second


def test_report_identity_is_independent_of_external_id():
    first = make_artifact(
        report=make_report(
            external_id="external-001",
        ),
    )
    second = make_artifact(
        report=make_report(
            external_id="external-002",
        ),
    )

    assert (
        first.report_artifact_id
        == second.report_artifact_id
    )
    assert first != second


def test_report_identity_is_independent_of_provenance_ref():
    first = make_artifact(
        report=make_report(
            provenance_ref="PRV-000000001",
        ),
    )
    second = make_artifact(
        report=make_report(
            provenance_ref="PRV-000000002",
        ),
    )

    assert (
        first.report_artifact_id
        == second.report_artifact_id
    )
    assert first != second


def test_repeated_construction_is_deterministic():
    report = make_report()

    first = make_artifact(
        report=report,
    )
    second = make_artifact(
        report=report,
    )

    assert first == second
    assert first.report is report
    assert second.report is report


def test_construction_emits_no_output(
    capsys,
):
    make_artifact()

    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""


def test_source_has_no_framework_or_service_imports():
    source_path = (
        Path(__file__).resolve().parents[2]
        / "models"
        / "runtime_record_inspection_report_artifact.py"
    )
    source = source_path.read_text(
        encoding="utf-8",
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
        "runtime_record_registry",
        "artifact_registry",
        "from services",
        "import services",
        "hashlib",
        "uuid",
        "pathlib",
    )

    for term in prohibited_terms:
        assert term not in source


def test_source_defines_private_pattern_constant():
    module = importlib.import_module(
        "models.runtime_record_inspection_report_artifact"
    )

    pattern = module._REPORT_ARTIFACT_ID_PATTERN

    assert (
        pattern.pattern
        == r"^RIRA-[0-9]{9}$"
    )


def test_pattern_constant_is_not_dataclass_field():
    field_names = {
        field.name
        for field in fields(
            RuntimeRecordInspectionReportArtifact
        )
    }

    assert (
        "_REPORT_ARTIFACT_ID_PATTERN"
        not in field_names
    )