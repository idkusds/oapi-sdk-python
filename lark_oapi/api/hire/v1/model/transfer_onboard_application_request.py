# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .transfer_onboard_application_request_body import TransferOnboardApplicationRequestBody


class TransferOnboardApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.application_id: Optional[str] = None
        self.request_body: Optional[TransferOnboardApplicationRequestBody] = None

    @staticmethod
    def builder() -> "TransferOnboardApplicationRequestBuilder":
        return TransferOnboardApplicationRequestBuilder()


class TransferOnboardApplicationRequestBuilder(object):

    def __init__(self) -> None:
        transfer_onboard_application_request = TransferOnboardApplicationRequest()
        transfer_onboard_application_request.http_method = HttpMethod.POST
        transfer_onboard_application_request.uri = "/open-apis/hire/v1/applications/:application_id/transfer_onboard"
        transfer_onboard_application_request.token_types = {AccessTokenType.TENANT}
        self._transfer_onboard_application_request: TransferOnboardApplicationRequest = transfer_onboard_application_request

    def user_id_type(self, user_id_type: str) -> "TransferOnboardApplicationRequestBuilder":
        self._transfer_onboard_application_request.user_id_type = user_id_type
        self._transfer_onboard_application_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "TransferOnboardApplicationRequestBuilder":
        self._transfer_onboard_application_request.department_id_type = department_id_type
        self._transfer_onboard_application_request.add_query("department_id_type", department_id_type)
        return self

    def application_id(self, application_id: str) -> "TransferOnboardApplicationRequestBuilder":
        self._transfer_onboard_application_request.application_id = application_id
        self._transfer_onboard_application_request.paths["application_id"] = str(application_id)
        return self

    def request_body(self,
                     request_body: TransferOnboardApplicationRequestBody) -> "TransferOnboardApplicationRequestBuilder":
        self._transfer_onboard_application_request.request_body = request_body
        self._transfer_onboard_application_request.body = request_body
        return self

    def build(self) -> TransferOnboardApplicationRequest:
        return self._transfer_onboard_application_request
