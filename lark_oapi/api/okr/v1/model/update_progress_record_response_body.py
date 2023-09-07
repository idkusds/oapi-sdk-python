# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .content_block import ContentBlock


class UpdateProgressRecordResponseBody(object):
    _types = {
        "progress_id": int,
        "modify_time": int,
        "content": ContentBlock,
    }

    def __init__(self, d=None):
        self.progress_id: Optional[int] = None
        self.modify_time: Optional[int] = None
        self.content: Optional[ContentBlock] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProgressRecordResponseBodyBuilder":
        return UpdateProgressRecordResponseBodyBuilder()


class UpdateProgressRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_progress_record_response_body = UpdateProgressRecordResponseBody()

    def progress_id(self, progress_id: int) -> "UpdateProgressRecordResponseBodyBuilder":
        self._update_progress_record_response_body.progress_id = progress_id
        return self

    def modify_time(self, modify_time: int) -> "UpdateProgressRecordResponseBodyBuilder":
        self._update_progress_record_response_body.modify_time = modify_time
        return self

    def content(self, content: ContentBlock) -> "UpdateProgressRecordResponseBodyBuilder":
        self._update_progress_record_response_body.content = content
        return self

    def build(self) -> "UpdateProgressRecordResponseBody":
        return self._update_progress_record_response_body
