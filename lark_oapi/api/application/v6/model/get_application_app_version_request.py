# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetApplicationAppVersionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.lang: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.app_id: Optional[str] = None
        self.version_id: Optional[int] = None

    @staticmethod
    def builder() -> "GetApplicationAppVersionRequestBuilder":
        return GetApplicationAppVersionRequestBuilder()


class GetApplicationAppVersionRequestBuilder(object):

    def __init__(self) -> None:
        get_application_app_version_request = GetApplicationAppVersionRequest()
        get_application_app_version_request.http_method = HttpMethod.GET
        get_application_app_version_request.uri = "/open-apis/application/v6/applications/:app_id/app_versions/:version_id"
        get_application_app_version_request.token_types = {AccessTokenType.TENANT}
        self._get_application_app_version_request: GetApplicationAppVersionRequest = get_application_app_version_request

    def lang(self, lang: str) -> "GetApplicationAppVersionRequestBuilder":
        self._get_application_app_version_request.lang = lang
        self._get_application_app_version_request.add_query("lang", lang)
        return self

    def user_id_type(self, user_id_type: str) -> "GetApplicationAppVersionRequestBuilder":
        self._get_application_app_version_request.user_id_type = user_id_type
        self._get_application_app_version_request.add_query("user_id_type", user_id_type)
        return self

    def app_id(self, app_id: str) -> "GetApplicationAppVersionRequestBuilder":
        self._get_application_app_version_request.app_id = app_id
        self._get_application_app_version_request.paths["app_id"] = str(app_id)
        return self

    def version_id(self, version_id: int) -> "GetApplicationAppVersionRequestBuilder":
        self._get_application_app_version_request.version_id = version_id
        self._get_application_app_version_request.paths["version_id"] = str(version_id)
        return self

    def build(self) -> GetApplicationAppVersionRequest:
        return self._get_application_app_version_request
