# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .entity import Entity


class CreateDraftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.repo_id: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[Entity] = None

    @staticmethod
    def builder() -> "CreateDraftRequestBuilder":
        return CreateDraftRequestBuilder()


class CreateDraftRequestBuilder(object):

    def __init__(self) -> None:
        create_draft_request = CreateDraftRequest()
        create_draft_request.http_method = HttpMethod.POST
        create_draft_request.uri = "/open-apis/lingo/v1/drafts"
        create_draft_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_draft_request: CreateDraftRequest = create_draft_request

    def repo_id(self, repo_id: int) -> "CreateDraftRequestBuilder":
        self._create_draft_request.repo_id = repo_id
        self._create_draft_request.add_query("repo_id", repo_id)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateDraftRequestBuilder":
        self._create_draft_request.user_id_type = user_id_type
        self._create_draft_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: Entity) -> "CreateDraftRequestBuilder":
        self._create_draft_request.request_body = request_body
        self._create_draft_request.body = request_body
        return self

    def build(self) -> CreateDraftRequest:
        return self._create_draft_request
