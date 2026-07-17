from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timezone
import importlib
import sys

import pytest

from models.runtime_object_version_record import (
    RuntimeObjectVersionRecord,
)
from models.runtime_record_identity import RuntimeRecordHeader


VALID_RECORDED_AT = datetime(
    2026,
    7,
    17,
    12,
    0,
    0,
    tzinfo=timezone.utc,
)

VALID_OBJECT_REF = "research_os"
VALID_REPRESENTATION_REF = "REP-000001"
VALID_VERSION_LABEL = "1"
VALID_PREDECESSOR_REF = "RR-000000201"
VALID_BRANCH_REF = "BRANCH-000001"
VALID_SCOPE_REF = "SCOPE-000001"


def make_version_header(**overrides):
    values = {
        "record_id": "RR-000000202",
        "record_category": "VERSION",
        "recorded_at": VALID_RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)


def make_version_record(**overrides):
    values = {
        "header": make_version_header(),
        "object_ref": VALID_OBJECT_REF,
        "representation_ref": VALID_REPRESENTATION_REF,
        "version_label": None,
        "predecessor_ref": None,
        "branch_ref": None,
        "scope_ref": None,
    }
    values.update(overrides)
    return RuntimeObjectVersionRecord(**values)


def test_runtime_object_version_record_is_a_dataclass():
    assert is_dataclass(RuntimeObjectVersionRecord)


def test_runtime_object_version_record_declares_exact_field_order():
    assert [
        field.name
        for field in fields(RuntimeObjectVersionRecord)
    ] == [
        "header",
        "object_ref",
        "representation_ref",
        "version_label",
        "predecessor_ref",
        "branch_ref",
        "scope_ref",
    ]


def test_runtime_object_version_record_accepts_required_fields_only():
    record = RuntimeObjectVersionRecord(
        header=make_version_header(),
        object_ref=VALID_OBJECT_REF,
        representation_ref=VALID_REPRESENTATION_REF,
    )

    assert record.header.record_category == "VERSION"
    assert record.object_ref == VALID_OBJECT_REF
    assert record.representation_ref == VALID_REPRESENTATION_REF
    assert record.version_label is None
    assert record.predecessor_ref is None
    assert record.branch_ref is None
    assert record.scope_ref is None


def test_runtime_object_version_record_preserves_exact_header_instance():
    header = make_version_header()
    record = make_version_record(header=header)

    assert record.header is header


def test_runtime_object_version_identity_is_supplied_by_header_record_id():
    record = make_version_record()

    assert record.header.record_id == "RR-000000202"
    assert not hasattr(record, "version_id")


def test_runtime_object_version_record_accepts_all_valid_optional_fields():
    record = make_version_record(
        version_label=VALID_VERSION_LABEL,
        predecessor_ref=VALID_PREDECESSOR_REF,
        branch_ref=VALID_BRANCH_REF,
        scope_ref=VALID_SCOPE_REF,
    )

    assert record.version_label == VALID_VERSION_LABEL
    assert record.predecessor_ref == VALID_PREDECESSOR_REF
    assert record.branch_ref == VALID_BRANCH_REF
    assert record.scope_ref == VALID_SCOPE_REF


def test_runtime_object_version_record_preserves_reference_values_exactly():
    record = make_version_record(
        object_ref=" object ",
        representation_ref=" representation ",
        version_label=" version ",
        predecessor_ref=" predecessor ",
        branch_ref=" branch ",
        scope_ref=" scope ",
    )

    assert record.object_ref == " object "
    assert record.representation_ref == " representation "
    assert record.version_label == " version "
    assert record.predecessor_ref == " predecessor "
    assert record.branch_ref == " branch "
    assert record.scope_ref == " scope "


def test_runtime_object_version_record_allows_equal_strings_across_semantic_fields():
    record = make_version_record(
        object_ref="same",
        representation_ref="same",
        version_label="same",
        branch_ref="same",
        scope_ref="same",
    )

    assert record.object_ref == "same"
    assert record.representation_ref == "same"
    assert record.version_label == "same"
    assert record.branch_ref == "same"
    assert record.scope_ref == "same"


@pytest.mark.parametrize(
    "missing_field",
    [
        "header",
        "object_ref",
        "representation_ref",
    ],
)
def test_runtime_object_version_record_requires_each_required_field(
    missing_field,
):
    values = {
        "header": make_version_header(),
        "object_ref": VALID_OBJECT_REF,
        "representation_ref": VALID_REPRESENTATION_REF,
    }
    values.pop(missing_field)

    with pytest.raises(TypeError):
        RuntimeObjectVersionRecord(**values)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        "RR-000000202",
        {},
        [],
        (),
        1,
        True,
    ],
)
def test_header_rejects_non_runtime_record_header_values(invalid_value):
    with pytest.raises(TypeError, match="header"):
        make_version_record(header=invalid_value)


def test_header_accepts_version_record_category():
    record = make_version_record(
        header=make_version_header(record_category="VERSION"),
    )

    assert record.header.record_category == "VERSION"


@pytest.mark.parametrize(
    "record_category",
    [
        "EVENT",
        "HOLD",
        "EVALUATION",
        "PROGRESSION_ASSERTION",
        "CUSTOM_RECORD",
    ],
)
def test_header_rejects_non_version_record_categories(
    record_category,
):
    header = make_version_header(
        record_category=record_category,
    )

    with pytest.raises(
        ValueError,
        match="header|record_category",
    ):
        make_version_record(header=header)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        1,
        1.0,
        True,
        b"research_os",
        [],
        {},
        (),
    ],
)
def test_object_ref_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="object_ref"):
        make_version_record(object_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "research_os",
        "OBJ-000001",
        "external/object/42",
        " object-ref ",
        "0",
        "x",
    ],
)
def test_object_ref_accepts_non_empty_strings(valid_value):
    record = make_version_record(object_ref=valid_value)

    assert record.object_ref == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_object_ref_rejects_empty_or_whitespace_only_values(
    invalid_value,
):
    with pytest.raises(ValueError, match="object_ref"):
        make_version_record(object_ref=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        1,
        1.0,
        True,
        b"REP-000001",
        [],
        {},
        (),
    ],
)
def test_representation_ref_rejects_non_string_values(
    invalid_value,
):
    with pytest.raises(TypeError, match="representation_ref"):
        make_version_record(
            representation_ref=invalid_value,
        )


@pytest.mark.parametrize(
    "valid_value",
    [
        "REP-000001",
        "artifact://representation/42",
        "content/object/version/1",
        " representation ",
        "0",
        "x",
    ],
)
def test_representation_ref_accepts_non_empty_strings(valid_value):
    record = make_version_record(
        representation_ref=valid_value,
    )

    assert record.representation_ref == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_representation_ref_rejects_empty_or_whitespace_only_values(
    invalid_value,
):
    with pytest.raises(ValueError, match="representation_ref"):
        make_version_record(
            representation_ref=invalid_value,
        )


@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"1",
        [],
        {},
        (),
    ],
)
def test_version_label_rejects_non_string_non_none_values(
    invalid_value,
):
    with pytest.raises(TypeError, match="version_label"):
        make_version_record(version_label=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "1",
        "2",
        "v1",
        "draft-2",
        "branch-a-3",
        " local label ",
        "0",
    ],
)
def test_version_label_accepts_non_empty_strings(valid_value):
    record = make_version_record(version_label=valid_value)

    assert record.version_label == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_version_label_rejects_empty_or_whitespace_only_values(
    invalid_value,
):
    with pytest.raises(ValueError, match="version_label"):
        make_version_record(version_label=invalid_value)


@pytest.mark.parametrize(
    "version_label",
    [
        "10",
        "2",
        "final",
        "draft",
    ],
)
def test_version_label_does_not_impose_format_or_ordering(
    version_label,
):
    record = make_version_record(
        version_label=version_label,
    )

    assert record.version_label == version_label


@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"RR-000000201",
        [],
        {},
        (),
    ],
)
def test_predecessor_ref_rejects_non_string_non_none_values(
    invalid_value,
):
    with pytest.raises(TypeError, match="predecessor_ref"):
        make_version_record(
            predecessor_ref=invalid_value,
        )


@pytest.mark.parametrize(
    "valid_value",
    [
        "RR-000000201",
        "legacy-version-1",
        "external/version/42",
        " predecessor ",
        "0",
    ],
)
def test_predecessor_ref_accepts_non_empty_strings(valid_value):
    record = make_version_record(
        predecessor_ref=valid_value,
    )

    assert record.predecessor_ref == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_predecessor_ref_rejects_empty_or_whitespace_only_values(
    invalid_value,
):
    with pytest.raises(ValueError, match="predecessor_ref"):
        make_version_record(
            predecessor_ref=invalid_value,
        )


def test_predecessor_ref_rejects_direct_self_reference():
    header = make_version_header(
        record_id="RR-000000202",
    )

    with pytest.raises(
        ValueError,
        match="predecessor_ref",
    ):
        make_version_record(
            header=header,
            predecessor_ref="RR-000000202",
        )


def test_predecessor_ref_does_not_require_runtime_record_id_syntax():
    predecessor_ref = "legacy-version-reference"

    record = make_version_record(
        predecessor_ref=predecessor_ref,
    )

    assert record.predecessor_ref == predecessor_ref


@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"BRANCH-000001",
        [],
        {},
        (),
    ],
)
def test_branch_ref_rejects_non_string_non_none_values(
    invalid_value,
):
    with pytest.raises(TypeError, match="branch_ref"):
        make_version_record(branch_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "BRANCH-000001",
        "main",
        "feature/a",
        " branch ",
        "0",
    ],
)
def test_branch_ref_accepts_non_empty_strings(valid_value):
    record = make_version_record(branch_ref=valid_value)

    assert record.branch_ref == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_branch_ref_rejects_empty_or_whitespace_only_values(
    invalid_value,
):
    with pytest.raises(ValueError, match="branch_ref"):
        make_version_record(branch_ref=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"SCOPE-000001",
        [],
        {},
        (),
    ],
)
def test_scope_ref_rejects_non_string_non_none_values(
    invalid_value,
):
    with pytest.raises(TypeError, match="scope_ref"):
        make_version_record(scope_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "SCOPE-000001",
        "research/program/1",
        "institutional",
        " scope ",
        "0",
    ],
)
def test_scope_ref_accepts_non_empty_strings(valid_value):
    record = make_version_record(scope_ref=valid_value)

    assert record.scope_ref == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_scope_ref_rejects_empty_or_whitespace_only_values(
    invalid_value,
):
    with pytest.raises(ValueError, match="scope_ref"):
        make_version_record(scope_ref=invalid_value)


@pytest.mark.parametrize(
    "field_name",
    [
        "version_label",
        "predecessor_ref",
        "branch_ref",
        "scope_ref",
    ],
)
def test_optional_fields_accept_none(field_name):
    record = make_version_record(
        **{field_name: None},
    )

    assert getattr(record, field_name) is None


def test_header_type_failure_precedes_required_reference_failures():
    with pytest.raises(TypeError, match="header"):
        RuntimeObjectVersionRecord(
            header={},
            object_ref=1,
            representation_ref=1,
            version_label=1,
            predecessor_ref=1,
            branch_ref=1,
            scope_ref=1,
        )


def test_header_category_failure_precedes_object_ref_failure():
    header = make_version_header(
        record_category="EVENT",
    )

    with pytest.raises(
        ValueError,
        match="header|record_category",
    ):
        RuntimeObjectVersionRecord(
            header=header,
            object_ref=1,
            representation_ref=1,
        )


def test_object_ref_type_failure_precedes_representation_ref_failure():
    with pytest.raises(TypeError, match="object_ref"):
        make_version_record(
            object_ref=1,
            representation_ref=1,
        )


def test_object_ref_value_failure_precedes_representation_ref_failure():
    with pytest.raises(ValueError, match="object_ref"):
        make_version_record(
            object_ref=" ",
            representation_ref=1,
        )


def test_representation_ref_failure_precedes_optional_field_failures():
    with pytest.raises(
        TypeError,
        match="representation_ref",
    ):
        make_version_record(
            representation_ref=1,
            version_label=1,
            predecessor_ref=1,
            branch_ref=1,
            scope_ref=1,
        )


def test_version_label_failure_precedes_predecessor_failure():
    with pytest.raises(TypeError, match="version_label"):
        make_version_record(
            version_label=1,
            predecessor_ref=1,
        )


def test_predecessor_failure_precedes_branch_failure():
    with pytest.raises(TypeError, match="predecessor_ref"):
        make_version_record(
            predecessor_ref=1,
            branch_ref=1,
        )


def test_self_predecessor_refusal_precedes_branch_and_scope_failures():
    header = make_version_header(
        record_id="RR-000000202",
    )

    with pytest.raises(
        ValueError,
        match="predecessor_ref",
    ):
        make_version_record(
            header=header,
            predecessor_ref="RR-000000202",
            branch_ref=1,
            scope_ref=1,
        )


def test_branch_failure_precedes_scope_failure():
    with pytest.raises(TypeError, match="branch_ref"):
        make_version_record(
            branch_ref=1,
            scope_ref=1,
        )


@pytest.mark.parametrize(
    ("field_name", "new_value"),
    [
        (
            "header",
            make_version_header(
                record_id="RR-000000203",
            ),
        ),
        ("object_ref", "object-2"),
        ("representation_ref", "REP-000002"),
        ("version_label", "2"),
        ("predecessor_ref", "RR-000000200"),
        ("branch_ref", "BRANCH-000002"),
        ("scope_ref", "SCOPE-000002"),
    ],
)
def test_runtime_object_version_record_is_frozen(
    field_name,
    new_value,
):
    record = make_version_record()

    with pytest.raises(FrozenInstanceError):
        setattr(record, field_name, new_value)


def test_identical_runtime_object_version_records_compare_equal():
    assert make_version_record() == make_version_record()


@pytest.mark.parametrize(
    ("field_name", "different_value"),
    [
        (
            "header",
            make_version_header(
                record_id="RR-000000203",
            ),
        ),
        ("object_ref", "object-2"),
        ("representation_ref", "REP-000002"),
        ("version_label", "2"),
        ("predecessor_ref", "RR-000000200"),
        ("branch_ref", "BRANCH-000002"),
        ("scope_ref", "SCOPE-000002"),
    ],
)
def test_runtime_object_version_record_equality_is_full_structural_equality(
    field_name,
    different_value,
):
    record_a = make_version_record()
    record_b = make_version_record(
        **{field_name: different_value},
    )

    assert record_a != record_b


def test_same_header_with_different_representation_ref_is_not_equal():
    header = make_version_header()

    record_a = make_version_record(
        header=header,
        representation_ref="REP-000001",
    )
    record_b = make_version_record(
        header=header,
        representation_ref="REP-000002",
    )

    assert record_a != record_b


def test_same_object_and_representation_with_different_header_is_not_equal():
    record_a = make_version_record(
        header=make_version_header(
            record_id="RR-000000202",
        ),
    )
    record_b = make_version_record(
        header=make_version_header(
            record_id="RR-000000203",
        ),
    )

    assert record_a.object_ref == record_b.object_ref
    assert (
        record_a.representation_ref
        == record_b.representation_ref
    )
    assert record_a != record_b


def test_same_header_object_and_representation_with_different_lineage_is_not_equal():
    header = make_version_header()

    record_a = make_version_record(
        header=header,
        predecessor_ref="RR-000000200",
    )
    record_b = make_version_record(
        header=header,
        predecessor_ref="RR-000000201",
    )

    assert record_a != record_b


def test_equal_runtime_object_version_records_have_equal_hashes():
    record_a = make_version_record()
    record_b = make_version_record()

    assert hash(record_a) == hash(record_b)


def test_structurally_different_runtime_object_version_records_can_coexist_in_a_set():
    record_a = make_version_record()
    record_b = make_version_record(
        header=make_version_header(
            record_id="RR-000000203",
        ),
    )

    assert len({record_a, record_b}) == 2


def test_hashing_does_not_change_runtime_object_version_record():
    record = make_version_record(
        version_label=VALID_VERSION_LABEL,
        predecessor_ref=VALID_PREDECESSOR_REF,
        branch_ref=VALID_BRANCH_REF,
        scope_ref=VALID_SCOPE_REF,
    )

    before = (
        record.header,
        record.object_ref,
        record.representation_ref,
        record.version_label,
        record.predecessor_ref,
        record.branch_ref,
        record.scope_ref,
    )

    hash(record)

    after = (
        record.header,
        record.object_ref,
        record.representation_ref,
        record.version_label,
        record.predecessor_ref,
        record.branch_ref,
        record.scope_ref,
    )

    assert after == before


def test_runtime_object_version_records_do_not_support_ordering():
    record_a = make_version_record()
    record_b = make_version_record(
        header=make_version_header(
            record_id="RR-000000203",
        ),
    )

    with pytest.raises(TypeError):
        _ = record_a < record_b


def test_runtime_object_version_record_exposes_no_serialization_methods():
    record = make_version_record()

    assert not hasattr(record, "to_dict")
    assert not hasattr(record, "from_dict")
    assert not hasattr(record, "to_json")
    assert not hasattr(record, "from_json")


def test_runtime_object_version_record_does_not_accept_legacy_object_dictionary_as_header():
    legacy_object = {
        "id": "research_os",
        "type": "project",
        "title": "Research OS",
        "status": "Active",
    }

    with pytest.raises(TypeError, match="header"):
        RuntimeObjectVersionRecord(
            header=legacy_object,
            object_ref=VALID_OBJECT_REF,
            representation_ref=VALID_REPRESENTATION_REF,
        )


def test_importing_runtime_object_version_record_does_not_import_object_engine():
    object_engine_was_loaded = (
        "src.services.object_engine" in sys.modules
    )

    module = importlib.import_module(
        "models.runtime_object_version_record"
    )

    assert hasattr(
        module,
        "RuntimeObjectVersionRecord",
    )

    if not object_engine_was_loaded:
        assert "src.services.object_engine" not in sys.modules


def test_importing_runtime_object_version_record_does_not_import_streamlit():
    streamlit_was_loaded = "streamlit" in sys.modules

    module = importlib.import_module(
        "models.runtime_object_version_record"
    )

    assert hasattr(
        module,
        "RuntimeObjectVersionRecord",
    )

    if not streamlit_was_loaded:
        assert "streamlit" not in sys.modules


def test_runtime_object_version_record_module_can_be_imported_directly():
    from models.runtime_object_version_record import (
        RuntimeObjectVersionRecord as ImportedRecord,
    )

    assert ImportedRecord is RuntimeObjectVersionRecord


def test_runtime_object_version_record_does_not_modify_composed_header():
    header = make_version_header(
        provenance_ref="PRV-000000001",
        external_id="external-version-202",
    )

    before = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    make_version_record(
        header=header,
        object_ref=VALID_OBJECT_REF,
        representation_ref=VALID_REPRESENTATION_REF,
        version_label=VALID_VERSION_LABEL,
        predecessor_ref=VALID_PREDECESSOR_REF,
        branch_ref=VALID_BRANCH_REF,
        scope_ref=VALID_SCOPE_REF,
    )

    after = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    assert after == before


def test_runtime_object_version_record_does_not_restrict_reference_prefixes():
    record = make_version_record(
        object_ref="custom-object",
        representation_ref="custom-representation",
        predecessor_ref="legacy-predecessor",
        branch_ref="custom-branch",
        scope_ref="custom-scope",
    )

    assert record.object_ref == "custom-object"
    assert record.representation_ref == "custom-representation"
    assert record.predecessor_ref == "legacy-predecessor"
    assert record.branch_ref == "custom-branch"
    assert record.scope_ref == "custom-scope"