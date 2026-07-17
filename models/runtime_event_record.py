from dataclasses import dataclass
from datetime import datetime
import re

from models.runtime_record_identity import RuntimeRecordHeader


_EVENT_TYPE_PATTERN = re.compile(
    r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$"
)


@dataclass(frozen=True)
class RuntimeEventRecord:
    """
    Immutable Runtime Event record.

    This model records event identity, event type, and explicitly
    available context only. It does not publish, persist, authorize,
    admit, validate semantically, or apply canonical effects.
    """

    header: RuntimeRecordHeader
    event_type: str
    target_ref: str | None = None
    actor_ref: str | None = None
    source_ref: str | None = None
    scope_ref: str | None = None
    branch_ref: str | None = None
    occurred_at: datetime | None = None
    effective_at: datetime | None = None

    def __post_init__(self) -> None:
        self._validate_header()
        self._validate_event_type()
        self._validate_reference("target_ref", self.target_ref)
        self._validate_reference("actor_ref", self.actor_ref)
        self._validate_reference("source_ref", self.source_ref)
        self._validate_reference("scope_ref", self.scope_ref)
        self._validate_reference("branch_ref", self.branch_ref)
        self._validate_optional_datetime(
            "occurred_at",
            self.occurred_at,
        )
        self._validate_optional_datetime(
            "effective_at",
            self.effective_at,
        )

    def _validate_header(self) -> None:
        if not isinstance(self.header, RuntimeRecordHeader):
            raise TypeError(
                "header must be a RuntimeRecordHeader"
            )

        if self.header.record_category != "EVENT":
            raise ValueError(
                "header record_category must be EVENT"
            )

    def _validate_event_type(self) -> None:
        if not isinstance(self.event_type, str):
            raise TypeError(
                "event_type must be a string"
            )

        if not _EVENT_TYPE_PATTERN.fullmatch(self.event_type):
            raise ValueError(
                "event_type must use uppercase underscore syntax"
            )

    @staticmethod
    def _validate_reference(
        field_name: str,
        value: str | None,
    ) -> None:
        if value is None:
            return

        if not isinstance(value, str):
            raise TypeError(
                f"{field_name} must be a string or None"
            )

        if not value.strip():
            raise ValueError(
                f"{field_name} must not be empty or whitespace-only"
            )

    @staticmethod
    def _validate_optional_datetime(
        field_name: str,
        value: datetime | None,
    ) -> None:
        if value is None:
            return

        if not isinstance(value, datetime):
            raise TypeError(
                f"{field_name} must be a datetime or None"
            )

        if (
            value.tzinfo is None
            or value.utcoffset() is None
        ):
            raise ValueError(
                f"{field_name} must be timezone-aware"
            )