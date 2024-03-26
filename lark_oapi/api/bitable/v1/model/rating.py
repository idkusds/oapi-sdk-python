# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Rating(object):
    _types = {
        "symbol": str,
    }

    def __init__(self, d=None):
        self.symbol: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RatingBuilder":
        return RatingBuilder()


class RatingBuilder(object):
    def __init__(self) -> None:
        self._rating = Rating()

    def symbol(self, symbol: str) -> "RatingBuilder":
        self._rating.symbol = symbol
        return self

    def build(self) -> "Rating":
        return self._rating
