from dataclasses import dataclass
from datetime import datetime

from models.runtime_record_identity import RuntimeRecordHeader


_ACCEPTED_PROGRESSION_CONDITIONS = frozenset(
    {
        "PENDING",
        "ACTIVE",
        "HELD",
        "DORMANT",
        "ABANDONED",
    }
)


@dataclass(frozen=True)
class ProgressionAssertionRecord:
    """
    Immutable assertion that a target has a declared progression condition
    within an explicit scope.

    Construction does not establish truth, authority, admission, transition
    validity, Hold control, conflict, or canonical current progression.
    """

    header: RuntimeRecordHeader
    target_ref: str
    asserted_condition: str
    scope_ref: str
    target_version_ref: str | None = None
    prior_condition: str | None = None
    branch_ref: str | None = None
    context_ref: str | None = None
    asserted_at: datetime | None = None
    effective_at: datetime | None = None
    actor_ref: str | None = None
    source_ref: str | None = None
    basis_ref: str | None = None

    def __post_init__(self) -> None:
        self._validate_header()

        self._validate_required_reference(
            "target_ref",
            self.target_ref,
        )
        self._validate_condition(
            "asserted_condition",
            self.asserted_condition,
            optional=False,
        )
        self._validate_required_reference(
            "scope_ref",
            self.scope_ref,
        )

        self._validate_optional_reference(
            "target_version_ref",
            self.target_version_ref,
        )
        self._validate_condition(
            "prior_condition",
            self.prior_condition,
            optional=True,
        )
        self._validate_optional_reference(
            "branch_ref",
            self.branch_ref,
        )
        self._validate_optional_reference(
            "context_ref",
            self.context_ref,
        )

        self._validate_optional_datetime(
            "asserted_at",
            self.asserted_at,
        )
        self._validate_optional_datetime(
            "effective_at",
            self.effective_at,
        )

        self._validate_optional_reference(
            "actor_ref",
            self.actor_ref,
        )
        self._validate_optional_reference(
            "source_ref",
            self.source_ref,
        )
        self._validate_optional_reference(
            "basis_ref",
            self.basis_ref,
        )

    def _validate_header(self) -> None:
        if not isinstance(self.header, RuntimeRecordHeader):
            raise TypeError(
                "header must be a RuntimeRecordHeader"
            )

        if self.header.record_category != "PROGRESSION_ASSERTION":
            raise ValueError(
                "header record_category must be PROGRESSION_ASSERTION"
            )

    @staticmethod
    def _validate_required_reference(
        field_name: str,
        value: str,
    ) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f"{field_name} must be a string"
            )

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
    def _validate_condition(
        field_name: str,
        value: str | None,
        *,
        optional: bool,
    ) -> None:
        if value is None:
            if optional:
                return

            raise TypeError(
                f"{field_name} must be a string"
            )

        if not isinstance(value, str):
            expected = "a string or None" if optional else "a string"
            raise TypeError(
                f"{field_name} must be {expected}"
            )

        if value not in _ACCEPTED_PROGRESSION_CONDITIONS:
            raise ValueError(
                f"{field_name} must be one of "
                "PENDING, ACTIVE, HELD, DORMANT, or ABANDONED"
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