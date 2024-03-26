# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Attachment(object):
    _types = {
        "id": str,
        "url": str,
        "name": str,
        "mime": str,
        "create_time": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.url: Optional[str] = None
        self.name: Optional[str] = None
        self.mime: Optional[str] = None
        self.create_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AttachmentBuilder":
        return AttachmentBuilder()


class AttachmentBuilder(object):
    def __init__(self) -> None:
        self._attachment = Attachment()

    def id(self, id: str) -> "AttachmentBuilder":
        self._attachment.id = id
        return self

    def url(self, url: str) -> "AttachmentBuilder":
        self._attachment.url = url
        return self

    def name(self, name: str) -> "AttachmentBuilder":
        self._attachment.name = name
        return self

    def mime(self, mime: str) -> "AttachmentBuilder":
        self._attachment.mime = mime
        return self

    def create_time(self, create_time: int) -> "AttachmentBuilder":
        self._attachment.create_time = create_time
        return self

    def build(self) -> "Attachment":
        return self._attachment
