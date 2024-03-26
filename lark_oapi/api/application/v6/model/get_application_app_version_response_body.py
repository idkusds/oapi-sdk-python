# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .application_app_version import ApplicationAppVersion


class GetApplicationAppVersionResponseBody(object):
    _types = {
        "app_version": ApplicationAppVersion,
    }

    def __init__(self, d=None):
        self.app_version: Optional[ApplicationAppVersion] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetApplicationAppVersionResponseBodyBuilder":
        return GetApplicationAppVersionResponseBodyBuilder()


class GetApplicationAppVersionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_application_app_version_response_body = GetApplicationAppVersionResponseBody()

    def app_version(self, app_version: ApplicationAppVersion) -> "GetApplicationAppVersionResponseBodyBuilder":
        self._get_application_app_version_response_body.app_version = app_version
        return self

    def build(self) -> "GetApplicationAppVersionResponseBody":
        return self._get_application_app_version_response_body
