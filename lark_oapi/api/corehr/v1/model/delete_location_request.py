# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.location_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteLocationRequestBuilder":
        return DeleteLocationRequestBuilder()


class DeleteLocationRequestBuilder(object):

    def __init__(self) -> None:
        delete_location_request = DeleteLocationRequest()
        delete_location_request.http_method = HttpMethod.DELETE
        delete_location_request.uri = "/open-apis/corehr/v1/locations/:location_id"
        delete_location_request.token_types = {AccessTokenType.TENANT}
        self._delete_location_request: DeleteLocationRequest = delete_location_request

    def location_id(self, location_id: str) -> "DeleteLocationRequestBuilder":
        self._delete_location_request.location_id = location_id
        self._delete_location_request.paths["location_id"] = str(location_id)
        return self

    def build(self) -> DeleteLocationRequest:
        return self._delete_location_request
