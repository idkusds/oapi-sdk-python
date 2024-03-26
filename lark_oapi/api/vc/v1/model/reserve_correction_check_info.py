# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ReserveCorrectionCheckInfo(object):
    _types = {
        "invalid_host_id_list": List[str],
    }

    def __init__(self, d=None):
        self.invalid_host_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveCorrectionCheckInfoBuilder":
        return ReserveCorrectionCheckInfoBuilder()


class ReserveCorrectionCheckInfoBuilder(object):
    def __init__(self) -> None:
        self._reserve_correction_check_info = ReserveCorrectionCheckInfo()

    def invalid_host_id_list(self, invalid_host_id_list: List[str]) -> "ReserveCorrectionCheckInfoBuilder":
        self._reserve_correction_check_info.invalid_host_id_list = invalid_host_id_list
        return self

    def build(self) -> "ReserveCorrectionCheckInfo":
        return self._reserve_correction_check_info
