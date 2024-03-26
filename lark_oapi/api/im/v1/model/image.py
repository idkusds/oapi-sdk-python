# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Image(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageBuilder":
        return ImageBuilder()


class ImageBuilder(object):
    def __init__(self) -> None:
        self._image = Image()

    def build(self) -> "Image":
        return self._image
