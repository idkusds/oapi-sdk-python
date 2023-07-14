# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .media_upload_info import MediaUploadInfo


class UploadPrepareMediaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[MediaUploadInfo] = None

    @staticmethod
    def builder() -> "UploadPrepareMediaRequestBuilder":
        return UploadPrepareMediaRequestBuilder()


class UploadPrepareMediaRequestBuilder(object):

    def __init__(self, upload_prepare_media_request: UploadPrepareMediaRequest = UploadPrepareMediaRequest()) -> None:
        upload_prepare_media_request.http_method = HttpMethod.POST
        upload_prepare_media_request.uri = "/open-apis/drive/v1/medias/upload_prepare"
        upload_prepare_media_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._upload_prepare_media_request: UploadPrepareMediaRequest = upload_prepare_media_request
    
    def request_body(self, request_body: MediaUploadInfo) -> "UploadPrepareMediaRequestBuilder":
        self._upload_prepare_media_request.request_body = request_body
        self._upload_prepare_media_request.body = request_body
        return self

    def build(self) -> UploadPrepareMediaRequest:
        return self._upload_prepare_media_request