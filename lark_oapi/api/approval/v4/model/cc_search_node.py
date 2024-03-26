# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .instance_search_link import InstanceSearchLink


class CcSearchNode(object):
    _types = {
        "user_id": str,
        "create_time": int,
        "read_status": str,
        "title": str,
        "extra": str,
        "link": InstanceSearchLink,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.read_status: Optional[str] = None
        self.title: Optional[str] = None
        self.extra: Optional[str] = None
        self.link: Optional[InstanceSearchLink] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CcSearchNodeBuilder":
        return CcSearchNodeBuilder()


class CcSearchNodeBuilder(object):
    def __init__(self) -> None:
        self._cc_search_node = CcSearchNode()

    def user_id(self, user_id: str) -> "CcSearchNodeBuilder":
        self._cc_search_node.user_id = user_id
        return self

    def create_time(self, create_time: int) -> "CcSearchNodeBuilder":
        self._cc_search_node.create_time = create_time
        return self

    def read_status(self, read_status: str) -> "CcSearchNodeBuilder":
        self._cc_search_node.read_status = read_status
        return self

    def title(self, title: str) -> "CcSearchNodeBuilder":
        self._cc_search_node.title = title
        return self

    def extra(self, extra: str) -> "CcSearchNodeBuilder":
        self._cc_search_node.extra = extra
        return self

    def link(self, link: InstanceSearchLink) -> "CcSearchNodeBuilder":
        self._cc_search_node.link = link
        return self

    def build(self) -> "CcSearchNode":
        return self._cc_search_node
