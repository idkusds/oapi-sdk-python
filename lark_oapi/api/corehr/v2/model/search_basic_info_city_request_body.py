# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SearchBasicInfoCityRequestBody(object):
    _types = {
        "country_region_subdivision_id_list": List[str],
        "city_id_list": List[str],
        "status_list": List[int],
    }

    def __init__(self, d=None):
        self.country_region_subdivision_id_list: Optional[List[str]] = None
        self.city_id_list: Optional[List[str]] = None
        self.status_list: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoCityRequestBodyBuilder":
        return SearchBasicInfoCityRequestBodyBuilder()


class SearchBasicInfoCityRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_city_request_body = SearchBasicInfoCityRequestBody()

    def country_region_subdivision_id_list(self, country_region_subdivision_id_list: List[
        str]) -> "SearchBasicInfoCityRequestBodyBuilder":
        self._search_basic_info_city_request_body.country_region_subdivision_id_list = country_region_subdivision_id_list
        return self

    def city_id_list(self, city_id_list: List[str]) -> "SearchBasicInfoCityRequestBodyBuilder":
        self._search_basic_info_city_request_body.city_id_list = city_id_list
        return self

    def status_list(self, status_list: List[int]) -> "SearchBasicInfoCityRequestBodyBuilder":
        self._search_basic_info_city_request_body.status_list = status_list
        return self

    def build(self) -> "SearchBasicInfoCityRequestBody":
        return self._search_basic_info_city_request_body
