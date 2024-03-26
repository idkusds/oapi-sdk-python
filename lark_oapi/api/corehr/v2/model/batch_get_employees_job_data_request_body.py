# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchGetEmployeesJobDataRequestBody(object):
    _types = {
        "employment_ids": List[str],
        "get_all_version": bool,
        "effective_date_start": str,
        "effective_date_end": str,
        "data_date": str,
    }

    def __init__(self, d=None):
        self.employment_ids: Optional[List[str]] = None
        self.get_all_version: Optional[bool] = None
        self.effective_date_start: Optional[str] = None
        self.effective_date_end: Optional[str] = None
        self.data_date: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetEmployeesJobDataRequestBodyBuilder":
        return BatchGetEmployeesJobDataRequestBodyBuilder()


class BatchGetEmployeesJobDataRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_employees_job_data_request_body = BatchGetEmployeesJobDataRequestBody()

    def employment_ids(self, employment_ids: List[str]) -> "BatchGetEmployeesJobDataRequestBodyBuilder":
        self._batch_get_employees_job_data_request_body.employment_ids = employment_ids
        return self

    def get_all_version(self, get_all_version: bool) -> "BatchGetEmployeesJobDataRequestBodyBuilder":
        self._batch_get_employees_job_data_request_body.get_all_version = get_all_version
        return self

    def effective_date_start(self, effective_date_start: str) -> "BatchGetEmployeesJobDataRequestBodyBuilder":
        self._batch_get_employees_job_data_request_body.effective_date_start = effective_date_start
        return self

    def effective_date_end(self, effective_date_end: str) -> "BatchGetEmployeesJobDataRequestBodyBuilder":
        self._batch_get_employees_job_data_request_body.effective_date_end = effective_date_end
        return self

    def data_date(self, data_date: str) -> "BatchGetEmployeesJobDataRequestBodyBuilder":
        self._batch_get_employees_job_data_request_body.data_date = data_date
        return self

    def build(self) -> "BatchGetEmployeesJobDataRequestBody":
        return self._batch_get_employees_job_data_request_body
