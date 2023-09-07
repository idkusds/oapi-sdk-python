# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .node import Node


class CreateSpaceNodeResponseBody(object):
    _types = {
        "node": Node,
    }

    def __init__(self, d=None):
        self.node: Optional[Node] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSpaceNodeResponseBodyBuilder":
        return CreateSpaceNodeResponseBodyBuilder()


class CreateSpaceNodeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_space_node_response_body = CreateSpaceNodeResponseBody()

    def node(self, node: Node) -> "CreateSpaceNodeResponseBodyBuilder":
        self._create_space_node_response_body.node = node
        return self

    def build(self) -> "CreateSpaceNodeResponseBody":
        return self._create_space_node_response_body
