# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Location(object):
    _types = {
        "location": str,
        "pname": str,
        "cityname": str,
        "adname": str,
        "address": str,
        "name": str,
        "full_address": str,
    }

    def __init__(self, d=None):
        self.location: Optional[str] = None
        self.pname: Optional[str] = None
        self.cityname: Optional[str] = None
        self.adname: Optional[str] = None
        self.address: Optional[str] = None
        self.name: Optional[str] = None
        self.full_address: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LocationBuilder":
        return LocationBuilder()


class LocationBuilder(object):
    def __init__(self) -> None:
        self._location = Location()

    def location(self, location: str) -> "LocationBuilder":
        self._location.location = location
        return self

    def pname(self, pname: str) -> "LocationBuilder":
        self._location.pname = pname
        return self

    def cityname(self, cityname: str) -> "LocationBuilder":
        self._location.cityname = cityname
        return self

    def adname(self, adname: str) -> "LocationBuilder":
        self._location.adname = adname
        return self

    def address(self, address: str) -> "LocationBuilder":
        self._location.address = address
        return self

    def name(self, name: str) -> "LocationBuilder":
        self._location.name = name
        return self

    def full_address(self, full_address: str) -> "LocationBuilder":
        self._location.full_address = full_address
        return self

    def build(self) -> "Location":
        return self._location
