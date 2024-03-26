# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class PreviewNode(object):
    _types = {
        "node_id": str,
        "node_name": str,
        "node_type": str,
        "comments": List[str],
        "custom_node_id": str,
        "user_id_list": List[str],
        "end_cc_id_list": List[str],
        "is_empty_logic": bool,
        "is_approver_type_free": bool,
        "has_cc_type_free": bool,
    }

    def __init__(self, d=None):
        self.node_id: Optional[str] = None
        self.node_name: Optional[str] = None
        self.node_type: Optional[str] = None
        self.comments: Optional[List[str]] = None
        self.custom_node_id: Optional[str] = None
        self.user_id_list: Optional[List[str]] = None
        self.end_cc_id_list: Optional[List[str]] = None
        self.is_empty_logic: Optional[bool] = None
        self.is_approver_type_free: Optional[bool] = None
        self.has_cc_type_free: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PreviewNodeBuilder":
        return PreviewNodeBuilder()


class PreviewNodeBuilder(object):
    def __init__(self) -> None:
        self._preview_node = PreviewNode()

    def node_id(self, node_id: str) -> "PreviewNodeBuilder":
        self._preview_node.node_id = node_id
        return self

    def node_name(self, node_name: str) -> "PreviewNodeBuilder":
        self._preview_node.node_name = node_name
        return self

    def node_type(self, node_type: str) -> "PreviewNodeBuilder":
        self._preview_node.node_type = node_type
        return self

    def comments(self, comments: List[str]) -> "PreviewNodeBuilder":
        self._preview_node.comments = comments
        return self

    def custom_node_id(self, custom_node_id: str) -> "PreviewNodeBuilder":
        self._preview_node.custom_node_id = custom_node_id
        return self

    def user_id_list(self, user_id_list: List[str]) -> "PreviewNodeBuilder":
        self._preview_node.user_id_list = user_id_list
        return self

    def end_cc_id_list(self, end_cc_id_list: List[str]) -> "PreviewNodeBuilder":
        self._preview_node.end_cc_id_list = end_cc_id_list
        return self

    def is_empty_logic(self, is_empty_logic: bool) -> "PreviewNodeBuilder":
        self._preview_node.is_empty_logic = is_empty_logic
        return self

    def is_approver_type_free(self, is_approver_type_free: bool) -> "PreviewNodeBuilder":
        self._preview_node.is_approver_type_free = is_approver_type_free
        return self

    def has_cc_type_free(self, has_cc_type_free: bool) -> "PreviewNodeBuilder":
        self._preview_node.has_cc_type_free = has_cc_type_free
        return self

    def build(self) -> "PreviewNode":
        return self._preview_node
