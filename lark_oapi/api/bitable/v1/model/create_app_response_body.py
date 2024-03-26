# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .app import App


class CreateAppResponseBody(object):
    _types = {
        "app": App,
    }

    def __init__(self, d=None):
        self.app: Optional[App] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAppResponseBodyBuilder":
        return CreateAppResponseBodyBuilder()


class CreateAppResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_app_response_body = CreateAppResponseBody()

    def app(self, app: App) -> "CreateAppResponseBodyBuilder":
        self._create_app_response_body.app = app
        return self

    def build(self) -> "CreateAppResponseBody":
        return self._create_app_response_body
