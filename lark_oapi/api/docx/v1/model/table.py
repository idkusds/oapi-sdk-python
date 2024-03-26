# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .table_property import TableProperty


class Table(object):
    _types = {
        "cells": List[str],
        "property": TableProperty,
    }

    def __init__(self, d=None):
        self.cells: Optional[List[str]] = None
        self.property: Optional[TableProperty] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TableBuilder":
        return TableBuilder()


class TableBuilder(object):
    def __init__(self) -> None:
        self._table = Table()

    def cells(self, cells: List[str]) -> "TableBuilder":
        self._table.cells = cells
        return self

    def property(self, property: TableProperty) -> "TableBuilder":
        self._table.property = property
        return self

    def build(self) -> "Table":
        return self._table
