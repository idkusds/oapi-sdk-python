# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FoodProduceEntity(object):
    _types = {
        "type": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FoodProduceEntityBuilder":
        return FoodProduceEntityBuilder()


class FoodProduceEntityBuilder(object):
    def __init__(self) -> None:
        self._food_produce_entity = FoodProduceEntity()

    def type(self, type: str) -> "FoodProduceEntityBuilder":
        self._food_produce_entity.type = type
        return self

    def value(self, value: str) -> "FoodProduceEntityBuilder":
        self._food_produce_entity.value = value
        return self

    def build(self) -> "FoodProduceEntity":
        return self._food_produce_entity
