# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_task_remedy import UserTaskRemedy


class CreateUserTaskRemedyResponseBody(object):
    _types = {
        "user_remedy": UserTaskRemedy,
    }

    def __init__(self, d=None):
        self.user_remedy: Optional[UserTaskRemedy] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateUserTaskRemedyResponseBodyBuilder":
        return CreateUserTaskRemedyResponseBodyBuilder()


class CreateUserTaskRemedyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_user_task_remedy_response_body = CreateUserTaskRemedyResponseBody()

    def user_remedy(self, user_remedy: UserTaskRemedy) -> "CreateUserTaskRemedyResponseBodyBuilder":
        self._create_user_task_remedy_response_body.user_remedy = user_remedy
        return self

    def build(self) -> "CreateUserTaskRemedyResponseBody":
        return self._create_user_task_remedy_response_body
