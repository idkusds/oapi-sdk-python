# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .location_info import LocationInfo
from .wifi_info import WifiInfo


class LocationSetting(object):
    _types = {
        "location": LocationInfo,
        "wifi": WifiInfo,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.location: Optional[LocationInfo] = None
        self.wifi: Optional[WifiInfo] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LocationSettingBuilder":
        return LocationSettingBuilder()


class LocationSettingBuilder(object):
    def __init__(self) -> None:
        self._location_setting = LocationSetting()

    def location(self, location: LocationInfo) -> "LocationSettingBuilder":
        self._location_setting.location = location
        return self

    def wifi(self, wifi: WifiInfo) -> "LocationSettingBuilder":
        self._location_setting.wifi = wifi
        return self

    def user_id(self, user_id: str) -> "LocationSettingBuilder":
        self._location_setting.user_id = user_id
        return self

    def build(self) -> "LocationSetting":
        return self._location_setting
