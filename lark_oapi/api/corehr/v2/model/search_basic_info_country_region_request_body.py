# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class SearchBasicInfoCountryRegionRequestBody(object):
    _types = {
        "country_region_id_list": List[str],
        "status_list": List[int],
    }

    def __init__(self, d=None):
        self.country_region_id_list: Optional[List[str]] = None
        self.status_list: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoCountryRegionRequestBodyBuilder":
        return SearchBasicInfoCountryRegionRequestBodyBuilder()


class SearchBasicInfoCountryRegionRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_country_region_request_body = SearchBasicInfoCountryRegionRequestBody()

    def country_region_id_list(self,
                               country_region_id_list: List[str]) -> "SearchBasicInfoCountryRegionRequestBodyBuilder":
        self._search_basic_info_country_region_request_body.country_region_id_list = country_region_id_list
        return self

    def status_list(self, status_list: List[int]) -> "SearchBasicInfoCountryRegionRequestBodyBuilder":
        self._search_basic_info_country_region_request_body.status_list = status_list
        return self

    def build(self) -> "SearchBasicInfoCountryRegionRequestBody":
        return self._search_basic_info_country_region_request_body