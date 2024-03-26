# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetWorkCityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.work_city_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetWorkCityRequestBuilder":
        return GetWorkCityRequestBuilder()


class GetWorkCityRequestBuilder(object):

    def __init__(self) -> None:
        get_work_city_request = GetWorkCityRequest()
        get_work_city_request.http_method = HttpMethod.GET
        get_work_city_request.uri = "/open-apis/contact/v3/work_cities/:work_city_id"
        get_work_city_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_work_city_request: GetWorkCityRequest = get_work_city_request

    def work_city_id(self, work_city_id: str) -> "GetWorkCityRequestBuilder":
        self._get_work_city_request.work_city_id = work_city_id
        self._get_work_city_request.paths["work_city_id"] = str(work_city_id)
        return self

    def build(self) -> GetWorkCityRequest:
        return self._get_work_city_request
