# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .entity import Entity


class UpdateDraftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.draft_id: Optional[int] = None
        self.request_body: Optional[Entity] = None

    @staticmethod
    def builder() -> "UpdateDraftRequestBuilder":
        return UpdateDraftRequestBuilder()


class UpdateDraftRequestBuilder(object):

    def __init__(self) -> None:
        update_draft_request = UpdateDraftRequest()
        update_draft_request.http_method = HttpMethod.PUT
        update_draft_request.uri = "/open-apis/lingo/v1/drafts/:draft_id"
        update_draft_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._update_draft_request: UpdateDraftRequest = update_draft_request

    def user_id_type(self, user_id_type: str) -> "UpdateDraftRequestBuilder":
        self._update_draft_request.user_id_type = user_id_type
        self._update_draft_request.add_query("user_id_type", user_id_type)
        return self

    def draft_id(self, draft_id: int) -> "UpdateDraftRequestBuilder":
        self._update_draft_request.draft_id = draft_id
        self._update_draft_request.paths["draft_id"] = str(draft_id)
        return self

    def request_body(self, request_body: Entity) -> "UpdateDraftRequestBuilder":
        self._update_draft_request.request_body = request_body
        self._update_draft_request.body = request_body
        return self

    def build(self) -> UpdateDraftRequest:
        return self._update_draft_request
