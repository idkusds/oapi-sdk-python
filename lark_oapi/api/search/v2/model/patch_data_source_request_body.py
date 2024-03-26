# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_meta import I18nMeta
from .i18n_meta import I18nMeta
from .connector_param import ConnectorParam


class PatchDataSourceRequestBody(object):
    _types = {
        "name": str,
        "state": int,
        "description": str,
        "icon_url": str,
        "i18n_name": I18nMeta,
        "i18n_description": I18nMeta,
        "connector_param": ConnectorParam,
        "enable_answer": bool,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.state: Optional[int] = None
        self.description: Optional[str] = None
        self.icon_url: Optional[str] = None
        self.i18n_name: Optional[I18nMeta] = None
        self.i18n_description: Optional[I18nMeta] = None
        self.connector_param: Optional[ConnectorParam] = None
        self.enable_answer: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchDataSourceRequestBodyBuilder":
        return PatchDataSourceRequestBodyBuilder()


class PatchDataSourceRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_data_source_request_body = PatchDataSourceRequestBody()

    def name(self, name: str) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.name = name
        return self

    def state(self, state: int) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.state = state
        return self

    def description(self, description: str) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.description = description
        return self

    def icon_url(self, icon_url: str) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.icon_url = icon_url
        return self

    def i18n_name(self, i18n_name: I18nMeta) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.i18n_name = i18n_name
        return self

    def i18n_description(self, i18n_description: I18nMeta) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.i18n_description = i18n_description
        return self

    def connector_param(self, connector_param: ConnectorParam) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.connector_param = connector_param
        return self

    def enable_answer(self, enable_answer: bool) -> "PatchDataSourceRequestBodyBuilder":
        self._patch_data_source_request_body.enable_answer = enable_answer
        return self

    def build(self) -> "PatchDataSourceRequestBody":
        return self._patch_data_source_request_body
