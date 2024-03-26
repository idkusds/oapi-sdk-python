# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ReplaceImageRequest(object):
    _types = {
        "token": str,
        "width": int,
        "height": int,
        "align": int,
    }

    def __init__(self, d=None):
        self.token: Optional[str] = None
        self.width: Optional[int] = None
        self.height: Optional[int] = None
        self.align: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReplaceImageRequestBuilder":
        return ReplaceImageRequestBuilder()


class ReplaceImageRequestBuilder(object):
    def __init__(self) -> None:
        self._replace_image_request = ReplaceImageRequest()

    def token(self, token: str) -> "ReplaceImageRequestBuilder":
        self._replace_image_request.token = token
        return self

    def width(self, width: int) -> "ReplaceImageRequestBuilder":
        self._replace_image_request.width = width
        return self

    def height(self, height: int) -> "ReplaceImageRequestBuilder":
        self._replace_image_request.height = height
        return self

    def align(self, align: int) -> "ReplaceImageRequestBuilder":
        self._replace_image_request.align = align
        return self

    def build(self) -> "ReplaceImageRequest":
        return self._replace_image_request
