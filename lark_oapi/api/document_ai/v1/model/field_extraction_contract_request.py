# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .field_extraction_contract_request_body import FieldExtractionContractRequestBody


class FieldExtractionContractRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[FieldExtractionContractRequestBody] = None

    @staticmethod
    def builder() -> "FieldExtractionContractRequestBuilder":
        return FieldExtractionContractRequestBuilder()


class FieldExtractionContractRequestBuilder(object):

    def __init__(self) -> None:
        field_extraction_contract_request = FieldExtractionContractRequest()
        field_extraction_contract_request.http_method = HttpMethod.POST
        field_extraction_contract_request.uri = "/open-apis/document_ai/v1/contract/field_extraction"
        field_extraction_contract_request.token_types = {AccessTokenType.TENANT}
        self._field_extraction_contract_request: FieldExtractionContractRequest = field_extraction_contract_request

    def request_body(self, request_body: FieldExtractionContractRequestBody) -> "FieldExtractionContractRequestBuilder":
        self._field_extraction_contract_request.request_body = request_body
        self._field_extraction_contract_request.body = request_body
        return self

    def build(self) -> FieldExtractionContractRequest:
        return self._field_extraction_contract_request
