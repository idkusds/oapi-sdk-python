# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TableMeta(object):
    _types = {
        "row_num": int,
        "col_num": int,
    }

    def __init__(self, d=None):
        self.row_num: Optional[int] = None
        self.col_num: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TableMetaBuilder":
        return TableMetaBuilder()


class TableMetaBuilder(object):
    def __init__(self) -> None:
        self._table_meta = TableMeta()

    def row_num(self, row_num: int) -> "TableMetaBuilder":
        self._table_meta.row_num = row_num
        return self

    def col_num(self, col_num: int) -> "TableMetaBuilder":
        self._table_meta.col_num = col_num
        return self

    def build(self) -> "TableMeta":
        return self._table_meta
