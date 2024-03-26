# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TaskRollback(object):
    _types = {
        "user_id": str,
        "task_id": int,
        "reason": str,
        "extra": str,
        "task_def_key": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.task_id: Optional[int] = None
        self.reason: Optional[str] = None
        self.extra: Optional[str] = None
        self.task_def_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskRollbackBuilder":
        return TaskRollbackBuilder()


class TaskRollbackBuilder(object):
    def __init__(self) -> None:
        self._task_rollback = TaskRollback()

    def user_id(self, user_id: str) -> "TaskRollbackBuilder":
        self._task_rollback.user_id = user_id
        return self

    def task_id(self, task_id: int) -> "TaskRollbackBuilder":
        self._task_rollback.task_id = task_id
        return self

    def reason(self, reason: str) -> "TaskRollbackBuilder":
        self._task_rollback.reason = reason
        return self

    def extra(self, extra: str) -> "TaskRollbackBuilder":
        self._task_rollback.extra = extra
        return self

    def task_def_key(self, task_def_key: str) -> "TaskRollbackBuilder":
        self._task_rollback.task_def_key = task_def_key
        return self

    def build(self) -> "TaskRollback":
        return self._task_rollback
