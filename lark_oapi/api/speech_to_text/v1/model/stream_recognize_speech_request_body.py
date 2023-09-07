# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .speech import Speech
from .stream_config import StreamConfig


class StreamRecognizeSpeechRequestBody(object):
    _types = {
        "speech": Speech,
        "config": StreamConfig,
    }

    def __init__(self, d=None):
        self.speech: Optional[Speech] = None
        self.config: Optional[StreamConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StreamRecognizeSpeechRequestBodyBuilder":
        return StreamRecognizeSpeechRequestBodyBuilder()


class StreamRecognizeSpeechRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._stream_recognize_speech_request_body = StreamRecognizeSpeechRequestBody()

    def speech(self, speech: Speech) -> "StreamRecognizeSpeechRequestBodyBuilder":
        self._stream_recognize_speech_request_body.speech = speech
        return self

    def config(self, config: StreamConfig) -> "StreamRecognizeSpeechRequestBodyBuilder":
        self._stream_recognize_speech_request_body.config = config
        return self

    def build(self) -> "StreamRecognizeSpeechRequestBody":
        return self._stream_recognize_speech_request_body
