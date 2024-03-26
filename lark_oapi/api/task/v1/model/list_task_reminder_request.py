# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListTaskReminderRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.task_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListTaskReminderRequestBuilder":
        return ListTaskReminderRequestBuilder()


class ListTaskReminderRequestBuilder(object):

    def __init__(self) -> None:
        list_task_reminder_request = ListTaskReminderRequest()
        list_task_reminder_request.http_method = HttpMethod.GET
        list_task_reminder_request.uri = "/open-apis/task/v1/tasks/:task_id/reminders"
        list_task_reminder_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_task_reminder_request: ListTaskReminderRequest = list_task_reminder_request

    def page_size(self, page_size: int) -> "ListTaskReminderRequestBuilder":
        self._list_task_reminder_request.page_size = page_size
        self._list_task_reminder_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListTaskReminderRequestBuilder":
        self._list_task_reminder_request.page_token = page_token
        self._list_task_reminder_request.add_query("page_token", page_token)
        return self

    def task_id(self, task_id: str) -> "ListTaskReminderRequestBuilder":
        self._list_task_reminder_request.task_id = task_id
        self._list_task_reminder_request.paths["task_id"] = str(task_id)
        return self

    def build(self) -> ListTaskReminderRequest:
        return self._list_task_reminder_request
