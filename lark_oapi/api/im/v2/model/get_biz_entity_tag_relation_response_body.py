# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .tag_info_with_bind_version import TagInfoWithBindVersion


class GetBizEntityTagRelationResponseBody(object):
    _types = {
        "tag_info_with_bind_versions": List[TagInfoWithBindVersion],
    }

    def __init__(self, d=None):
        self.tag_info_with_bind_versions: Optional[List[TagInfoWithBindVersion]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetBizEntityTagRelationResponseBodyBuilder":
        return GetBizEntityTagRelationResponseBodyBuilder()


class GetBizEntityTagRelationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_biz_entity_tag_relation_response_body = GetBizEntityTagRelationResponseBody()

    def tag_info_with_bind_versions(self, tag_info_with_bind_versions: List[
        TagInfoWithBindVersion]) -> "GetBizEntityTagRelationResponseBodyBuilder":
        self._get_biz_entity_tag_relation_response_body.tag_info_with_bind_versions = tag_info_with_bind_versions
        return self

    def build(self) -> "GetBizEntityTagRelationResponseBody":
        return self._get_biz_entity_tag_relation_response_body
