# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class EventLocation(object):
    _types = {
        "name": str,
        "address": str,
        "latitude": float,
        "longitude": float,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.address: Optional[str] = None
        self.latitude: Optional[float] = None
        self.longitude: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventLocationBuilder":
        return EventLocationBuilder()


class EventLocationBuilder(object):
    def __init__(self) -> None:
        self._event_location = EventLocation()

    def name(self, name: str) -> "EventLocationBuilder":
        self._event_location.name = name
        return self

    def address(self, address: str) -> "EventLocationBuilder":
        self._event_location.address = address
        return self

    def latitude(self, latitude: float) -> "EventLocationBuilder":
        self._event_location.latitude = latitude
        return self

    def longitude(self, longitude: float) -> "EventLocationBuilder":
        self._event_location.longitude = longitude
        return self

    def build(self) -> "EventLocation":
        return self._event_location
