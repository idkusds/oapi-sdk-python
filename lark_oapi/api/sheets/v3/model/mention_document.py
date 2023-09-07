# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .segment_style import SegmentStyle


class MentionDocument(object):
    _types = {
        "title": str,
        "object_type": str,
        "token": str,
        "segment_style": SegmentStyle,
    }

    def __init__(self, d=None):
        self.title: Optional[str] = None
        self.object_type: Optional[str] = None
        self.token: Optional[str] = None
        self.segment_style: Optional[SegmentStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MentionDocumentBuilder":
        return MentionDocumentBuilder()


class MentionDocumentBuilder(object):
    def __init__(self) -> None:
        self._mention_document = MentionDocument()

    def title(self, title: str) -> "MentionDocumentBuilder":
        self._mention_document.title = title
        return self

    def object_type(self, object_type: str) -> "MentionDocumentBuilder":
        self._mention_document.object_type = object_type
        return self

    def token(self, token: str) -> "MentionDocumentBuilder":
        self._mention_document.token = token
        return self

    def segment_style(self, segment_style: SegmentStyle) -> "MentionDocumentBuilder":
        self._mention_document.segment_style = segment_style
        return self

    def build(self) -> "MentionDocument":
        return self._mention_document
