# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ImageInfo(object):
    _types = {
        "file_token": str,
        "url": str,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageInfoBuilder":
        return ImageInfoBuilder()


class ImageInfoBuilder(object):
    def __init__(self) -> None:
        self._image_info = ImageInfo()

    def file_token(self, file_token: str) -> "ImageInfoBuilder":
        self._image_info.file_token = file_token
        return self

    def url(self, url: str) -> "ImageInfoBuilder":
        self._image_info.url = url
        return self

    def build(self) -> "ImageInfo":
        return self._image_info
