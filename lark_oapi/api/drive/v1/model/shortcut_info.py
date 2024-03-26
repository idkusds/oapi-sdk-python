# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ShortcutInfo(object):
    _types = {
        "target_type": str,
        "target_token": str,
    }

    def __init__(self, d=None):
        self.target_type: Optional[str] = None
        self.target_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ShortcutInfoBuilder":
        return ShortcutInfoBuilder()


class ShortcutInfoBuilder(object):
    def __init__(self) -> None:
        self._shortcut_info = ShortcutInfo()

    def target_type(self, target_type: str) -> "ShortcutInfoBuilder":
        self._shortcut_info.target_type = target_type
        return self

    def target_token(self, target_token: str) -> "ShortcutInfoBuilder":
        self._shortcut_info.target_token = target_token
        return self

    def build(self) -> "ShortcutInfo":
        return self._shortcut_info
