# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .faq_update_info import FaqUpdateInfo


class CreateFaqRequestBody(object):
    _types = {
        "faq": FaqUpdateInfo,
    }

    def __init__(self, d):
        self.faq: Optional[FaqUpdateInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateFaqRequestBodyBuilder":
        return CreateFaqRequestBodyBuilder()


class CreateFaqRequestBodyBuilder(object):
    def __init__(self, create_faq_request_body: CreateFaqRequestBody = CreateFaqRequestBody({})) -> None:
        self._create_faq_request_body: CreateFaqRequestBody = create_faq_request_body
    
    def faq(self, faq: FaqUpdateInfo) -> "CreateFaqRequestBodyBuilder":
        self._create_faq_request_body.faq = faq
        return self
    
    def build(self) -> "CreateFaqRequestBody":
        return self._create_faq_request_body