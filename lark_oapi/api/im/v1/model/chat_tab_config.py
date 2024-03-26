# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ChatTabConfig(object):
    _types = {
        "icon_key": str,
        "is_built_in": bool,
    }

    def __init__(self, d=None):
        self.icon_key: Optional[str] = None
        self.is_built_in: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatTabConfigBuilder":
        return ChatTabConfigBuilder()


class ChatTabConfigBuilder(object):
    def __init__(self) -> None:
        self._chat_tab_config = ChatTabConfig()

    def icon_key(self, icon_key: str) -> "ChatTabConfigBuilder":
        self._chat_tab_config.icon_key = icon_key
        return self

    def is_built_in(self, is_built_in: bool) -> "ChatTabConfigBuilder":
        self._chat_tab_config.is_built_in = is_built_in
        return self

    def build(self) -> "ChatTabConfig":
        return self._chat_tab_config
