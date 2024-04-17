# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UpdateBizEntityTagRelationRequestBody(object):
    _types = {
        "tag_biz_type": str,
        "biz_entity_id": str,
        "tag_ids": List[str],
    }

    def __init__(self, d=None):
        self.tag_biz_type: Optional[str] = None
        self.biz_entity_id: Optional[str] = None
        self.tag_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateBizEntityTagRelationRequestBodyBuilder":
        return UpdateBizEntityTagRelationRequestBodyBuilder()


class UpdateBizEntityTagRelationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._update_biz_entity_tag_relation_request_body = UpdateBizEntityTagRelationRequestBody()

    def tag_biz_type(self, tag_biz_type: str) -> "UpdateBizEntityTagRelationRequestBodyBuilder":
        self._update_biz_entity_tag_relation_request_body.tag_biz_type = tag_biz_type
        return self

    def biz_entity_id(self, biz_entity_id: str) -> "UpdateBizEntityTagRelationRequestBodyBuilder":
        self._update_biz_entity_tag_relation_request_body.biz_entity_id = biz_entity_id
        return self

    def tag_ids(self, tag_ids: List[str]) -> "UpdateBizEntityTagRelationRequestBodyBuilder":
        self._update_biz_entity_tag_relation_request_body.tag_ids = tag_ids
        return self

    def build(self) -> "UpdateBizEntityTagRelationRequestBody":
        return self._update_biz_entity_tag_relation_request_body