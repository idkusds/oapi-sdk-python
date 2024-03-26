# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .recognize_chinese_passport_request_body import RecognizeChinesePassportRequestBody


class RecognizeChinesePassportRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[RecognizeChinesePassportRequestBody] = None

    @staticmethod
    def builder() -> "RecognizeChinesePassportRequestBuilder":
        return RecognizeChinesePassportRequestBuilder()


class RecognizeChinesePassportRequestBuilder(object):

    def __init__(self) -> None:
        recognize_chinese_passport_request = RecognizeChinesePassportRequest()
        recognize_chinese_passport_request.http_method = HttpMethod.POST
        recognize_chinese_passport_request.uri = "/open-apis/document_ai/v1/chinese_passport/recognize"
        recognize_chinese_passport_request.token_types = {AccessTokenType.TENANT}
        self._recognize_chinese_passport_request: RecognizeChinesePassportRequest = recognize_chinese_passport_request

    def request_body(self,
                     request_body: RecognizeChinesePassportRequestBody) -> "RecognizeChinesePassportRequestBuilder":
        self._recognize_chinese_passport_request.request_body = request_body
        self._recognize_chinese_passport_request.body = request_body
        return self

    def build(self) -> RecognizeChinesePassportRequest:
        return self._recognize_chinese_passport_request
