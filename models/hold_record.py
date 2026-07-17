from dataclasses import dataclass
from datetime import datetime

from models.runtime_record_identity import RuntimeRecordHeader


@dataclass(frozen=True)
class HoldRecord:
    """
    Immutable Runtime control record declaring that a consequence is held
    for a target within an explicit scope pending a resolution condition.

    Construction does not establish authority, admission, active status,
    blocking enforcement, resolution, release, refusal, failure, progression
    HELD, or Evaluation HOLD.
    """

    header: RuntimeRecordHeader
    target_ref: str
    blocked_consequence_ref: str
    scope_ref: str
    reason_ref: str
    resolution_condition_ref: str
    target_version_ref: str | None = None
    branch_ref: str | None = None
    context_ref: str | None = None
    trigger_ref: str | None = None
    basis_ref: str | None = None
    owner_ref: str | None = None
    placed_by_ref: str | None = None
    placement_authority_ref: str | None = None
    release_authority_ref: str | None = None
    placed_at: datetime | None = None
    effective_at: datetime | None = None
    review_at: datetime | None = None
    expires_at: datetime | None = None

    def __post_init__(self) -> None:
        self._validate_header()

        self._validate_required_reference("target_ref", self.target_ref)
        self._validate_required_reference(
            "blocked_consequence_ref",
            self.blocked_consequence_ref,
        )
        self._validate_required_reference("scope_ref", self.scope_ref)
        self._validate_required_reference("reason_ref", self.reason_ref)
        self._validate_required_reference(
            "resolution_condition_ref",
            self.resolution_condition_ref,
        )

        self._validate_optional_reference(
            "target_version_ref",
            self.target_version_ref,
        )
        self._validate_optional_reference("branch_ref", self.branch_ref)
        self._validate_optional_reference("context_ref", self.context_ref)
        self._validate_optional_reference("trigger_ref", self.trigger_ref)
        self._validate_optional_reference("basis_ref", self.basis_ref)
        self._validate_optional_reference("owner_ref", self.owner_ref)
        self._validate_optional_reference(
            "placed_by_ref",
            self.placed_by_ref,
        )
        self._validate_optional_reference(
            "placement_authority_ref",
            self.placement_authority_ref,
        )
        self._validate_optional_reference(
            "release_authority_ref",
            self.release_authority_ref,
        )

        self._validate_optional_datetime("placed_at", self.placed_at)
        self._validate_optional_datetime("effective_at", self.effective_at)
        self._validate_optional_datetime("review_at", self.review_at)
        self._validate_optional_datetime("expires_at", self.expires_at)

    def _validate_header(self) -> None:
        if not isinstance(self.header, RuntimeRecordHeader):
            raise TypeError("header must be a RuntimeRecordHeader")

        if self.header.record_category != "HOLD":
            raise ValueError(
                "header record_category must be HOLD"
            )

    @staticmethod
    def _validate_required_reference(
        field_name: str,
        value: str,
    ) -> None:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")

        if not value.strip():
            raise ValueError(
                f"{field_name} must not be empty or whitespace-only"
            )

    @staticmethod
    def _validate_optional_reference(
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

        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError(
                f"{field_name} must be timezone-aware"
            )