# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Bp(object):
    _types = {
        "department_id": str,
        "hrbp_id": str,
    }

    def __init__(self, d=None):
        self.department_id: Optional[str] = None
        self.hrbp_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BpBuilder":
        return BpBuilder()


class BpBuilder(object):
    def __init__(self) -> None:
        self._bp = Bp()

    def department_id(self, department_id: str) -> "BpBuilder":
        self._bp.department_id = department_id
        return self

    def hrbp_id(self, hrbp_id: str) -> "BpBuilder":
        self._bp.hrbp_id = hrbp_id
        return self

    def build(self) -> "Bp":
        return self._bp
