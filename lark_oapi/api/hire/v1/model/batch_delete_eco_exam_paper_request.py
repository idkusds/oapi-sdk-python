# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_delete_eco_exam_paper_request_body import BatchDeleteEcoExamPaperRequestBody


class BatchDeleteEcoExamPaperRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[BatchDeleteEcoExamPaperRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeleteEcoExamPaperRequestBuilder":
        return BatchDeleteEcoExamPaperRequestBuilder()


class BatchDeleteEcoExamPaperRequestBuilder(object):

    def __init__(self) -> None:
        batch_delete_eco_exam_paper_request = BatchDeleteEcoExamPaperRequest()
        batch_delete_eco_exam_paper_request.http_method = HttpMethod.POST
        batch_delete_eco_exam_paper_request.uri = "/open-apis/hire/v1/eco_exam_papers/batch_delete"
        batch_delete_eco_exam_paper_request.token_types = {AccessTokenType.TENANT}
        self._batch_delete_eco_exam_paper_request: BatchDeleteEcoExamPaperRequest = batch_delete_eco_exam_paper_request

    def request_body(self, request_body: BatchDeleteEcoExamPaperRequestBody) -> "BatchDeleteEcoExamPaperRequestBuilder":
        self._batch_delete_eco_exam_paper_request.request_body = request_body
        self._batch_delete_eco_exam_paper_request.body = request_body
        return self

    def build(self) -> BatchDeleteEcoExamPaperRequest:
        return self._batch_delete_eco_exam_paper_request
