# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .recognize_business_license_request_body import RecognizeBusinessLicenseRequestBody


class RecognizeBusinessLicenseRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[RecognizeBusinessLicenseRequestBody] = None

    @staticmethod
    def builder() -> "RecognizeBusinessLicenseRequestBuilder":
        return RecognizeBusinessLicenseRequestBuilder()


class RecognizeBusinessLicenseRequestBuilder(object):

    def __init__(self) -> None:
        recognize_business_license_request = RecognizeBusinessLicenseRequest()
        recognize_business_license_request.http_method = HttpMethod.POST
        recognize_business_license_request.uri = "/open-apis/document_ai/v1/business_license/recognize"
        recognize_business_license_request.token_types = {AccessTokenType.TENANT}
        self._recognize_business_license_request: RecognizeBusinessLicenseRequest = recognize_business_license_request

    def request_body(self,
                     request_body: RecognizeBusinessLicenseRequestBody) -> "RecognizeBusinessLicenseRequestBuilder":
        self._recognize_business_license_request.request_body = request_body
        self._recognize_business_license_request.body = request_body
        return self

    def build(self) -> RecognizeBusinessLicenseRequest:
        return self._recognize_business_license_request