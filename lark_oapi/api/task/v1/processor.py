# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type

from lark_oapi.event.processor import IEventProcessor
from .model.p2_task_task_update_tenant_v1 import P2TaskTaskUpdateTenantV1
from .model.p2_task_task_updated_v1 import P2TaskTaskUpdatedV1
from .model.p2_task_task_comment_updated_v1 import P2TaskTaskCommentUpdatedV1


class P2TaskTaskUpdateTenantV1Processor(IEventProcessor[P2TaskTaskUpdateTenantV1]):
    def __init__(self, f: Callable[[P2TaskTaskUpdateTenantV1], None]):
        self.f = f

    def type(self) -> Type[P2TaskTaskUpdateTenantV1]:
        return P2TaskTaskUpdateTenantV1

    def do(self, data: P2TaskTaskUpdateTenantV1) -> None:
        self.f(data)


class P2TaskTaskUpdatedV1Processor(IEventProcessor[P2TaskTaskUpdatedV1]):
    def __init__(self, f: Callable[[P2TaskTaskUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2TaskTaskUpdatedV1]:
        return P2TaskTaskUpdatedV1

    def do(self, data: P2TaskTaskUpdatedV1) -> None:
        self.f(data)


class P2TaskTaskCommentUpdatedV1Processor(IEventProcessor[P2TaskTaskCommentUpdatedV1]):
    def __init__(self, f: Callable[[P2TaskTaskCommentUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2TaskTaskCommentUpdatedV1]:
        return P2TaskTaskCommentUpdatedV1

    def do(self, data: P2TaskTaskCommentUpdatedV1) -> None:
        self.f(data)
