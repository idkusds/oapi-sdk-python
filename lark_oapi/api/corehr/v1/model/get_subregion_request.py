# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetSubregionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.subregion_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetSubregionRequestBuilder":
        return GetSubregionRequestBuilder()


class GetSubregionRequestBuilder(object):

    def __init__(self) -> None:
        get_subregion_request = GetSubregionRequest()
        get_subregion_request.http_method = HttpMethod.GET
        get_subregion_request.uri = "/open-apis/corehr/v1/subregions/:subregion_id"
        get_subregion_request.token_types = {AccessTokenType.TENANT}
        self._get_subregion_request: GetSubregionRequest = get_subregion_request

    def subregion_id(self, subregion_id: str) -> "GetSubregionRequestBuilder":
        self._get_subregion_request.subregion_id = subregion_id
        self._get_subregion_request.paths["subregion_id"] = str(subregion_id)
        return self

    def build(self) -> GetSubregionRequest:
        return self._get_subregion_request
