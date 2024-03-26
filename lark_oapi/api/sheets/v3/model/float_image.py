# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FloatImage(object):
    _types = {
        "float_image_id": str,
        "float_image_token": str,
        "range": str,
        "width": float,
        "height": float,
        "offset_x": float,
        "offset_y": float,
    }

    def __init__(self, d=None):
        self.float_image_id: Optional[str] = None
        self.float_image_token: Optional[str] = None
        self.range: Optional[str] = None
        self.width: Optional[float] = None
        self.height: Optional[float] = None
        self.offset_x: Optional[float] = None
        self.offset_y: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FloatImageBuilder":
        return FloatImageBuilder()


class FloatImageBuilder(object):
    def __init__(self) -> None:
        self._float_image = FloatImage()

    def float_image_id(self, float_image_id: str) -> "FloatImageBuilder":
        self._float_image.float_image_id = float_image_id
        return self

    def float_image_token(self, float_image_token: str) -> "FloatImageBuilder":
        self._float_image.float_image_token = float_image_token
        return self

    def range(self, range: str) -> "FloatImageBuilder":
        self._float_image.range = range
        return self

    def width(self, width: float) -> "FloatImageBuilder":
        self._float_image.width = width
        return self

    def height(self, height: float) -> "FloatImageBuilder":
        self._float_image.height = height
        return self

    def offset_x(self, offset_x: float) -> "FloatImageBuilder":
        self._float_image.offset_x = offset_x
        return self

    def offset_y(self, offset_y: float) -> "FloatImageBuilder":
        self._float_image.offset_y = offset_y
        return self

    def build(self) -> "FloatImage":
        return self._float_image
