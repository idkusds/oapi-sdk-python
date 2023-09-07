# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class App(object):
    _types = {
        "app_token": str,
        "name": str,
        "revision": int,
        "folder_token": str,
        "url": str,
        "default_table_id": str,
    }

    def __init__(self, d=None):
        self.app_token: Optional[str] = None
        self.name: Optional[str] = None
        self.revision: Optional[int] = None
        self.folder_token: Optional[str] = None
        self.url: Optional[str] = None
        self.default_table_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppBuilder":
        return AppBuilder()


class AppBuilder(object):
    def __init__(self) -> None:
        self._app = App()

    def app_token(self, app_token: str) -> "AppBuilder":
        self._app.app_token = app_token
        return self

    def name(self, name: str) -> "AppBuilder":
        self._app.name = name
        return self

    def revision(self, revision: int) -> "AppBuilder":
        self._app.revision = revision
        return self

    def folder_token(self, folder_token: str) -> "AppBuilder":
        self._app.folder_token = folder_token
        return self

    def url(self, url: str) -> "AppBuilder":
        self._app.url = url
        return self

    def default_table_id(self, default_table_id: str) -> "AppBuilder":
        self._app.default_table_id = default_table_id
        return self

    def build(self) -> "App":
        return self._app
