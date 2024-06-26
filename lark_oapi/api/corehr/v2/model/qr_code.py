# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .qr_code_dimension_value import QrCodeDimensionValue


class QrCode(object):
    _types = {
        "id": str,
        "png": str,
        "url": str,
        "active": bool,
        "created_by": str,
        "updated_by": str,
        "created_at": int,
        "updated_at": int,
        "dimension_value_list": List[QrCodeDimensionValue],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.png: Optional[str] = None
        self.url: Optional[str] = None
        self.active: Optional[bool] = None
        self.created_by: Optional[str] = None
        self.updated_by: Optional[str] = None
        self.created_at: Optional[int] = None
        self.updated_at: Optional[int] = None
        self.dimension_value_list: Optional[List[QrCodeDimensionValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QrCodeBuilder":
        return QrCodeBuilder()


class QrCodeBuilder(object):
    def __init__(self) -> None:
        self._qr_code = QrCode()

    def id(self, id: str) -> "QrCodeBuilder":
        self._qr_code.id = id
        return self

    def png(self, png: str) -> "QrCodeBuilder":
        self._qr_code.png = png
        return self

    def url(self, url: str) -> "QrCodeBuilder":
        self._qr_code.url = url
        return self

    def active(self, active: bool) -> "QrCodeBuilder":
        self._qr_code.active = active
        return self

    def created_by(self, created_by: str) -> "QrCodeBuilder":
        self._qr_code.created_by = created_by
        return self

    def updated_by(self, updated_by: str) -> "QrCodeBuilder":
        self._qr_code.updated_by = updated_by
        return self

    def created_at(self, created_at: int) -> "QrCodeBuilder":
        self._qr_code.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> "QrCodeBuilder":
        self._qr_code.updated_at = updated_at
        return self

    def dimension_value_list(self, dimension_value_list: List[QrCodeDimensionValue]) -> "QrCodeBuilder":
        self._qr_code.dimension_value_list = dimension_value_list
        return self

    def build(self) -> "QrCode":
        return self._qr_code
