# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteTaskReminderRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_id: Optional[str] = None
        self.reminder_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteTaskReminderRequestBuilder":
        return DeleteTaskReminderRequestBuilder()


class DeleteTaskReminderRequestBuilder(object):

    def __init__(self) -> None:
        delete_task_reminder_request = DeleteTaskReminderRequest()
        delete_task_reminder_request.http_method = HttpMethod.DELETE
        delete_task_reminder_request.uri = "/open-apis/task/v1/tasks/:task_id/reminders/:reminder_id"
        delete_task_reminder_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_task_reminder_request: DeleteTaskReminderRequest = delete_task_reminder_request

    def task_id(self, task_id: str) -> "DeleteTaskReminderRequestBuilder":
        self._delete_task_reminder_request.task_id = task_id
        self._delete_task_reminder_request.paths["task_id"] = str(task_id)
        return self

    def reminder_id(self, reminder_id: str) -> "DeleteTaskReminderRequestBuilder":
        self._delete_task_reminder_request.reminder_id = reminder_id
        self._delete_task_reminder_request.paths["reminder_id"] = str(reminder_id)
        return self

    def build(self) -> DeleteTaskReminderRequest:
        return self._delete_task_reminder_request
