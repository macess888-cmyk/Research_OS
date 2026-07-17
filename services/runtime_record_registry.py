from models.hold_record import HoldRecord
from models.progression_assertion_record import ProgressionAssertionRecord
from models.runtime_event_record import RuntimeEventRecord
from models.runtime_object_version_record import RuntimeObjectVersionRecord
from models.runtime_record_registration_result import (
    RuntimeRecordRegistrationResult,
)


_SUPPORTED_RECORD_TYPES = (
    RuntimeEventRecord,
    RuntimeObjectVersionRecord,
    ProgressionAssertionRecord,
    HoldRecord,
)


class RuntimeRecordDuplicateError(Exception):
    pass


class RuntimeRecordIdentityCollisionError(Exception):
    pass


class RuntimeRecordRegistry:
    """
    In-memory append-only registry for supported immutable Runtime records.

    Registration establishes local membership only. It does not establish
    admission, authority, persistence, canonicality, currentness, progression,
    active Hold state, or any operational consequence.
    """

    def __init__(self) -> None:
        self._records_by_id = {}

    def register(self, record):
        if type(record) not in _SUPPORTED_RECORD_TYPES:
            raise TypeError(
                "record must be a supported Runtime record"
            )

        record_id = record.header.record_id
        existing = self._records_by_id.get(record_id)

        if existing is not None:
            if incoming_equals_existing := (record == existing):
                raise RuntimeRecordDuplicateError(
                    f"record_id already registered: {record_id}"
                )

            raise RuntimeRecordIdentityCollisionError(
                f"record_id identity collision: {record_id}"
            )

        append_position = len(self._records_by_id)
        self._records_by_id[record_id] = record

        return RuntimeRecordRegistrationResult(
            record_id=record_id,
            append_position=append_position,
        )

    def get(self, record_id: str):
        self._validate_record_id_input(record_id)

        try:
            return self._records_by_id[record_id]
        except KeyError:
            raise KeyError(record_id) from None

    def contains(self, record_id: str) -> bool:
        self._validate_record_id_input(record_id)
        return record_id in self._records_by_id

    def count(self) -> int:
        return len(self._records_by_id)

    def records(self) -> tuple:
        return tuple(self._records_by_id.values())

    def records_by_category(
        self,
        record_category: str,
    ) -> tuple:
        if not isinstance(record_category, str):
            raise TypeError(
                "record_category must be a string"
            )

        if not record_category.strip():
            raise ValueError(
                "record_category must not be empty or whitespace-only"
            )

        return tuple(
            record
            for record in self._records_by_id.values()
            if record.header.record_category == record_category
        )

    @staticmethod
    def _validate_record_id_input(record_id: str) -> None:
        if not isinstance(record_id, str):
            raise TypeError(
                "record_id must be a string"
            )