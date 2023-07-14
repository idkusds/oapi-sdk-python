# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .search_assigned_user_request_body import SearchAssignedUserRequestBody


class SearchAssignedUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[SearchAssignedUserRequestBody] = None

    @staticmethod
    def builder() -> "SearchAssignedUserRequestBuilder":
        return SearchAssignedUserRequestBuilder()


class SearchAssignedUserRequestBuilder(object):

    def __init__(self, search_assigned_user_request: SearchAssignedUserRequest = SearchAssignedUserRequest()) -> None:
        search_assigned_user_request.http_method = HttpMethod.POST
        search_assigned_user_request.uri = "/open-apis/corehr/v1/assigned_users/search"
        search_assigned_user_request.token_types = {AccessTokenType.TENANT}
        self._search_assigned_user_request: SearchAssignedUserRequest = search_assigned_user_request
    
    def user_id_type(self, user_id_type: str) -> "SearchAssignedUserRequestBuilder":
        self._search_assigned_user_request.user_id_type = user_id_type
        self._search_assigned_user_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def request_body(self, request_body: SearchAssignedUserRequestBody) -> "SearchAssignedUserRequestBuilder":
        self._search_assigned_user_request.request_body = request_body
        self._search_assigned_user_request.body = request_body
        return self

    def build(self) -> SearchAssignedUserRequest:
        return self._search_assigned_user_request