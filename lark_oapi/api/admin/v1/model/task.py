# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .file import File


class Task(object):
    _types = {
        "original_user_id": str,
        "target_owner_id": str,
        "file_list": List[File],
        "task_id": str,
        "status": int,
        "original_user_email": str,
        "target_owner_email": str,
    }

    def __init__(self, d=None):
        self.original_user_id: Optional[str] = None
        self.target_owner_id: Optional[str] = None
        self.file_list: Optional[List[File]] = None
        self.task_id: Optional[str] = None
        self.status: Optional[int] = None
        self.original_user_email: Optional[str] = None
        self.target_owner_email: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskBuilder":
        return TaskBuilder()


class TaskBuilder(object):
    def __init__(self) -> None:
        self._task = Task()

    def original_user_id(self, original_user_id: str) -> "TaskBuilder":
        self._task.original_user_id = original_user_id
        return self

    def target_owner_id(self, target_owner_id: str) -> "TaskBuilder":
        self._task.target_owner_id = target_owner_id
        return self

    def file_list(self, file_list: List[File]) -> "TaskBuilder":
        self._task.file_list = file_list
        return self

    def task_id(self, task_id: str) -> "TaskBuilder":
        self._task.task_id = task_id
        return self

    def status(self, status: int) -> "TaskBuilder":
        self._task.status = status
        return self

    def original_user_email(self, original_user_email: str) -> "TaskBuilder":
        self._task.original_user_email = original_user_email
        return self

    def target_owner_email(self, target_owner_email: str) -> "TaskBuilder":
        self._task.target_owner_email = target_owner_email
        return self

    def build(self) -> "Task":
        return self._task
