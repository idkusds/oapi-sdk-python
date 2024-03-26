# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .system_status_sync_i18n_name import SystemStatusSyncI18nName
from .system_status_sync_i18n_explain import SystemStatusSyncI18nExplain


class SystemStatusSyncSetting(object):
    _types = {
        "is_open_by_default": bool,
        "title": str,
        "i18n_title": SystemStatusSyncI18nName,
        "explain": str,
        "i18n_explain": SystemStatusSyncI18nExplain,
    }

    def __init__(self, d=None):
        self.is_open_by_default: Optional[bool] = None
        self.title: Optional[str] = None
        self.i18n_title: Optional[SystemStatusSyncI18nName] = None
        self.explain: Optional[str] = None
        self.i18n_explain: Optional[SystemStatusSyncI18nExplain] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemStatusSyncSettingBuilder":
        return SystemStatusSyncSettingBuilder()


class SystemStatusSyncSettingBuilder(object):
    def __init__(self) -> None:
        self._system_status_sync_setting = SystemStatusSyncSetting()

    def is_open_by_default(self, is_open_by_default: bool) -> "SystemStatusSyncSettingBuilder":
        self._system_status_sync_setting.is_open_by_default = is_open_by_default
        return self

    def title(self, title: str) -> "SystemStatusSyncSettingBuilder":
        self._system_status_sync_setting.title = title
        return self

    def i18n_title(self, i18n_title: SystemStatusSyncI18nName) -> "SystemStatusSyncSettingBuilder":
        self._system_status_sync_setting.i18n_title = i18n_title
        return self

    def explain(self, explain: str) -> "SystemStatusSyncSettingBuilder":
        self._system_status_sync_setting.explain = explain
        return self

    def i18n_explain(self, i18n_explain: SystemStatusSyncI18nExplain) -> "SystemStatusSyncSettingBuilder":
        self._system_status_sync_setting.i18n_explain = i18n_explain
        return self

    def build(self) -> "SystemStatusSyncSetting":
        return self._system_status_sync_setting
