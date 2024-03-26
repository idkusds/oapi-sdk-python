# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .freebusy import Freebusy


class UserFreebusy(object):
    _types = {
        "freebusy_items": List[Freebusy],
        "user_id": str,
    }

    def __init__(self, d=None):
        self.freebusy_items: Optional[List[Freebusy]] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserFreebusyBuilder":
        return UserFreebusyBuilder()


class UserFreebusyBuilder(object):
    def __init__(self) -> None:
        self._user_freebusy = UserFreebusy()

    def freebusy_items(self, freebusy_items: List[Freebusy]) -> "UserFreebusyBuilder":
        self._user_freebusy.freebusy_items = freebusy_items
        return self

    def user_id(self, user_id: str) -> "UserFreebusyBuilder":
        self._user_freebusy.user_id = user_id
        return self

    def build(self) -> "UserFreebusy":
        return self._user_freebusy
