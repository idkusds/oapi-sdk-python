# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .job_recruiter2 import JobRecruiter2


class RecruiterJobResponseBody(object):
    _types = {
        "info": JobRecruiter2,
    }

    def __init__(self, d=None):
        self.info: Optional[JobRecruiter2] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecruiterJobResponseBodyBuilder":
        return RecruiterJobResponseBodyBuilder()


class RecruiterJobResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._recruiter_job_response_body = RecruiterJobResponseBody()

    def info(self, info: JobRecruiter2) -> "RecruiterJobResponseBodyBuilder":
        self._recruiter_job_response_body.info = info
        return self

    def build(self) -> "RecruiterJobResponseBody":
        return self._recruiter_job_response_body
