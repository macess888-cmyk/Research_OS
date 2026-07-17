from dataclasses import dataclass
from datetime import datetime
import re


_RECORD_ID_PATTERN = re.compile(r"^RR-[0-9]{9}$")
_RECORD_CATEGORY_PATTERN = re.compile(
    r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$"
)
_PROVENANCE_REF_PATTERN = re.compile(r"^PRV-[0-9]{9}$")
_SCHEMA_VERSION_PATTERN = re.compile(r"^[1-9][0-9]*\.[0-9]+$")


@dataclass(frozen=True)
class RuntimeRecordHeader:
    """
    Immutable structural header shared by Runtime Kernel records.

    This model defines record identity and structural attribution only.
    It does not define semantic payload, persistence, authority,
    progression, graph topology, or canonical effect.
    """

    record_id: str
    record_category: str
    recorded_at: datetime
    schema_version: str
    provenance_ref: str | None = None
    external_id: str | None = None

    def __post_init__(self) -> None:
        self._validate_record_id()
        self._validate_record_category()
        self._validate_recorded_at()
        self._validate_schema_version()
        self._validate_provenance_ref()
        self._validate_external_id()

    def _validate_record_id(self) -> None:
        if not isinstance(self.record_id, str):
            raise TypeError("record_id must be a string")

        if not _RECORD_ID_PATTERN.fullmatch(self.record_id):
            raise ValueError(
                "record_id must match RR-#########"
            )

        if int(self.record_id[3:]) <= 0:
            raise ValueError(
                "record_id numeric component must be greater than zero"
            )

    def _validate_record_category(self) -> None:
        if not isinstance(self.record_category, str):
            raise TypeError("record_category must be a string")

        if not _RECORD_CATEGORY_PATTERN.fullmatch(
            self.record_category
        ):
            raise ValueError(
                "record_category must use uppercase underscore syntax"
            )

    def _validate_recorded_at(self) -> None:
        if not isinstance(self.recorded_at, datetime):
            raise TypeError("recorded_at must be a datetime")

        if (
            self.recorded_at.tzinfo is None
            or self.recorded_at.utcoffset() is None
        ):
            raise ValueError(
                "recorded_at must be timezone-aware"
            )

    def _validate_schema_version(self) -> None:
        if not isinstance(self.schema_version, str):
            raise TypeError("schema_version must be a string")

        if not _SCHEMA_VERSION_PATTERN.fullmatch(
            self.schema_version
        ):
            raise ValueError(
                "schema_version must use MAJOR.MINOR format"
            )

    def _validate_provenance_ref(self) -> None:
        if self.provenance_ref is None:
            return

        if not isinstance(self.provenance_ref, str):
            raise TypeError(
                "provenance_ref must be a string or None"
            )

        if not _PROVENANCE_REF_PATTERN.fullmatch(
            self.provenance_ref
        ):
            raise ValueError(
                "provenance_ref must match PRV-#########"
            )

        if int(self.provenance_ref[4:]) <= 0:
            raise ValueError(
                "provenance_ref numeric component must be greater than zero"
            )

    def _validate_external_id(self) -> None:
        if self.external_id is None:
            return

        if not isinstance(self.external_id, str):
            raise TypeError(
                "external_id must be a string or None"
            )

        if not self.external_id.strip():
            raise ValueError(
                "external_id must not be empty or whitespace-only"
            )