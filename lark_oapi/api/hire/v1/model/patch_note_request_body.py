# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class PatchNoteRequestBody(object):
    _types = {
        "content": str,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchNoteRequestBodyBuilder":
        return PatchNoteRequestBodyBuilder()


class PatchNoteRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_note_request_body = PatchNoteRequestBody()

    def content(self, content: str) -> "PatchNoteRequestBodyBuilder":
        self._patch_note_request_body.content = content
        return self

    def build(self) -> "PatchNoteRequestBody":
        return self._patch_note_request_body
