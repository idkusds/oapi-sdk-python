# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .display_app import DisplayApp


class GetAppResponseBody(object):
    _types = {
        "app": DisplayApp,
    }

    def __init__(self, d=None):
        self.app: Optional[DisplayApp] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAppResponseBodyBuilder":
        return GetAppResponseBodyBuilder()


class GetAppResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_app_response_body = GetAppResponseBody()

    def app(self, app: DisplayApp) -> "GetAppResponseBodyBuilder":
        self._get_app_response_body.app = app
        return self

    def build(self) -> "GetAppResponseBody":
        return self._get_app_response_body
