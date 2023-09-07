# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_file_comment_request_body import PatchFileCommentRequestBody


class PatchFileCommentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_type: Optional[str] = None
        self.file_token: Optional[str] = None
        self.comment_id: Optional[int] = None
        self.request_body: Optional[PatchFileCommentRequestBody] = None

    @staticmethod
    def builder() -> "PatchFileCommentRequestBuilder":
        return PatchFileCommentRequestBuilder()


class PatchFileCommentRequestBuilder(object):

    def __init__(self) -> None:
        patch_file_comment_request = PatchFileCommentRequest()
        patch_file_comment_request.http_method = HttpMethod.PATCH
        patch_file_comment_request.uri = "/open-apis/drive/v1/files/:file_token/comments/:comment_id"
        patch_file_comment_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._patch_file_comment_request: PatchFileCommentRequest = patch_file_comment_request

    def file_type(self, file_type: str) -> "PatchFileCommentRequestBuilder":
        self._patch_file_comment_request.file_type = file_type
        self._patch_file_comment_request.add_query("file_type", file_type)
        return self

    def file_token(self, file_token: str) -> "PatchFileCommentRequestBuilder":
        self._patch_file_comment_request.file_token = file_token
        self._patch_file_comment_request.paths["file_token"] = str(file_token)
        return self

    def comment_id(self, comment_id: int) -> "PatchFileCommentRequestBuilder":
        self._patch_file_comment_request.comment_id = comment_id
        self._patch_file_comment_request.paths["comment_id"] = str(comment_id)
        return self

    def request_body(self, request_body: PatchFileCommentRequestBody) -> "PatchFileCommentRequestBuilder":
        self._patch_file_comment_request.request_body = request_body
        self._patch_file_comment_request.body = request_body
        return self

    def build(self) -> PatchFileCommentRequest:
        return self._patch_file_comment_request
