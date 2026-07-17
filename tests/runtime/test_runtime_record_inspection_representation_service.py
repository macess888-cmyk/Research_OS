from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from services.runtime_record_inspection_representation_service import (
    RuntimeRecordInspectionRepresentationService,
)


TOP_LEVEL_KEYS = [
    "record_id",
    "record_type",
    "record_category",
    "append_position",
    "recorded_at",
    "schema_version",
    "provenance_ref",
    "external_id",
    "declared_fields",
]

PROHIBITED_METHODS = {
    "to_dict",
    "to_json",
    "serialize",
    "deserialize",
    "from_dict",
    "from_json",
    "from_primitive_dict",
    "encode",
    "decode",
    "dump",
    "dumps",
    "load",
    "loads",
    "save",
    "persist",
    "export",
    "write",
    "read",
    "hash",
    "digest",
    "checksum",
    "sign",
    "verify",
    "redact",
    "mask",
    "classify",
    "publish",
    "upload",
    "download",
    "inspect",
    "health",
    "status",
    "represent_collection",
    "to_primitive_list",
    "to_primitive_tuple",
}

PROHIBITED_OUTPUT_KEYS = {
    "representation_version",
    "serializer_version",
    "format_version",
    "schema_id",
    "inspection_id",
    "snapshot_id",
    "created_at",
    "represented_at",
    "serialized_at",
    "exported_at",
    "registry_id",
    "registry_version",
    "source_commit",
    "hash",
    "digest",
    "signature",
    "status",
    "healthy",
    "valid",
    "validity",
    "admitted",
    "admission_status",
    "authorized",
    "authority_valid",
    "canonical",
    "current",
    "active",
    "persistent",
    "persisted",
    "public",
    "publishable",
    "disclosure_authorized",
    "sharing_allowed",
    "export_authorized",
    "redacted",
    "source_report",
    "report",
    "registry",
}


def make_event_report(
    *,
    recorded_at: datetime | None = None,
    occurred_at: datetime | None = None,
    effective_at: datetime | None = None,
    provenance_ref: str | None = "PRV-000000001",
    external_id: str | None = "external-α",
) -> RuntimeRecordInspectionReport:
    recorded = recorded_at or datetime(
        2026,
        7,
        17,
        12,
        30,
        45,
        123456,
        tzinfo=timezone.utc,
    )

    return RuntimeRecordInspectionReport(
        record_id="RR-000000001",
        record_type="RuntimeEventRecord",
        record_category="EVENT",
        append_position=0,
        recorded_at=recorded,
        schema_version="1.0",
        provenance_ref=provenance_ref,
        external_id=external_id,
        declared_fields=(
            ("event_type", " OBJECT_CREATED "),
            ("target_ref", "OBJ-α"),
            ("actor_ref", None),
            ("source_ref", "SRC-001"),
            ("scope_ref", None),
            ("branch_ref", "BRANCH-main"),
            ("occurred_at", occurred_at),
            ("effective_at", effective_at),
        ),
    )


def make_version_report() -> RuntimeRecordInspectionReport:
    return RuntimeRecordInspectionReport(
        record_id="RR-000000002",
        record_type="RuntimeObjectVersionRecord",
        record_category="VERSION",
        append_position=1,
        recorded_at=datetime(
            2026,
            7,
            17,
            13,
            0,
            tzinfo=timezone(timedelta(hours=-7)),
        ),
        schema_version="1.0",
        provenance_ref=None,
        external_id=None,
        declared_fields=(
            ("object_ref", "OBJ-001"),
            ("representation_ref", "REP-001"),
            ("version_label", "v1.0"),
            ("predecessor_ref", None),
            ("branch_ref", "main"),
            ("scope_ref", None),
        ),
    )


def make_progression_report() -> RuntimeRecordInspectionReport:
    asserted_at = datetime(
        2026,
        7,
        17,
        14,
        15,
        16,
        654321,
        tzinfo=timezone(timedelta(hours=5, minutes=30)),
    )

    return RuntimeRecordInspectionReport(
        record_id="RR-000000003",
        record_type="ProgressionAssertionRecord",
        record_category="PROGRESSION_ASSERTION",
        append_position=2,
        recorded_at=datetime(
            2026,
            7,
            17,
            8,
            45,
            tzinfo=timezone.utc,
        ),
        schema_version="2.1",
        provenance_ref="PRV-000000002",
        external_id="progression-external",
        declared_fields=(
            ("target_ref", "OBJ-001"),
            ("asserted_condition", "ACTIVE"),
            ("scope_ref", "SCOPE-001"),
            ("target_version_ref", "VER-001"),
            ("prior_condition", "PENDING"),
            ("branch_ref", "main"),
            ("context_ref", None),
            ("asserted_at", asserted_at),
            ("effective_at", None),
            ("actor_ref", "ACTOR-001"),
            ("source_ref", "SOURCE-001"),
            ("basis_ref", None),
        ),
    )


def make_hold_report() -> RuntimeRecordInspectionReport:
    placed_at = datetime(
        2026,
        7,
        17,
        9,
        10,
        tzinfo=timezone.utc,
    )
    review_at = datetime(
        2026,
        7,
        18,
        9,
        10,
        tzinfo=timezone.utc,
    )

    return RuntimeRecordInspectionReport(
        record_id="RR-000000004",
        record_type="HoldRecord",
        record_category="HOLD",
        append_position=3,
        recorded_at=datetime(
            2026,
            7,
            17,
            9,
            11,
            tzinfo=timezone.utc,
        ),
        schema_version="1.0",
        provenance_ref="PRV-000000003",
        external_id=None,
        declared_fields=(
            ("target_ref", "OBJ-001"),
            ("blocked_consequence_ref", "CONSEQUENCE-001"),
            ("scope_ref", "SCOPE-001"),
            ("reason_ref", "REASON-001"),
            ("resolution_condition_ref", "RESOLUTION-001"),
            ("target_version_ref", None),
            ("branch_ref", "main"),
            ("context_ref", None),
            ("trigger_ref", "TRIGGER-001"),
            ("basis_ref", None),
            ("owner_ref", "OWNER-001"),
            ("placed_by_ref", "ACTOR-001"),
            ("placement_authority_ref", "AUTH-PLACE-001"),
            ("release_authority_ref", "AUTH-RELEASE-001"),
            ("placed_at", placed_at),
            ("effective_at", placed_at),
            ("review_at", review_at),
            ("expires_at", None),
        ),
    )


@pytest.fixture
def service() -> RuntimeRecordInspectionRepresentationService:
    return RuntimeRecordInspectionRepresentationService()


@pytest.fixture
def event_report() -> RuntimeRecordInspectionReport:
    return make_event_report(
        occurred_at=datetime(
            2026,
            7,
            17,
            5,
            30,
            45,
            123456,
            tzinfo=timezone(timedelta(hours=-7)),
        ),
        effective_at=datetime(
            2026,
            7,
            17,
            12,
            30,
            45,
            tzinfo=timezone.utc,
        ),
    )


def test_service_constructs_without_arguments() -> None:
    service = RuntimeRecordInspectionRepresentationService()

    assert type(service) is RuntimeRecordInspectionRepresentationService


def test_service_instances_have_no_required_state() -> None:
    first = RuntimeRecordInspectionRepresentationService()
    second = RuntimeRecordInspectionRepresentationService()

    assert vars(first) == {}
    assert vars(second) == {}


@pytest.mark.parametrize(
    "invalid_report",
    [
        None,
        {},
        [],
        (),
        "report",
        1,
        object(),
    ],
)
def test_rejects_non_report_inputs(
    service: RuntimeRecordInspectionRepresentationService,
    invalid_report: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="report must be an exact RuntimeRecordInspectionReport",
    ):
        service.to_primitive_dict(invalid_report)  # type: ignore[arg-type]


def test_rejects_report_subclass(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    class DerivedReport(RuntimeRecordInspectionReport):
        pass

    derived = DerivedReport(
        record_id=event_report.record_id,
        record_type=event_report.record_type,
        record_category=event_report.record_category,
        append_position=event_report.append_position,
        recorded_at=event_report.recorded_at,
        schema_version=event_report.schema_version,
        provenance_ref=event_report.provenance_ref,
        external_id=event_report.external_id,
        declared_fields=event_report.declared_fields,
    )

    with pytest.raises(
        TypeError,
        match="report must be an exact RuntimeRecordInspectionReport",
    ):
        service.to_primitive_dict(derived)


def test_returns_exact_plain_dict(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert type(result) is dict


def test_preserves_exact_top_level_key_order(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert list(result.keys()) == TOP_LEVEL_KEYS


def test_preserves_exact_top_level_values(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert result["record_id"] == event_report.record_id
    assert result["record_type"] == event_report.record_type
    assert result["record_category"] == event_report.record_category
    assert result["append_position"] == event_report.append_position
    assert result["recorded_at"] == event_report.recorded_at.isoformat()
    assert result["schema_version"] == event_report.schema_version
    assert result["provenance_ref"] == event_report.provenance_ref
    assert result["external_id"] == event_report.external_id


def test_recorded_at_is_string(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert type(result["recorded_at"]) is str


def test_preserves_utc_offset_without_z_conversion(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    report = make_event_report(
        recorded_at=datetime(
            2026,
            7,
            17,
            12,
            0,
            tzinfo=timezone.utc,
        )
    )

    result = service.to_primitive_dict(report)

    assert result["recorded_at"] == "2026-07-17T12:00:00+00:00"
    assert not str(result["recorded_at"]).endswith("Z")


@pytest.mark.parametrize(
    ("offset", "expected_suffix"),
    [
        (timedelta(hours=-7), "-07:00"),
        (timedelta(hours=5, minutes=30), "+05:30"),
    ],
)
def test_preserves_non_utc_offsets(
    service: RuntimeRecordInspectionRepresentationService,
    offset: timedelta,
    expected_suffix: str,
) -> None:
    report = make_event_report(
        recorded_at=datetime(
            2026,
            7,
            17,
            12,
            0,
            tzinfo=timezone(offset),
        )
    )

    result = service.to_primitive_dict(report)

    assert str(result["recorded_at"]).endswith(expected_suffix)


def test_preserves_recorded_at_microseconds(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    report = make_event_report(
        recorded_at=datetime(
            2026,
            7,
            17,
            12,
            0,
            0,
            123456,
            tzinfo=timezone.utc,
        )
    )

    result = service.to_primitive_dict(report)

    assert result["recorded_at"] == (
        "2026-07-17T12:00:00.123456+00:00"
    )


def test_preserves_optional_none_values(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    report = make_event_report(
        provenance_ref=None,
        external_id=None,
        occurred_at=None,
        effective_at=None,
    )

    result = service.to_primitive_dict(report)

    assert "provenance_ref" in result
    assert result["provenance_ref"] is None
    assert "external_id" in result
    assert result["external_id"] is None

    declared = dict(result["declared_fields"])
    assert "occurred_at" in declared
    assert declared["occurred_at"] is None
    assert "effective_at" in declared
    assert declared["effective_at"] is None


def test_preserves_strings_exactly(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    report = make_event_report(external_id="  Éxternal-Δ  ")

    result = service.to_primitive_dict(report)

    assert result["external_id"] == "  Éxternal-Δ  "
    assert result["declared_fields"][0][1] == " OBJECT_CREATED "
    assert result["declared_fields"][1][1] == "OBJ-α"


def test_preserves_append_position_as_exact_integer(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert type(result["append_position"]) is int
    assert result["append_position"] == 0


def test_declared_fields_is_exact_plain_list(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert type(result["declared_fields"]) is list


def test_each_declared_field_entry_is_exact_two_item_list(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    for entry in result["declared_fields"]:
        assert type(entry) is list
        assert len(entry) == 2


def test_preserves_event_declared_field_order(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert [entry[0] for entry in result["declared_fields"]] == [
        "event_type",
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
        "occurred_at",
        "effective_at",
    ]


def test_converts_declared_datetime_values(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)
    declared = dict(result["declared_fields"])

    assert declared["occurred_at"] == (
        "2026-07-17T05:30:45.123456-07:00"
    )
    assert declared["effective_at"] == (
        "2026-07-17T12:30:45+00:00"
    )


def test_preserves_version_declared_field_order(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    result = service.to_primitive_dict(make_version_report())

    assert [entry[0] for entry in result["declared_fields"]] == [
        "object_ref",
        "representation_ref",
        "version_label",
        "predecessor_ref",
        "branch_ref",
        "scope_ref",
    ]


def test_preserves_progression_declared_field_order(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    result = service.to_primitive_dict(make_progression_report())

    assert [entry[0] for entry in result["declared_fields"]] == [
        "target_ref",
        "asserted_condition",
        "scope_ref",
        "target_version_ref",
        "prior_condition",
        "branch_ref",
        "context_ref",
        "asserted_at",
        "effective_at",
        "actor_ref",
        "source_ref",
        "basis_ref",
    ]

    declared = dict(result["declared_fields"])
    assert declared["asserted_at"] == (
        "2026-07-17T14:15:16.654321+05:30"
    )
    assert declared["effective_at"] is None


def test_preserves_hold_declared_field_order(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    result = service.to_primitive_dict(make_hold_report())

    assert [entry[0] for entry in result["declared_fields"]] == [
        "target_ref",
        "blocked_consequence_ref",
        "scope_ref",
        "reason_ref",
        "resolution_condition_ref",
        "target_version_ref",
        "branch_ref",
        "context_ref",
        "trigger_ref",
        "basis_ref",
        "owner_ref",
        "placed_by_ref",
        "placement_authority_ref",
        "release_authority_ref",
        "placed_at",
        "effective_at",
        "review_at",
        "expires_at",
    ]


def test_preserves_hold_authority_references_without_derivation(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    result = service.to_primitive_dict(make_hold_report())
    declared = dict(result["declared_fields"])

    assert declared["placement_authority_ref"] == "AUTH-PLACE-001"
    assert declared["release_authority_ref"] == "AUTH-RELEASE-001"


def test_repeated_calls_are_equal(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    first = service.to_primitive_dict(event_report)
    second = service.to_primitive_dict(event_report)

    assert first == second


def test_repeated_calls_return_fresh_top_level_dicts(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    first = service.to_primitive_dict(event_report)
    second = service.to_primitive_dict(event_report)

    assert first is not second


def test_repeated_calls_return_fresh_declared_fields_lists(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    first = service.to_primitive_dict(event_report)
    second = service.to_primitive_dict(event_report)

    assert first["declared_fields"] is not second["declared_fields"]


def test_repeated_calls_return_fresh_inner_pair_lists(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    first = service.to_primitive_dict(event_report)
    second = service.to_primitive_dict(event_report)

    for first_pair, second_pair in zip(
        first["declared_fields"],
        second["declared_fields"],
        strict=True,
    ):
        assert first_pair is not second_pair


def test_mutating_result_does_not_mutate_report(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    original_fields = event_report.declared_fields
    original_record_id = event_report.record_id

    result = service.to_primitive_dict(event_report)
    result["record_id"] = "changed"
    result["declared_fields"][0][0] = "changed_name"
    result["declared_fields"].append(["new", "value"])

    assert event_report.record_id == original_record_id
    assert event_report.declared_fields == original_fields


def test_mutating_one_result_does_not_affect_later_result(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    first = service.to_primitive_dict(event_report)
    first["record_id"] = "changed"
    first["declared_fields"][0][1] = "changed"

    second = service.to_primitive_dict(event_report)

    assert second["record_id"] == event_report.record_id
    assert second["declared_fields"][0][1] == " OBJECT_CREATED "


def test_representation_does_not_change_source_report(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    before = event_report

    service.to_primitive_dict(event_report)

    assert event_report == before


def test_two_service_instances_produce_equal_output(
    event_report: RuntimeRecordInspectionReport,
) -> None:
    first_service = RuntimeRecordInspectionRepresentationService()
    second_service = RuntimeRecordInspectionRepresentationService()

    assert (
        first_service.to_primitive_dict(event_report)
        == second_service.to_primitive_dict(event_report)
    )


def test_service_exposes_no_prohibited_methods(
    service: RuntimeRecordInspectionRepresentationService,
) -> None:
    for method_name in PROHIBITED_METHODS:
        assert not hasattr(service, method_name)


def test_output_contains_no_prohibited_keys(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
) -> None:
    result = service.to_primitive_dict(event_report)

    assert PROHIBITED_OUTPUT_KEYS.isdisjoint(result.keys())


@pytest.mark.parametrize(
    "collection",
    [
        [],
        (),
        [make_event_report()],
        (make_event_report(),),
    ],
)
def test_rejects_collection_inputs(
    service: RuntimeRecordInspectionRepresentationService,
    collection: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="report must be an exact RuntimeRecordInspectionReport",
    ):
        service.to_primitive_dict(collection)  # type: ignore[arg-type]


def test_service_does_not_inherit_platform_inspectable() -> None:
    from src.services.inspectable import Inspectable

    assert not issubclass(
        RuntimeRecordInspectionRepresentationService,
        Inspectable,
    )


def test_production_source_contains_no_prohibited_imports() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_representation_service.py"
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
        "import hashlib",
        "from hashlib",
        "runtime_record_registry",
        "runtime_record_inspector",
        "src.services.inspectable",
        "event_engine",
        "dataclasses.asdict",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_current_time_generation() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_representation_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source


def test_representation_creates_no_files(
    service: RuntimeRecordInspectionRepresentationService,
    event_report: RuntimeRecordInspectionReport,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_primitive_dict(event_report)

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before