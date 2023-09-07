# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DisplayAppV2(object):
    _types = {
        "app_token": str,
        "name": str,
        "is_advanced": bool,
    }

    def __init__(self, d=None):
        self.app_token: Optional[str] = None
        self.name: Optional[str] = None
        self.is_advanced: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DisplayAppV2Builder":
        return DisplayAppV2Builder()


class DisplayAppV2Builder(object):
    def __init__(self) -> None:
        self._display_app_v2 = DisplayAppV2()

    def app_token(self, app_token: str) -> "DisplayAppV2Builder":
        self._display_app_v2.app_token = app_token
        return self

    def name(self, name: str) -> "DisplayAppV2Builder":
        self._display_app_v2.name = name
        return self

    def is_advanced(self, is_advanced: bool) -> "DisplayAppV2Builder":
        self._display_app_v2.is_advanced = is_advanced
        return self

    def build(self) -> "DisplayAppV2":
        return self._display_app_v2
