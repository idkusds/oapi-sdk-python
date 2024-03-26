# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class RecognizeBusinessCardRequestBody(object):
    _types = {
        "file": IO[Any],
    }

    def __init__(self, d=None):
        self.file: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecognizeBusinessCardRequestBodyBuilder":
        return RecognizeBusinessCardRequestBodyBuilder()


class RecognizeBusinessCardRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._recognize_business_card_request_body = RecognizeBusinessCardRequestBody()

    def file(self, file: IO[Any]) -> "RecognizeBusinessCardRequestBodyBuilder":
        self._recognize_business_card_request_body.file = file
        return self

    def build(self) -> "RecognizeBusinessCardRequestBody":
        return self._recognize_business_card_request_body
