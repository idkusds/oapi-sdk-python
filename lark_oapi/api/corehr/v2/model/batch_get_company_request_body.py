# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchGetCompanyRequestBody(object):
    _types = {
        "company_ids": List[str],
    }

    def __init__(self, d=None):
        self.company_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetCompanyRequestBodyBuilder":
        return BatchGetCompanyRequestBodyBuilder()


class BatchGetCompanyRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_company_request_body = BatchGetCompanyRequestBody()

    def company_ids(self, company_ids: List[str]) -> "BatchGetCompanyRequestBodyBuilder":
        self._batch_get_company_request_body.company_ids = company_ids
        return self

    def build(self) -> "BatchGetCompanyRequestBody":
        return self._batch_get_company_request_body
