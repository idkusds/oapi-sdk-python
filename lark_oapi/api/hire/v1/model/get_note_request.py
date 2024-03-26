# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetNoteRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.note_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetNoteRequestBuilder":
        return GetNoteRequestBuilder()


class GetNoteRequestBuilder(object):

    def __init__(self) -> None:
        get_note_request = GetNoteRequest()
        get_note_request.http_method = HttpMethod.GET
        get_note_request.uri = "/open-apis/hire/v1/notes/:note_id"
        get_note_request.token_types = {AccessTokenType.TENANT}
        self._get_note_request: GetNoteRequest = get_note_request

    def user_id_type(self, user_id_type: str) -> "GetNoteRequestBuilder":
        self._get_note_request.user_id_type = user_id_type
        self._get_note_request.add_query("user_id_type", user_id_type)
        return self

    def note_id(self, note_id: str) -> "GetNoteRequestBuilder":
        self._get_note_request.note_id = note_id
        self._get_note_request.paths["note_id"] = str(note_id)
        return self

    def build(self) -> GetNoteRequest:
        return self._get_note_request
