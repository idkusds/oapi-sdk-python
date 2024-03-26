# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .file_recognize_speech_request_body import FileRecognizeSpeechRequestBody


class FileRecognizeSpeechRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[FileRecognizeSpeechRequestBody] = None

    @staticmethod
    def builder() -> "FileRecognizeSpeechRequestBuilder":
        return FileRecognizeSpeechRequestBuilder()


class FileRecognizeSpeechRequestBuilder(object):

    def __init__(self) -> None:
        file_recognize_speech_request = FileRecognizeSpeechRequest()
        file_recognize_speech_request.http_method = HttpMethod.POST
        file_recognize_speech_request.uri = "/open-apis/speech_to_text/v1/speech/file_recognize"
        file_recognize_speech_request.token_types = {AccessTokenType.TENANT}
        self._file_recognize_speech_request: FileRecognizeSpeechRequest = file_recognize_speech_request

    def request_body(self, request_body: FileRecognizeSpeechRequestBody) -> "FileRecognizeSpeechRequestBuilder":
        self._file_recognize_speech_request.request_body = request_body
        self._file_recognize_speech_request.body = request_body
        return self

    def build(self) -> FileRecognizeSpeechRequest:
        return self._file_recognize_speech_request
