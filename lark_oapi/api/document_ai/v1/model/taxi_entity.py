# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TaxiEntity(object):
    _types = {
        "type": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaxiEntityBuilder":
        return TaxiEntityBuilder()


class TaxiEntityBuilder(object):
    def __init__(self) -> None:
        self._taxi_entity = TaxiEntity()

    def type(self, type: str) -> "TaxiEntityBuilder":
        self._taxi_entity.type = type
        return self

    def value(self, value: str) -> "TaxiEntityBuilder":
        self._taxi_entity.value = value
        return self

    def build(self) -> "TaxiEntity":
        return self._taxi_entity
