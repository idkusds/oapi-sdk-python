# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListJobLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.name: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobLevelRequestBuilder":
        return ListJobLevelRequestBuilder()


class ListJobLevelRequestBuilder(object):

    def __init__(self) -> None:
        list_job_level_request = ListJobLevelRequest()
        list_job_level_request.http_method = HttpMethod.GET
        list_job_level_request.uri = "/open-apis/contact/v3/job_levels"
        list_job_level_request.token_types = {AccessTokenType.TENANT}
        self._list_job_level_request: ListJobLevelRequest = list_job_level_request

    def page_size(self, page_size: int) -> "ListJobLevelRequestBuilder":
        self._list_job_level_request.page_size = page_size
        self._list_job_level_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListJobLevelRequestBuilder":
        self._list_job_level_request.page_token = page_token
        self._list_job_level_request.add_query("page_token", page_token)
        return self

    def name(self, name: str) -> "ListJobLevelRequestBuilder":
        self._list_job_level_request.name = name
        self._list_job_level_request.add_query("name", name)
        return self

    def build(self) -> ListJobLevelRequest:
        return self._list_job_level_request
