from datetime import datetime

from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)


class RuntimeRecordInspectionRepresentationService:
    def to_primitive_dict(
        self,
        report: RuntimeRecordInspectionReport,
    ) -> dict[str, object]:
        if type(report) is not RuntimeRecordInspectionReport:
            raise TypeError(
                "report must be an exact RuntimeRecordInspectionReport"
            )

        return {
            "record_id": report.record_id,
            "record_type": report.record_type,
            "record_category": report.record_category,
            "append_position": report.append_position,
            "recorded_at": report.recorded_at.isoformat(),
            "schema_version": report.schema_version,
            "provenance_ref": report.provenance_ref,
            "external_id": report.external_id,
            "declared_fields": [
                [
                    field_name,
                    self._to_primitive_value(field_value),
                ]
                for field_name, field_value in report.declared_fields
            ],
        }

    def _to_primitive_value(
        self,
        value: object,
    ) -> object:
        if isinstance(value, datetime):
            return value.isoformat()

        return value