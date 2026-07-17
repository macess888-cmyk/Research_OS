from models.hold_record import HoldRecord
from models.progression_assertion_record import ProgressionAssertionRecord
from models.runtime_event_record import RuntimeEventRecord
from models.runtime_object_version_record import RuntimeObjectVersionRecord
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from services.runtime_record_registry import RuntimeRecordRegistry


class RuntimeRecordInspector:
    def __init__(
        self,
        registry: RuntimeRecordRegistry,
    ) -> None:
        if type(registry) is not RuntimeRecordRegistry:
            raise TypeError(
                "registry must be an exact RuntimeRecordRegistry"
            )

        self._registry = registry

    def inspect_record(
        self,
        record_id: str,
    ) -> RuntimeRecordInspectionReport:
        record = self._registry.get(record_id)
        records = self._registry.records()

        for append_position, registered_record in enumerate(records):
            if registered_record is record:
                return self._build_report(
                    record,
                    append_position,
                )

        raise KeyError(record_id)

    def inspect_records(
        self,
    ) -> tuple[RuntimeRecordInspectionReport, ...]:
        records = self._registry.records()

        return tuple(
            self._build_report(record, append_position)
            for append_position, record in enumerate(records)
        )

    def inspect_records_by_category(
        self,
        record_category: str,
    ) -> tuple[RuntimeRecordInspectionReport, ...]:
        matching_records = self._registry.records_by_category(
            record_category
        )
        all_records = self._registry.records()

        positions_by_identity = {
            id(record): append_position
            for append_position, record in enumerate(all_records)
        }

        return tuple(
            self._build_report(
                record,
                positions_by_identity[id(record)],
            )
            for record in matching_records
        )

    def _build_report(
        self,
        record,
        append_position: int,
    ) -> RuntimeRecordInspectionReport:
        if type(record) is RuntimeEventRecord:
            declared_fields = (
                ("event_type", record.event_type),
                ("target_ref", record.target_ref),
                ("actor_ref", record.actor_ref),
                ("source_ref", record.source_ref),
                ("scope_ref", record.scope_ref),
                ("branch_ref", record.branch_ref),
                ("occurred_at", record.occurred_at),
                ("effective_at", record.effective_at),
            )
            record_type = "RuntimeEventRecord"

        elif type(record) is RuntimeObjectVersionRecord:
            declared_fields = (
                ("object_ref", record.object_ref),
                ("representation_ref", record.representation_ref),
                ("version_label", record.version_label),
                ("predecessor_ref", record.predecessor_ref),
                ("branch_ref", record.branch_ref),
                ("scope_ref", record.scope_ref),
            )
            record_type = "RuntimeObjectVersionRecord"

        elif type(record) is ProgressionAssertionRecord:
            declared_fields = (
                ("target_ref", record.target_ref),
                (
                    "asserted_condition",
                    record.asserted_condition,
                ),
                ("scope_ref", record.scope_ref),
                (
                    "target_version_ref",
                    record.target_version_ref,
                ),
                ("prior_condition", record.prior_condition),
                ("branch_ref", record.branch_ref),
                ("context_ref", record.context_ref),
                ("asserted_at", record.asserted_at),
                ("effective_at", record.effective_at),
                ("actor_ref", record.actor_ref),
                ("source_ref", record.source_ref),
                ("basis_ref", record.basis_ref),
            )
            record_type = "ProgressionAssertionRecord"

        elif type(record) is HoldRecord:
            declared_fields = (
                ("target_ref", record.target_ref),
                (
                    "blocked_consequence_ref",
                    record.blocked_consequence_ref,
                ),
                ("scope_ref", record.scope_ref),
                ("reason_ref", record.reason_ref),
                (
                    "resolution_condition_ref",
                    record.resolution_condition_ref,
                ),
                (
                    "target_version_ref",
                    record.target_version_ref,
                ),
                ("branch_ref", record.branch_ref),
                ("context_ref", record.context_ref),
                ("trigger_ref", record.trigger_ref),
                ("basis_ref", record.basis_ref),
                ("owner_ref", record.owner_ref),
                ("placed_by_ref", record.placed_by_ref),
                (
                    "placement_authority_ref",
                    record.placement_authority_ref,
                ),
                (
                    "release_authority_ref",
                    record.release_authority_ref,
                ),
                ("placed_at", record.placed_at),
                ("effective_at", record.effective_at),
                ("review_at", record.review_at),
                ("expires_at", record.expires_at),
            )
            record_type = "HoldRecord"

        else:
            raise TypeError("unsupported Runtime record type")

        header = record.header

        return RuntimeRecordInspectionReport(
            record_id=header.record_id,
            record_type=record_type,
            record_category=header.record_category,
            append_position=append_position,
            recorded_at=header.recorded_at,
            schema_version=header.schema_version,
            provenance_ref=header.provenance_ref,
            external_id=header.external_id,
            declared_fields=declared_fields,
        )