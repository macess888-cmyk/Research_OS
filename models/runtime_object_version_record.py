from dataclasses import dataclass

from models.runtime_record_identity import RuntimeRecordHeader


@dataclass(frozen=True)
class RuntimeObjectVersionRecord:
    """
    Immutable Runtime Object Version record.

    This model identifies one declared representation version of an
    enduring Runtime Object. It does not establish currentness,
    supersession, validity, admission, authority, persistence, or
    representation integrity.
    """

    header: RuntimeRecordHeader
    object_ref: str
    representation_ref: str
    version_label: str | None = None
    predecessor_ref: str | None = None
    branch_ref: str | None = None
    scope_ref: str | None = None

    def __post_init__(self) -> None:
        self._validate_header()
        self._validate_required_reference(
            "object_ref",
            self.object_ref,
        )
        self._validate_required_reference(
            "representation_ref",
            self.representation_ref,
        )
        self._validate_optional_reference(
            "version_label",
            self.version_label,
        )
        self._validate_optional_reference(
            "predecessor_ref",
            self.predecessor_ref,
        )
        self._validate_self_predecessor()
        self._validate_optional_reference(
            "branch_ref",
            self.branch_ref,
        )
        self._validate_optional_reference(
            "scope_ref",
            self.scope_ref,
        )

    def _validate_header(self) -> None:
        if not isinstance(self.header, RuntimeRecordHeader):
            raise TypeError(
                "header must be a RuntimeRecordHeader"
            )

        if self.header.record_category != "VERSION":
            raise ValueError(
                "header record_category must be VERSION"
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

    def _validate_self_predecessor(self) -> None:
        if self.predecessor_ref == self.header.record_id:
            raise ValueError(
                "predecessor_ref must not equal header record_id"
            )