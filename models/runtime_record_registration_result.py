from dataclasses import dataclass
import re


_RECORD_ID_PATTERN = re.compile(r"^RR-[0-9]{9}$")


@dataclass(frozen=True)
class RuntimeRecordRegistrationResult:
    """
    Immutable result returned after one successful Runtime record registration.

    The result establishes registry membership and append position only.
    It does not establish admission, authority, persistence, canonicality,
    currentness, or semantic validity.
    """

    record_id: str
    append_position: int

    def __post_init__(self) -> None:
        self._validate_record_id()
        self._validate_append_position()

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
                "append_position must be greater than or equal to zero"
            )