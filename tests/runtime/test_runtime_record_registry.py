from dataclasses import FrozenInstanceError, dataclass, fields, is_dataclass
from datetime import datetime, timedelta, timezone
import importlib
import sys

import pytest

from models.hold_record import HoldRecord
from models.progression_assertion_record import ProgressionAssertionRecord
from models.runtime_event_record import RuntimeEventRecord
from models.runtime_object_version_record import RuntimeObjectVersionRecord
from models.runtime_record_identity import RuntimeRecordHeader
from models.runtime_record_registration_result import RuntimeRecordRegistrationResult
from services.runtime_record_registry import (
    RuntimeRecordDuplicateError,
    RuntimeRecordIdentityCollisionError,
    RuntimeRecordRegistry,
)

RECORDED = datetime(2026, 7, 17, 12, tzinfo=timezone.utc)


def make_header(record_id, category, **overrides):
    values = {
        "record_id": record_id,
        "record_category": category,
        "recorded_at": RECORDED,
        "schema_version": "1.0",
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)


def make_event(record_id="RR-000000501", **overrides):
    values = {
        "header": make_header(record_id, "EVENT"),
        "event_type": "CREATED",
    }
    values.update(overrides)
    return RuntimeEventRecord(**values)


def make_version(record_id="RR-000000502", **overrides):
    values = {
        "header": make_header(record_id, "VERSION"),
        "object_ref": "research_os",
        "representation_ref": "REP-000001",
    }
    values.update(overrides)
    return RuntimeObjectVersionRecord(**values)


def make_progression(record_id="RR-000000503", **overrides):
    values = {
        "header": make_header(record_id, "PROGRESSION_ASSERTION"),
        "target_ref": "research_os",
        "asserted_condition": "ACTIVE",
        "scope_ref": "SCOPE-000001",
    }
    values.update(overrides)
    return ProgressionAssertionRecord(**values)


def make_hold(record_id="RR-000000504", **overrides):
    values = {
        "header": make_header(record_id, "HOLD"),
        "target_ref": "research_os",
        "blocked_consequence_ref": "release",
        "scope_ref": "SCOPE-000001",
        "reason_ref": "REASON-000001",
        "resolution_condition_ref": "RESOLUTION-000001",
    }
    values.update(overrides)
    return HoldRecord(**values)


SUPPORTED_FACTORIES = [make_event, make_version, make_progression, make_hold]


def test_registration_result_is_a_dataclass():
    assert is_dataclass(RuntimeRecordRegistrationResult)


def test_registration_result_declares_exact_field_order():
    assert [f.name for f in fields(RuntimeRecordRegistrationResult)] == [
        "record_id",
        "append_position",
    ]


def test_registration_result_exposes_no_extra_fields():
    result = RuntimeRecordRegistrationResult("RR-000000501", 0)
    for name in (
        "status", "success", "registered", "duplicate", "collision",
        "record", "record_category", "registered_at", "persisted",
        "admitted", "authorized", "canonical", "registry_id", "storage_path",
    ):
        assert not hasattr(result, name)


@pytest.mark.parametrize("position", [0, 1, 2, 999])
def test_registration_result_accepts_valid_values(position):
    result = RuntimeRecordRegistrationResult("RR-000000501", position)
    assert result.record_id == "RR-000000501"
    assert result.append_position == position


@pytest.mark.parametrize("bad", [None, 1, 1.0, True, b"RR-000000001", [], {}, ()])
def test_result_record_id_rejects_non_string_values(bad):
    with pytest.raises(TypeError, match="record_id"):
        RuntimeRecordRegistrationResult(bad, 0)


@pytest.mark.parametrize("value", ["RR-000000001", "RR-000000501", "RR-999999999"])
def test_result_record_id_accepts_valid_values(value):
    assert RuntimeRecordRegistrationResult(value, 0).record_id == value


@pytest.mark.parametrize("bad", [
    "", " ", "RR-1", "rr-000000001", "RR-ABCDEFGHI",
    " RR-000000001 ", "R-000000001", "RR_000000001",
])
def test_result_record_id_rejects_invalid_syntax(bad):
    with pytest.raises(ValueError, match="record_id"):
        RuntimeRecordRegistrationResult(bad, 0)


def test_result_record_id_rejects_zero_identity():
    with pytest.raises(ValueError, match="record_id"):
        RuntimeRecordRegistrationResult("RR-000000000", 0)


@pytest.mark.parametrize("bad", [None, 1.0, "0", b"0", [], {}, ()])
def test_result_append_position_rejects_non_integer_values(bad):
    with pytest.raises(TypeError, match="append_position"):
        RuntimeRecordRegistrationResult("RR-000000501", bad)


@pytest.mark.parametrize("bad", [True, False])
def test_result_append_position_rejects_boolean_values(bad):
    with pytest.raises(TypeError, match="append_position"):
        RuntimeRecordRegistrationResult("RR-000000501", bad)


@pytest.mark.parametrize("bad", [-1, -2, -999])
def test_result_append_position_rejects_negative_values(bad):
    with pytest.raises(ValueError, match="append_position"):
        RuntimeRecordRegistrationResult("RR-000000501", bad)


def test_result_validation_precedence():
    with pytest.raises(TypeError, match="record_id"):
        RuntimeRecordRegistrationResult(1, -1)
    with pytest.raises(ValueError, match="record_id"):
        RuntimeRecordRegistrationResult("bad", -1)
    with pytest.raises(TypeError, match="append_position"):
        RuntimeRecordRegistrationResult("RR-000000501", True)


@pytest.mark.parametrize("field_name,value", [
    ("record_id", "RR-000000502"),
    ("append_position", 1),
])
def test_registration_result_is_frozen(field_name, value):
    result = RuntimeRecordRegistrationResult("RR-000000501", 0)
    with pytest.raises(FrozenInstanceError):
        setattr(result, field_name, value)


def test_registration_result_structural_equality_hashing_and_no_ordering():
    a = RuntimeRecordRegistrationResult("RR-000000501", 0)
    b = RuntimeRecordRegistrationResult("RR-000000501", 0)
    c = RuntimeRecordRegistrationResult("RR-000000502", 1)
    assert a == b
    assert a != c
    assert hash(a) == hash(b)
    assert len({a, c}) == 2
    with pytest.raises(TypeError):
        _ = a < c


def test_empty_registry_contract():
    registry = RuntimeRecordRegistry()
    assert registry.count() == 0
    assert registry.records() == ()
    assert registry.contains("RR-000000501") is False
    assert registry.records_by_category("EVENT") == ()
    with pytest.raises(KeyError, match="RR-000000501"):
        registry.get("RR-000000501")


@pytest.mark.parametrize("args,kwargs", [
    ((make_event(),), {}),
    ((), {"records": [make_event()]}),
])
def test_registry_rejects_constructor_arguments(args, kwargs):
    with pytest.raises(TypeError):
        RuntimeRecordRegistry(*args, **kwargs)


@pytest.mark.parametrize("factory", SUPPORTED_FACTORIES)
def test_registry_accepts_supported_exact_record_types(factory):
    registry = RuntimeRecordRegistry()
    record = factory()
    result = registry.register(record)
    assert isinstance(result, RuntimeRecordRegistrationResult)
    assert result.record_id == record.header.record_id
    assert result.append_position == 0
    assert registry.count() == 1
    assert registry.get(record.header.record_id) is record


@pytest.mark.parametrize("bad", [None, {}, [], (), "record", 1, True])
def test_registry_rejects_arbitrary_objects(bad):
    registry = RuntimeRecordRegistry()
    with pytest.raises(TypeError, match="record"):
        registry.register(bad)
    assert registry.records() == ()


def test_registry_rejects_bare_runtime_record_header():
    with pytest.raises(TypeError, match="record"):
        RuntimeRecordRegistry().register(make_header("RR-000000501", "EVENT"))


class ExplodingHeaderObject:
    @property
    def header(self):
        raise AssertionError("header must not be accessed")


def test_unsupported_type_fails_before_header_access():
    with pytest.raises(TypeError, match="record"):
        RuntimeRecordRegistry().register(ExplodingHeaderObject())


@dataclass
class ArbitraryDataclass:
    header: RuntimeRecordHeader


def test_registry_rejects_arbitrary_dataclass():
    value = ArbitraryDataclass(make_header("RR-000000501", "EVENT"))
    with pytest.raises(TypeError, match="record"):
        RuntimeRecordRegistry().register(value)


class EventSubclass(RuntimeEventRecord):
    pass


class VersionSubclass(RuntimeObjectVersionRecord):
    pass


class ProgressionSubclass(ProgressionAssertionRecord):
    pass


class HoldSubclass(HoldRecord):
    pass


@pytest.mark.parametrize("record", [
    EventSubclass(make_header("RR-000000511", "EVENT"), "CREATED"),
    VersionSubclass(make_header("RR-000000512", "VERSION"), "research_os", "REP-000001"),
    ProgressionSubclass(
        make_header("RR-000000513", "PROGRESSION_ASSERTION"),
        "research_os", "ACTIVE", "SCOPE-000001",
    ),
    HoldSubclass(
        make_header("RR-000000514", "HOLD"),
        "research_os", "release", "SCOPE-000001",
        "REASON-000001", "RESOLUTION-000001",
    ),
])
def test_registry_rejects_supported_record_subclasses(record):
    registry = RuntimeRecordRegistry()
    with pytest.raises(TypeError, match="record"):
        registry.register(record)
    assert registry.count() == 0


def test_zero_based_append_positions_equal_prior_count():
    registry = RuntimeRecordRegistry()
    for expected, factory in enumerate(SUPPORTED_FACTORIES):
        assert registry.count() == expected
        result = registry.register(factory())
        assert result.append_position == expected


def test_count_changes_only_after_successful_unique_registration():
    registry = RuntimeRecordRegistry()
    for expected, factory in enumerate(SUPPORTED_FACTORIES, start=1):
        registry.register(factory())
        assert registry.count() == expected
    registry.get("RR-000000501")
    registry.contains("RR-000000502")
    registry.records_by_category("EVENT")
    assert registry.count() == 4


@pytest.mark.parametrize("factory", SUPPORTED_FACTORIES)
def test_registration_preserves_exact_instance_and_record_structure(factory):
    registry = RuntimeRecordRegistry()
    record = factory()
    before = tuple(getattr(record, f.name) for f in fields(record))
    registry.register(record)
    after = tuple(getattr(record, f.name) for f in fields(record))
    assert registry.get(record.header.record_id) is record
    assert registry.records()[0] is record
    assert registry.records_by_category(record.header.record_category)[0] is record
    assert after == before


def test_registry_preserves_registration_order_without_sorting():
    registry = RuntimeRecordRegistry()
    records = [
        make_hold("RR-000000599"),
        make_event(
            "RR-000000501",
            header=make_header(
                "RR-000000501", "EVENT",
                recorded_at=RECORDED + timedelta(days=1),
            ),
        ),
        make_progression("RR-000000503"),
        make_version(
            "RR-000000502",
            header=make_header(
                "RR-000000502", "VERSION",
                recorded_at=RECORDED - timedelta(days=1),
            ),
        ),
    ]
    for record in records:
        registry.register(record)
    assert registry.records() == tuple(records)


@pytest.mark.parametrize("factory", SUPPORTED_FACTORIES)
def test_equal_record_with_occupied_identity_raises_duplicate(factory):
    registry = RuntimeRecordRegistry()
    existing = factory()
    registry.register(existing)
    before = registry.records()
    with pytest.raises(RuntimeRecordDuplicateError, match=existing.header.record_id):
        registry.register(factory())
    assert registry.records() == before
    assert registry.count() == 1
    assert registry.get(existing.header.record_id) is existing


@pytest.mark.parametrize("existing,incoming", [
    (make_event(), make_event(event_type="UPDATED")),
    (make_version(), make_version(representation_ref="REP-000002")),
    (make_progression(), make_progression(asserted_condition="HELD")),
    (make_hold(), make_hold(reason_ref="REASON-000002")),
    (make_event("RR-000000550"), make_hold("RR-000000550")),
])
def test_same_identity_with_different_structure_raises_collision(existing, incoming):
    registry = RuntimeRecordRegistry()
    registry.register(existing)
    before = registry.records()
    with pytest.raises(
        RuntimeRecordIdentityCollisionError,
        match=existing.header.record_id,
    ):
        registry.register(incoming)
    assert registry.records() == before
    assert registry.count() == 1
    assert registry.get(existing.header.record_id) is existing


def test_duplicate_and_collision_exceptions_are_distinct_direct_exception_types():
    assert RuntimeRecordDuplicateError.__bases__ == (Exception,)
    assert RuntimeRecordIdentityCollisionError.__bases__ == (Exception,)
    assert RuntimeRecordDuplicateError is not RuntimeRecordIdentityCollisionError
    assert not issubclass(RuntimeRecordDuplicateError, RuntimeRecordIdentityCollisionError)
    assert not issubclass(RuntimeRecordIdentityCollisionError, RuntimeRecordDuplicateError)


def test_failed_registration_is_atomic_for_populated_registry():
    registry = RuntimeRecordRegistry()
    first = make_event()
    second = make_version()
    registry.register(first)
    registry.register(second)
    before = registry.records()
    before_ids = tuple(id(record) for record in before)
    with pytest.raises(TypeError):
        registry.register({})
    assert registry.records() == before
    assert tuple(id(record) for record in registry.records()) == before_ids


@pytest.mark.parametrize("bad", [None, 1, 1.0, True, b"RR-000000501", [], {}, ()])
def test_get_rejects_non_string_record_ids(bad):
    with pytest.raises(TypeError, match="record_id"):
        RuntimeRecordRegistry().get(bad)


@pytest.mark.parametrize("missing", ["", " ", "invalid", "RR-1", "rr-000000501", " RR-000000501 "])
def test_get_uses_exact_lookup_and_arbitrary_strings_are_missing(missing):
    with pytest.raises(KeyError):
        RuntimeRecordRegistry().get(missing)


def test_get_returns_exact_registered_record():
    registry = RuntimeRecordRegistry()
    record = make_event()
    registry.register(record)
    assert registry.get("RR-000000501") is record
    with pytest.raises(KeyError):
        registry.get("rr-000000501")
    with pytest.raises(KeyError):
        registry.get(" RR-000000501 ")


@pytest.mark.parametrize("bad", [None, 1, 1.0, True, b"RR-000000501", [], {}, ()])
def test_contains_rejects_non_string_record_ids(bad):
    with pytest.raises(TypeError, match="record_id"):
        RuntimeRecordRegistry().contains(bad)


def test_contains_uses_exact_membership_without_normalization():
    registry = RuntimeRecordRegistry()
    registry.register(make_event())
    assert registry.contains("RR-000000501") is True
    for missing in ("RR-000000999", "", " ", "invalid", "RR-1", "rr-000000501", " RR-000000501 "):
        assert registry.contains(missing) is False


def test_records_returns_immutable_snapshot_and_old_snapshot_is_stable():
    registry = RuntimeRecordRegistry()
    first = make_event()
    second = make_version()
    registry.register(first)
    old_snapshot = registry.records()
    assert isinstance(old_snapshot, tuple)
    with pytest.raises(AttributeError):
        old_snapshot.append(second)
    registry.register(second)
    assert old_snapshot == (first,)
    assert registry.records() == (first, second)


@pytest.mark.parametrize("bad", [None, 1, 1.0, True, b"EVENT", [], {}, ()])
def test_records_by_category_rejects_non_string_values(bad):
    with pytest.raises(TypeError, match="record_category"):
        RuntimeRecordRegistry().records_by_category(bad)


@pytest.mark.parametrize("bad", ["", " ", "\t", "\n", "\r\n"])
def test_records_by_category_rejects_whitespace_only_values(bad):
    with pytest.raises(ValueError, match="record_category"):
        RuntimeRecordRegistry().records_by_category(bad)


def test_records_by_category_is_exact_ordered_and_returns_tuple():
    registry = RuntimeRecordRegistry()
    first = make_event("RR-000000501")
    middle = make_hold("RR-000000502")
    second = make_event("RR-000000503", event_type="UPDATED")
    for record in (first, middle, second):
        registry.register(record)
    assert registry.records_by_category("EVENT") == (first, second)
    assert isinstance(registry.records_by_category("EVENT"), tuple)
    assert registry.records_by_category("event") == ()
    assert registry.records_by_category(" EVENT ") == ()
    assert registry.records_by_category("UNKNOWN_CATEGORY") == ()


def test_category_snapshot_remains_stable_after_later_registration():
    registry = RuntimeRecordRegistry()
    first = make_event("RR-000000501")
    registry.register(first)
    snapshot = registry.records_by_category("EVENT")
    registry.register(make_event("RR-000000502", event_type="UPDATED"))
    assert snapshot == (first,)


def test_registry_exposes_required_public_methods():
    registry = RuntimeRecordRegistry()
    for name in ("register", "get", "contains", "count", "records", "records_by_category"):
        assert callable(getattr(registry, name))


@pytest.mark.parametrize("name", [
    "add", "append", "insert", "store", "register_many", "remove",
    "delete", "replace", "update", "upsert", "clear", "reset",
    "load", "save", "persist", "serialize", "deserialize", "admit",
    "authorize", "project", "reconstruct",
])
def test_registry_exposes_no_prohibited_methods(name):
    assert not hasattr(RuntimeRecordRegistry(), name)


@pytest.mark.parametrize("name", [
    "__len__", "__iter__", "__contains__", "__getitem__", "__setitem__", "__delitem__",
])
def test_registry_defines_no_prohibited_protocol_methods(name):
    assert name not in RuntimeRecordRegistry.__dict__


@pytest.mark.parametrize("name", ["records_by_id", "records_list", "entries", "storage", "items"])
def test_registry_exposes_no_public_mutable_storage(name):
    assert not hasattr(RuntimeRecordRegistry(), name)


def test_registry_uses_instance_identity_equality_and_no_custom_hash():
    first = RuntimeRecordRegistry()
    second = RuntimeRecordRegistry()
    first.register(make_event())
    second.register(make_event())
    assert first != second
    assert "__eq__" not in RuntimeRecordRegistry.__dict__
    assert "__hash__" not in RuntimeRecordRegistry.__dict__


def test_registration_and_result_expose_no_admission_or_persistence_semantics():
    registry = RuntimeRecordRegistry()
    hold = make_hold()
    result = registry.register(hold)
    for name in (
        "admitted", "accepted", "approved", "authorized", "valid",
        "canonical", "active", "current", "persisted", "durable",
        "committed", "storage_path", "database_id", "file_offset",
    ):
        assert not hasattr(result, name)
    for name in ("admit", "approve", "authorize", "save", "load", "persist", "restore"):
        assert not hasattr(registry, name)
    assert not hasattr(hold, "active")
    assert not hasattr(hold, "authorized")


def test_registering_record_creates_no_files(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    before = set(tmp_path.iterdir())
    RuntimeRecordRegistry().register(make_event())
    assert set(tmp_path.iterdir()) == before


def test_registry_exposes_no_canonical_projection_or_telemetry():
    registry = RuntimeRecordRegistry()
    for name in (
        "current_record", "latest_record", "active_hold", "current_progression",
        "canonical", "duplicate_attempt_count", "collision_count",
        "failed_registration_count", "lookup_count", "registration_time",
    ):
        assert not hasattr(registry, name)


def test_registry_preserves_semantically_conflicting_records_with_distinct_ids():
    registry = RuntimeRecordRegistry()
    active = make_progression("RR-000000503", asserted_condition="ACTIVE")
    held = make_progression("RR-000000505", asserted_condition="HELD")
    registry.register(active)
    registry.register(held)
    assert registry.records() == (active, held)


@pytest.mark.parametrize("module_name", [
    "src.services.platform_registry", "src.services.object_engine",
    "src.services.event_engine", "src.kernel.kernel", "streamlit",
])
def test_importing_registry_does_not_import_application_modules(module_name):
    was_loaded = module_name in sys.modules
    module = importlib.import_module("services.runtime_record_registry")
    assert hasattr(module, "RuntimeRecordRegistry")
    if not was_loaded:
        assert module_name not in sys.modules


def test_modules_and_exceptions_can_be_imported_directly():
    from models.runtime_record_registration_result import RuntimeRecordRegistrationResult as ImportedResult
    from services.runtime_record_registry import (
        RuntimeRecordDuplicateError as ImportedDuplicate,
        RuntimeRecordIdentityCollisionError as ImportedCollision,
        RuntimeRecordRegistry as ImportedRegistry,
    )
    assert ImportedResult is RuntimeRecordRegistrationResult
    assert ImportedRegistry is RuntimeRecordRegistry
    assert ImportedDuplicate is RuntimeRecordDuplicateError
    assert ImportedCollision is RuntimeRecordIdentityCollisionError


def test_registration_does_not_generate_runtime_events():
    registry = RuntimeRecordRegistry()
    registry.register(make_hold())
    assert not hasattr(registry, "events")
    with pytest.raises(RuntimeRecordDuplicateError):
        registry.register(make_hold())
    assert not hasattr(registry, "events")


def test_append_position_does_not_imply_semantic_order_or_currentness():
    registry = RuntimeRecordRegistry()
    first = make_event(
        "RR-000000599",
        header=make_header(
            "RR-000000599", "EVENT",
            recorded_at=RECORDED + timedelta(days=1),
        ),
    )
    second = make_version(
        "RR-000000501",
        header=make_header(
            "RR-000000501", "VERSION",
            recorded_at=RECORDED - timedelta(days=1),
        ),
    )
    first_result = registry.register(first)
    second_result = registry.register(second)
    assert first_result.append_position == 0
    assert second_result.append_position == 1
    assert not hasattr(first_result, "current")
    assert not hasattr(second_result, "canonical")


def test_distinct_correction_supersession_and_release_related_records_preserve_originals():
    registry = RuntimeRecordRegistry()
    original_event = make_event("RR-000000501", event_type="CREATED")
    correction = make_event("RR-000000505", event_type="CORRECTED")
    original_version = make_version("RR-000000502")
    later_version = make_version(
        "RR-000000506",
        representation_ref="REP-000002",
        predecessor_ref="RR-000000502",
    )
    hold = make_hold("RR-000000504")
    release_event = make_event(
        "RR-000000507",
        event_type="RELEASED",
        target_ref=hold.header.record_id,
    )
    hold_before = tuple(getattr(hold, f.name) for f in fields(hold))
    for record in (original_event, correction, original_version, later_version, hold, release_event):
        registry.register(record)
    assert registry.records() == (
        original_event, correction, original_version, later_version, hold, release_event,
    )
    assert tuple(getattr(hold, f.name) for f in fields(hold)) == hold_before