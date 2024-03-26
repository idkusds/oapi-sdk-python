# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .instance_cc import InstanceCc


class CcInstanceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[InstanceCc] = None

    @staticmethod
    def builder() -> "CcInstanceRequestBuilder":
        return CcInstanceRequestBuilder()


class CcInstanceRequestBuilder(object):

    def __init__(self) -> None:
        cc_instance_request = CcInstanceRequest()
        cc_instance_request.http_method = HttpMethod.POST
        cc_instance_request.uri = "/open-apis/approval/v4/instances/cc"
        cc_instance_request.token_types = {AccessTokenType.TENANT}
        self._cc_instance_request: CcInstanceRequest = cc_instance_request

    def user_id_type(self, user_id_type: str) -> "CcInstanceRequestBuilder":
        self._cc_instance_request.user_id_type = user_id_type
        self._cc_instance_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: InstanceCc) -> "CcInstanceRequestBuilder":
        self._cc_instance_request.request_body = request_body
        self._cc_instance_request.body = request_body
        return self

    def build(self) -> CcInstanceRequest:
        return self._cc_instance_request
