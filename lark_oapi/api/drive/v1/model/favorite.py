# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Favorite(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FavoriteBuilder":
        return FavoriteBuilder()


class FavoriteBuilder(object):
    def __init__(self) -> None:
        self._favorite = Favorite()

    def build(self) -> "Favorite":
        return self._favorite
