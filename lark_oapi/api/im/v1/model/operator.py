# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Operator(object):
    _types = {
        "operator_id": str,
        "operator_type": str,
    }

    def __init__(self, d=None):
        self.operator_id: Optional[str] = None
        self.operator_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OperatorBuilder":
        return OperatorBuilder()


class OperatorBuilder(object):
    def __init__(self) -> None:
        self._operator = Operator()

    def operator_id(self, operator_id: str) -> "OperatorBuilder":
        self._operator.operator_id = operator_id
        return self

    def operator_type(self, operator_type: str) -> "OperatorBuilder":
        self._operator.operator_type = operator_type
        return self

    def build(self) -> "Operator":
        return self._operator
