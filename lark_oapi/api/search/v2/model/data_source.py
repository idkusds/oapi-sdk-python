# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_meta import I18nMeta
from .i18n_meta import I18nMeta
from .connector_param import ConnectorParam


class DataSource(object):
    _types = {
        "id": int,
        "name": str,
        "state": int,
        "description": str,
        "create_time": str,
        "update_time": str,
        "is_exceed_quota": bool,
        "icon_url": str,
        "template": str,
        "searchable_fields": List[str],
        "i18n_name": I18nMeta,
        "i18n_description": I18nMeta,
        "schema_id": str,
        "app_id": str,
        "connect_type": int,
        "connector_param": ConnectorParam,
        "enable_answer": bool,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        self.state: Optional[int] = None
        self.description: Optional[str] = None
        self.create_time: Optional[str] = None
        self.update_time: Optional[str] = None
        self.is_exceed_quota: Optional[bool] = None
        self.icon_url: Optional[str] = None
        self.template: Optional[str] = None
        self.searchable_fields: Optional[List[str]] = None
        self.i18n_name: Optional[I18nMeta] = None
        self.i18n_description: Optional[I18nMeta] = None
        self.schema_id: Optional[str] = None
        self.app_id: Optional[str] = None
        self.connect_type: Optional[int] = None
        self.connector_param: Optional[ConnectorParam] = None
        self.enable_answer: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DataSourceBuilder":
        return DataSourceBuilder()


class DataSourceBuilder(object):
    def __init__(self) -> None:
        self._data_source = DataSource()

    def id(self, id: int) -> "DataSourceBuilder":
        self._data_source.id = id
        return self

    def name(self, name: str) -> "DataSourceBuilder":
        self._data_source.name = name
        return self

    def state(self, state: int) -> "DataSourceBuilder":
        self._data_source.state = state
        return self

    def description(self, description: str) -> "DataSourceBuilder":
        self._data_source.description = description
        return self

    def create_time(self, create_time: str) -> "DataSourceBuilder":
        self._data_source.create_time = create_time
        return self

    def update_time(self, update_time: str) -> "DataSourceBuilder":
        self._data_source.update_time = update_time
        return self

    def is_exceed_quota(self, is_exceed_quota: bool) -> "DataSourceBuilder":
        self._data_source.is_exceed_quota = is_exceed_quota
        return self

    def icon_url(self, icon_url: str) -> "DataSourceBuilder":
        self._data_source.icon_url = icon_url
        return self

    def template(self, template: str) -> "DataSourceBuilder":
        self._data_source.template = template
        return self

    def searchable_fields(self, searchable_fields: List[str]) -> "DataSourceBuilder":
        self._data_source.searchable_fields = searchable_fields
        return self

    def i18n_name(self, i18n_name: I18nMeta) -> "DataSourceBuilder":
        self._data_source.i18n_name = i18n_name
        return self

    def i18n_description(self, i18n_description: I18nMeta) -> "DataSourceBuilder":
        self._data_source.i18n_description = i18n_description
        return self

    def schema_id(self, schema_id: str) -> "DataSourceBuilder":
        self._data_source.schema_id = schema_id
        return self

    def app_id(self, app_id: str) -> "DataSourceBuilder":
        self._data_source.app_id = app_id
        return self

    def connect_type(self, connect_type: int) -> "DataSourceBuilder":
        self._data_source.connect_type = connect_type
        return self

    def connector_param(self, connector_param: ConnectorParam) -> "DataSourceBuilder":
        self._data_source.connector_param = connector_param
        return self

    def enable_answer(self, enable_answer: bool) -> "DataSourceBuilder":
        self._data_source.enable_answer = enable_answer
        return self

    def build(self) -> "DataSource":
        return self._data_source
