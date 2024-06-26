# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OpenAppFeedCardUrl(object):
    _types = {
        "url": str,
        "android_url": str,
        "ios_url": str,
        "pc_url": str,
    }

    def __init__(self, d=None):
        self.url: Optional[str] = None
        self.android_url: Optional[str] = None
        self.ios_url: Optional[str] = None
        self.pc_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OpenAppFeedCardUrlBuilder":
        return OpenAppFeedCardUrlBuilder()


class OpenAppFeedCardUrlBuilder(object):
    def __init__(self) -> None:
        self._open_app_feed_card_url = OpenAppFeedCardUrl()

    def url(self, url: str) -> "OpenAppFeedCardUrlBuilder":
        self._open_app_feed_card_url.url = url
        return self

    def android_url(self, android_url: str) -> "OpenAppFeedCardUrlBuilder":
        self._open_app_feed_card_url.android_url = android_url
        return self

    def ios_url(self, ios_url: str) -> "OpenAppFeedCardUrlBuilder":
        self._open_app_feed_card_url.ios_url = ios_url
        return self

    def pc_url(self, pc_url: str) -> "OpenAppFeedCardUrlBuilder":
        self._open_app_feed_card_url.pc_url = pc_url
        return self

    def build(self) -> "OpenAppFeedCardUrl":
        return self._open_app_feed_card_url
