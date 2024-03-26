# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteVisitorRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.visitor_id: Optional[int] = None

    @staticmethod
    def builder() -> "DeleteVisitorRequestBuilder":
        return DeleteVisitorRequestBuilder()


class DeleteVisitorRequestBuilder(object):

    def __init__(self) -> None:
        delete_visitor_request = DeleteVisitorRequest()
        delete_visitor_request.http_method = HttpMethod.DELETE
        delete_visitor_request.uri = "/open-apis/acs/v1/visitors/:visitor_id"
        delete_visitor_request.token_types = {AccessTokenType.USER}
        self._delete_visitor_request: DeleteVisitorRequest = delete_visitor_request

    def user_id_type(self, user_id_type: str) -> "DeleteVisitorRequestBuilder":
        self._delete_visitor_request.user_id_type = user_id_type
        self._delete_visitor_request.add_query("user_id_type", user_id_type)
        return self

    def visitor_id(self, visitor_id: int) -> "DeleteVisitorRequestBuilder":
        self._delete_visitor_request.visitor_id = visitor_id
        self._delete_visitor_request.paths["visitor_id"] = str(visitor_id)
        return self

    def build(self) -> DeleteVisitorRequest:
        return self._delete_visitor_request
