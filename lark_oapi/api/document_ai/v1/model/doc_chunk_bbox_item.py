# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DocChunkBboxItem(object):
    _types = {
        "bbox_positions": List[str],
    }

    def __init__(self, d=None):
        self.bbox_positions: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocChunkBboxItemBuilder":
        return DocChunkBboxItemBuilder()


class DocChunkBboxItemBuilder(object):
    def __init__(self) -> None:
        self._doc_chunk_bbox_item = DocChunkBboxItem()

    def bbox_positions(self, bbox_positions: List[str]) -> "DocChunkBboxItemBuilder":
        self._doc_chunk_bbox_item.bbox_positions = bbox_positions
        return self

    def build(self) -> "DocChunkBboxItem":
        return self._doc_chunk_bbox_item
