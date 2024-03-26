# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .country import Country


class City(object):
    _types = {
        "city_code": str,
        "name": str,
        "en_name": str,
        "country": Country,
    }

    def __init__(self, d=None):
        self.city_code: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.country: Optional[Country] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CityBuilder":
        return CityBuilder()


class CityBuilder(object):
    def __init__(self) -> None:
        self._city = City()

    def city_code(self, city_code: str) -> "CityBuilder":
        self._city.city_code = city_code
        return self

    def name(self, name: str) -> "CityBuilder":
        self._city.name = name
        return self

    def en_name(self, en_name: str) -> "CityBuilder":
        self._city.en_name = en_name
        return self

    def country(self, country: Country) -> "CityBuilder":
        self._city.country = country
        return self

    def build(self) -> "City":
        return self._city
