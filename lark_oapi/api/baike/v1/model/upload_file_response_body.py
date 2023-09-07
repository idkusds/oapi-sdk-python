# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class UploadFileResponseBody(object):
    _types = {
        "file_token": str,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadFileResponseBodyBuilder":
        return UploadFileResponseBodyBuilder()


class UploadFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_file_response_body = UploadFileResponseBody()

    def file_token(self, file_token: str) -> "UploadFileResponseBodyBuilder":
        self._upload_file_response_body.file_token = file_token
        return self

    def build(self) -> "UploadFileResponseBody":
        return self._upload_file_response_body
