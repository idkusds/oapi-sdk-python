# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class NodeAutoApproval(object):
    _types = {
        "node_id_type": str,
        "node_id": str,
    }

    def __init__(self, d=None):
        self.node_id_type: Optional[str] = None
        self.node_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NodeAutoApprovalBuilder":
        return NodeAutoApprovalBuilder()


class NodeAutoApprovalBuilder(object):
    def __init__(self) -> None:
        self._node_auto_approval = NodeAutoApproval()

    def node_id_type(self, node_id_type: str) -> "NodeAutoApprovalBuilder":
        self._node_auto_approval.node_id_type = node_id_type
        return self

    def node_id(self, node_id: str) -> "NodeAutoApprovalBuilder":
        self._node_auto_approval.node_id = node_id
        return self

    def build(self) -> "NodeAutoApproval":
        return self._node_auto_approval
