# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CurrentOkrSimple(object):
    _types = {
        "okr_id": str,
        "period_id": str,
    }

    def __init__(self, d=None):
        self.okr_id: Optional[str] = None
        self.period_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CurrentOkrSimpleBuilder":
        return CurrentOkrSimpleBuilder()


class CurrentOkrSimpleBuilder(object):
    def __init__(self) -> None:
        self._current_okr_simple = CurrentOkrSimple()

    def okr_id(self, okr_id: str) -> "CurrentOkrSimpleBuilder":
        self._current_okr_simple.okr_id = okr_id
        return self

    def period_id(self, period_id: str) -> "CurrentOkrSimpleBuilder":
        self._current_okr_simple.period_id = period_id
        return self

    def build(self) -> "CurrentOkrSimple":
        return self._current_okr_simple
