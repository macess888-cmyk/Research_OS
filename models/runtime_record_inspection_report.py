from dataclasses import dataclass
from datetime import datetime
import re


_RECORD_ID_PATTERN = re.compile(r"^RR-(\d{9})$")
_PROVENANCE_REF_PATTERN = re.compile(r"^PRV-(\d{9})$")
_SCHEMA_VERSION_PATTERN = re.compile(r"^(\d+)\.(\d+)$")

_SUPPORTED_CONDITIONS = {
    "PENDING",
    "ACTIVE",
    "HELD",
    "DORMANT",
    "ABANDONED",
}

_TYPE_CATEGORY_MAP = {
    "RuntimeEventRecord": "EVENT",
    "RuntimeObjectVersionRecord": "VERSION",
    "ProgressionAssertionRecord": "PROGRESSION_ASSERTION",
    "HoldRecord": "HOLD",
}

_DECLARED_FIELD_CONTRACTS = {
    "RuntimeEventRecord": (
        "event_type",
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
        "occurred_at",
        "effective_at",
    ),
    "RuntimeObjectVersionRecord": (
        "object_ref",
        "representation_ref",
        "version_label",
        "predecessor_ref",
        "branch_ref",
        "scope_ref",
    ),
    "ProgressionAssertionRecord": (
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
    ),
    "HoldRecord": (
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
    ),
}

_REQUIRED_STRING_FIELDS = {
    "RuntimeEventRecord": {
        "event_type",
    },
    "RuntimeObjectVersionRecord": {
        "object_ref",
        "representation_ref",
    },
    "ProgressionAssertionRecord": {
        "target_ref",
        "asserted_condition",
        "scope_ref",
    },
    "HoldRecord": {
        "target_ref",
        "blocked_consequence_ref",
        "scope_ref",
        "reason_ref",
        "resolution_condition_ref",
    },
}

_OPTIONAL_DATETIME_FIELDS = {
    "RuntimeEventRecord": {
        "occurred_at",
        "effective_at",
    },
    "RuntimeObjectVersionRecord": set(),
    "ProgressionAssertionRecord": {
        "asserted_at",
        "effective_at",
    },
    "HoldRecord": {
        "placed_at",
        "effective_at",
        "review_at",
        "expires_at",
    },
}


def _validate_non_empty_string(
    value: object,
    field_name: str,
) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")

    if not value.strip():
        raise ValueError(f"{field_name} must not be empty")


def _validate_optional_string(
    value: object,
    field_name: str,
) -> None:
    if value is None:
        return

    _validate_non_empty_string(value, field_name)


def _validate_aware_datetime(
    value: object,
    field_name: str,
) -> None:
    if not isinstance(value, datetime):
        raise TypeError(f"{field_name} must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{field_name} must be timezone-aware")


def _validate_optional_aware_datetime(
    value: object,
    field_name: str,
) -> None:
    if value is None:
        return

    _validate_aware_datetime(value, field_name)


@dataclass(frozen=True)
class RuntimeRecordInspectionReport:
    record_id: str
    record_type: str
    record_category: str
    append_position: int
    recorded_at: datetime
    schema_version: str
    provenance_ref: str | None
    external_id: str | None
    declared_fields: tuple[tuple[str, object], ...]

    def __post_init__(self) -> None:
        self._validate_record_id()
        self._validate_record_type()
        self._validate_record_category()
        self._validate_type_category_alignment()
        self._validate_append_position()
        self._validate_recorded_at()
        self._validate_schema_version()
        self._validate_provenance_ref()
        self._validate_external_id()
        self._validate_declared_fields()

    def _validate_record_id(self) -> None:
        if not isinstance(self.record_id, str):
            raise TypeError("record_id must be a string")

        match = _RECORD_ID_PATTERN.fullmatch(self.record_id)

        if match is None:
            raise ValueError(
                "record_id must use RR-######### syntax"
            )

        if int(match.group(1)) == 0:
            raise ValueError(
                "record_id numeric component must be greater than zero"
            )

    def _validate_record_type(self) -> None:
        if not isinstance(self.record_type, str):
            raise TypeError("record_type must be a string")

        if self.record_type not in _TYPE_CATEGORY_MAP:
            raise ValueError("unsupported record_type")

    def _validate_record_category(self) -> None:
        if not isinstance(self.record_category, str):
            raise TypeError("record_category must be a string")

        if self.record_category not in _TYPE_CATEGORY_MAP.values():
            raise ValueError("unsupported record_category")

    def _validate_type_category_alignment(self) -> None:
        expected_category = _TYPE_CATEGORY_MAP[
            self.record_type
        ]

        if self.record_category != expected_category:
            raise ValueError(
                "record_type and record_category do not align"
            )

    def _validate_append_position(self) -> None:
        if isinstance(self.append_position, bool):
            raise TypeError(
                "append_position must be an integer"
            )

        if not isinstance(self.append_position, int):
            raise TypeError(
                "append_position must be an integer"
            )

        if self.append_position < 0:
            raise ValueError(
                "append_position must not be negative"
            )

    def _validate_recorded_at(self) -> None:
        _validate_aware_datetime(
            self.recorded_at,
            "recorded_at",
        )

    def _validate_schema_version(self) -> None:
        if not isinstance(self.schema_version, str):
            raise TypeError("schema_version must be a string")

        match = _SCHEMA_VERSION_PATTERN.fullmatch(
            self.schema_version
        )

        if match is None:
            raise ValueError(
                "schema_version must use MAJOR.MINOR syntax"
            )

        if int(match.group(1)) == 0:
            raise ValueError(
                "schema_version major component must be greater "
                "than zero"
            )

    def _validate_provenance_ref(self) -> None:
        if self.provenance_ref is None:
            return

        if not isinstance(self.provenance_ref, str):
            raise TypeError(
                "provenance_ref must be a string or None"
            )

        match = _PROVENANCE_REF_PATTERN.fullmatch(
            self.provenance_ref
        )

        if match is None:
            raise ValueError(
                "provenance_ref must use PRV-######### syntax"
            )

        if int(match.group(1)) == 0:
            raise ValueError(
                "provenance_ref numeric component must be greater "
                "than zero"
            )

    def _validate_external_id(self) -> None:
        _validate_optional_string(
            self.external_id,
            "external_id",
        )

    def _validate_declared_fields(self) -> None:
        if type(self.declared_fields) is not tuple:
            raise TypeError(
                "declared_fields must be an exact tuple"
            )

        field_names: list[str] = []
        field_values: dict[str, object] = {}

        for entry in self.declared_fields:
            if type(entry) is not tuple:
                raise TypeError(
                    "each declared field entry must be an exact tuple"
                )

            if len(entry) != 2:
                raise ValueError(
                    "each declared field entry must contain two items"
                )

            field_name, field_value = entry

            if not isinstance(field_name, str):
                raise TypeError(
                    "declared field names must be strings"
                )

            if not field_name.strip():
                raise ValueError(
                    "declared field names must not be empty"
                )

            if field_name in field_values:
                raise ValueError(
                    "declared field names must be unique"
                )

            field_names.append(field_name)
            field_values[field_name] = field_value

        expected_field_names = _DECLARED_FIELD_CONTRACTS[
            self.record_type
        ]

        if tuple(field_names) != expected_field_names:
            raise ValueError(
                "declared field names and order do not match "
                "the record_type contract"
            )

        self._validate_declared_field_values(field_values)

    def _validate_declared_field_values(
        self,
        values: dict[str, object],
    ) -> None:
        required_strings = _REQUIRED_STRING_FIELDS[
            self.record_type
        ]
        optional_datetimes = _OPTIONAL_DATETIME_FIELDS[
            self.record_type
        ]

        for field_name, value in values.items():
            if field_name in required_strings:
                _validate_non_empty_string(
                    value,
                    field_name,
                )
                continue

            if field_name in optional_datetimes:
                _validate_optional_aware_datetime(
                    value,
                    field_name,
                )
                continue

            _validate_optional_string(
                value,
                field_name,
            )

        if self.record_type == "ProgressionAssertionRecord":
            asserted_condition = values[
                "asserted_condition"
            ]
            prior_condition = values["prior_condition"]

            if asserted_condition not in _SUPPORTED_CONDITIONS:
                raise ValueError(
                    "unsupported asserted_condition"
                )

            if (
                prior_condition is not None
                and prior_condition not in _SUPPORTED_CONDITIONS
            ):
                raise ValueError(
                    "unsupported prior_condition"
                )