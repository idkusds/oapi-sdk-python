# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SearchBasicInfoCountryRegionSubdivisionRequestBody(object):
    _types = {
        "country_region_id_list": List[str],
        "country_region_subdivision_id_list": List[str],
        "status_list": List[int],
    }

    def __init__(self, d=None):
        self.country_region_id_list: Optional[List[str]] = None
        self.country_region_subdivision_id_list: Optional[List[str]] = None
        self.status_list: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder":
        return SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder()


class SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_country_region_subdivision_request_body = SearchBasicInfoCountryRegionSubdivisionRequestBody()

    def country_region_id_list(self, country_region_id_list: List[
        str]) -> "SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder":
        self._search_basic_info_country_region_subdivision_request_body.country_region_id_list = country_region_id_list
        return self

    def country_region_subdivision_id_list(self, country_region_subdivision_id_list: List[
        str]) -> "SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder":
        self._search_basic_info_country_region_subdivision_request_body.country_region_subdivision_id_list = country_region_subdivision_id_list
        return self

    def status_list(self, status_list: List[int]) -> "SearchBasicInfoCountryRegionSubdivisionRequestBodyBuilder":
        self._search_basic_info_country_region_subdivision_request_body.status_list = status_list
        return self

    def build(self) -> "SearchBasicInfoCountryRegionSubdivisionRequestBody":
        return self._search_basic_info_country_region_subdivision_request_body
