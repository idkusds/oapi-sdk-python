# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .job_data import JobData


class CreateJobDataResponseBody(object):
    _types = {
        "job_data": JobData,
    }

    def __init__(self, d=None):
        self.job_data: Optional[JobData] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateJobDataResponseBodyBuilder":
        return CreateJobDataResponseBodyBuilder()


class CreateJobDataResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_job_data_response_body = CreateJobDataResponseBody()

    def job_data(self, job_data: JobData) -> "CreateJobDataResponseBodyBuilder":
        self._create_job_data_response_body.job_data = job_data
        return self

    def build(self) -> "CreateJobDataResponseBody":
        return self._create_job_data_response_body
