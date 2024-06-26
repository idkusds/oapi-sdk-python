# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OpenFailedUserAppFeedCardItem(object):
    _types = {
        "biz_id": str,
        "user_id": str,
        "reason": str,
    }

    def __init__(self, d=None):
        self.biz_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.reason: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OpenFailedUserAppFeedCardItemBuilder":
        return OpenFailedUserAppFeedCardItemBuilder()


class OpenFailedUserAppFeedCardItemBuilder(object):
    def __init__(self) -> None:
        self._open_failed_user_app_feed_card_item = OpenFailedUserAppFeedCardItem()

    def biz_id(self, biz_id: str) -> "OpenFailedUserAppFeedCardItemBuilder":
        self._open_failed_user_app_feed_card_item.biz_id = biz_id
        return self

    def user_id(self, user_id: str) -> "OpenFailedUserAppFeedCardItemBuilder":
        self._open_failed_user_app_feed_card_item.user_id = user_id
        return self

    def reason(self, reason: str) -> "OpenFailedUserAppFeedCardItemBuilder":
        self._open_failed_user_app_feed_card_item.reason = reason
        return self

    def build(self) -> "OpenFailedUserAppFeedCardItem":
        return self._open_failed_user_app_feed_card_item
