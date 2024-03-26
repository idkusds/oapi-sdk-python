# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .recognize_tw_mainland_travel_permit_request_body import RecognizeTwMainlandTravelPermitRequestBody


class RecognizeTwMainlandTravelPermitRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[RecognizeTwMainlandTravelPermitRequestBody] = None

    @staticmethod
    def builder() -> "RecognizeTwMainlandTravelPermitRequestBuilder":
        return RecognizeTwMainlandTravelPermitRequestBuilder()


class RecognizeTwMainlandTravelPermitRequestBuilder(object):

    def __init__(self) -> None:
        recognize_tw_mainland_travel_permit_request = RecognizeTwMainlandTravelPermitRequest()
        recognize_tw_mainland_travel_permit_request.http_method = HttpMethod.POST
        recognize_tw_mainland_travel_permit_request.uri = "/open-apis/document_ai/v1/tw_mainland_travel_permit/recognize"
        recognize_tw_mainland_travel_permit_request.token_types = {AccessTokenType.TENANT}
        self._recognize_tw_mainland_travel_permit_request: RecognizeTwMainlandTravelPermitRequest = recognize_tw_mainland_travel_permit_request

    def request_body(self,
                     request_body: RecognizeTwMainlandTravelPermitRequestBody) -> "RecognizeTwMainlandTravelPermitRequestBuilder":
        self._recognize_tw_mainland_travel_permit_request.request_body = request_body
        self._recognize_tw_mainland_travel_permit_request.body = request_body
        return self

    def build(self) -> RecognizeTwMainlandTravelPermitRequest:
        return self._recognize_tw_mainland_travel_permit_request
