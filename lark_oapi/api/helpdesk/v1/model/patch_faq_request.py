# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .patch_faq_request_body import PatchFaqRequestBody


class PatchFaqRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.id: Optional[str] = None
        self.request_body: Optional[PatchFaqRequestBody] = None

    @staticmethod
    def builder() -> "PatchFaqRequestBuilder":
        return PatchFaqRequestBuilder()


class PatchFaqRequestBuilder(object):

    def __init__(self) -> None:
        patch_faq_request = PatchFaqRequest()
        patch_faq_request.http_method = HttpMethod.PATCH
        patch_faq_request.uri = "/open-apis/helpdesk/v1/faqs/:id"
        patch_faq_request.token_types = {AccessTokenType.USER}
        self._patch_faq_request: PatchFaqRequest = patch_faq_request

    def id(self, id: str) -> "PatchFaqRequestBuilder":
        self._patch_faq_request.id = id
        self._patch_faq_request.paths["id"] = str(id)
        return self

    def request_body(self, request_body: PatchFaqRequestBody) -> "PatchFaqRequestBuilder":
        self._patch_faq_request.request_body = request_body
        self._patch_faq_request.body = request_body
        return self

    def build(self) -> PatchFaqRequest:
        return self._patch_faq_request
