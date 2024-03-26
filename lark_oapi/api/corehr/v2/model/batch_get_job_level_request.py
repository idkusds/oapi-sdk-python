# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_get_job_level_request_body import BatchGetJobLevelRequestBody


class BatchGetJobLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[BatchGetJobLevelRequestBody] = None

    @staticmethod
    def builder() -> "BatchGetJobLevelRequestBuilder":
        return BatchGetJobLevelRequestBuilder()


class BatchGetJobLevelRequestBuilder(object):

    def __init__(self) -> None:
        batch_get_job_level_request = BatchGetJobLevelRequest()
        batch_get_job_level_request.http_method = HttpMethod.POST
        batch_get_job_level_request.uri = "/open-apis/corehr/v2/job_levels/batch_get"
        batch_get_job_level_request.token_types = {AccessTokenType.TENANT}
        self._batch_get_job_level_request: BatchGetJobLevelRequest = batch_get_job_level_request

    def request_body(self, request_body: BatchGetJobLevelRequestBody) -> "BatchGetJobLevelRequestBuilder":
        self._batch_get_job_level_request.request_body = request_body
        self._batch_get_job_level_request.body = request_body
        return self

    def build(self) -> BatchGetJobLevelRequest:
        return self._batch_get_job_level_request
