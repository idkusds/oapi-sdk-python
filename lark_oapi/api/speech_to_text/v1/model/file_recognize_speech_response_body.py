# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FileRecognizeSpeechResponseBody(object):
    _types = {
        "recognition_text": str,
    }

    def __init__(self, d=None):
        self.recognition_text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileRecognizeSpeechResponseBodyBuilder":
        return FileRecognizeSpeechResponseBodyBuilder()


class FileRecognizeSpeechResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._file_recognize_speech_response_body = FileRecognizeSpeechResponseBody()

    def recognition_text(self, recognition_text: str) -> "FileRecognizeSpeechResponseBodyBuilder":
        self._file_recognize_speech_response_body.recognition_text = recognition_text
        return self

    def build(self) -> "FileRecognizeSpeechResponseBody":
        return self._file_recognize_speech_response_body
