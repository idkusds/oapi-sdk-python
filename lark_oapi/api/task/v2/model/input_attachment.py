# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class InputAttachment(object):
    _types = {
        "resource_type": str,
        "resource_id": str,
        "file": IO[Any],
    }

    def __init__(self, d=None):
        self.resource_type: Optional[str] = None
        self.resource_id: Optional[str] = None
        self.file: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InputAttachmentBuilder":
        return InputAttachmentBuilder()


class InputAttachmentBuilder(object):
    def __init__(self) -> None:
        self._input_attachment = InputAttachment()

    def resource_type(self, resource_type: str) -> "InputAttachmentBuilder":
        self._input_attachment.resource_type = resource_type
        return self

    def resource_id(self, resource_id: str) -> "InputAttachmentBuilder":
        self._input_attachment.resource_id = resource_id
        return self

    def file(self, file: IO[Any]) -> "InputAttachmentBuilder":
        self._input_attachment.file = file
        return self

    def build(self) -> "InputAttachment":
        return self._input_attachment
