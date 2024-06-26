# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UserOpenAppFeedCardDeleter(object):
    _types = {
        "biz_id": str,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.biz_id: Optional[str] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserOpenAppFeedCardDeleterBuilder":
        return UserOpenAppFeedCardDeleterBuilder()


class UserOpenAppFeedCardDeleterBuilder(object):
    def __init__(self) -> None:
        self._user_open_app_feed_card_deleter = UserOpenAppFeedCardDeleter()

    def biz_id(self, biz_id: str) -> "UserOpenAppFeedCardDeleterBuilder":
        self._user_open_app_feed_card_deleter.biz_id = biz_id
        return self

    def user_id(self, user_id: str) -> "UserOpenAppFeedCardDeleterBuilder":
        self._user_open_app_feed_card_deleter.user_id = user_id
        return self

    def build(self) -> "UserOpenAppFeedCardDeleter":
        return self._user_open_app_feed_card_deleter
