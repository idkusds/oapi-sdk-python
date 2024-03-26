# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .transfer_info import TransferInfo


class JobChange(object):
    _types = {
        "job_change_id": str,
        "employment_id": str,
        "status": str,
        "transfer_type_unique_identifier": str,
        "transfer_reason_unique_identifier": str,
        "process_id": str,
        "effective_date": str,
        "created_time": str,
        "updated_time": str,
        "transfer_info": TransferInfo,
    }

    def __init__(self, d=None):
        self.job_change_id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.status: Optional[str] = None
        self.transfer_type_unique_identifier: Optional[str] = None
        self.transfer_reason_unique_identifier: Optional[str] = None
        self.process_id: Optional[str] = None
        self.effective_date: Optional[str] = None
        self.created_time: Optional[str] = None
        self.updated_time: Optional[str] = None
        self.transfer_info: Optional[TransferInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobChangeBuilder":
        return JobChangeBuilder()


class JobChangeBuilder(object):
    def __init__(self) -> None:
        self._job_change = JobChange()

    def job_change_id(self, job_change_id: str) -> "JobChangeBuilder":
        self._job_change.job_change_id = job_change_id
        return self

    def employment_id(self, employment_id: str) -> "JobChangeBuilder":
        self._job_change.employment_id = employment_id
        return self

    def status(self, status: str) -> "JobChangeBuilder":
        self._job_change.status = status
        return self

    def transfer_type_unique_identifier(self, transfer_type_unique_identifier: str) -> "JobChangeBuilder":
        self._job_change.transfer_type_unique_identifier = transfer_type_unique_identifier
        return self

    def transfer_reason_unique_identifier(self, transfer_reason_unique_identifier: str) -> "JobChangeBuilder":
        self._job_change.transfer_reason_unique_identifier = transfer_reason_unique_identifier
        return self

    def process_id(self, process_id: str) -> "JobChangeBuilder":
        self._job_change.process_id = process_id
        return self

    def effective_date(self, effective_date: str) -> "JobChangeBuilder":
        self._job_change.effective_date = effective_date
        return self

    def created_time(self, created_time: str) -> "JobChangeBuilder":
        self._job_change.created_time = created_time
        return self

    def updated_time(self, updated_time: str) -> "JobChangeBuilder":
        self._job_change.updated_time = updated_time
        return self

    def transfer_info(self, transfer_info: TransferInfo) -> "JobChangeBuilder":
        self._job_change.transfer_info = transfer_info
        return self

    def build(self) -> "JobChange":
        return self._job_change
