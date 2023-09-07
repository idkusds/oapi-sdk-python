# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class RemoveRemindersTaskRequestBody(object):
    _types = {
        "reminder_ids": List[str],
    }

    def __init__(self, d=None):
        self.reminder_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemoveRemindersTaskRequestBodyBuilder":
        return RemoveRemindersTaskRequestBodyBuilder()


class RemoveRemindersTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._remove_reminders_task_request_body = RemoveRemindersTaskRequestBody()

    def reminder_ids(self, reminder_ids: List[str]) -> "RemoveRemindersTaskRequestBodyBuilder":
        self._remove_reminders_task_request_body.reminder_ids = reminder_ids
        return self

    def build(self) -> "RemoveRemindersTaskRequestBody":
        return self._remove_reminders_task_request_body
