# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .external_application import ExternalApplication


class UpdateExternalApplicationResponseBody(object):
    _types = {
        "external_application": ExternalApplication,
    }

    def __init__(self, d=None):
        self.external_application: Optional[ExternalApplication] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateExternalApplicationResponseBodyBuilder":
        return UpdateExternalApplicationResponseBodyBuilder()


class UpdateExternalApplicationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_external_application_response_body = UpdateExternalApplicationResponseBody()

    def external_application(self,
                             external_application: ExternalApplication) -> "UpdateExternalApplicationResponseBodyBuilder":
        self._update_external_application_response_body.external_application = external_application
        return self

    def build(self) -> "UpdateExternalApplicationResponseBody":
        return self._update_external_application_response_body
