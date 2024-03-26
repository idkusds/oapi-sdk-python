# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class NodeApprover(object):
    _types = {
        "key": str,
        "value": List[str],
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NodeApproverBuilder":
        return NodeApproverBuilder()


class NodeApproverBuilder(object):
    def __init__(self) -> None:
        self._node_approver = NodeApprover()

    def key(self, key: str) -> "NodeApproverBuilder":
        self._node_approver.key = key
        return self

    def value(self, value: List[str]) -> "NodeApproverBuilder":
        self._node_approver.value = value
        return self

    def build(self) -> "NodeApprover":
        return self._node_approver
