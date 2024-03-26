# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .process_form_variable import ProcessFormVariable


class ProcessApprover(object):
    _types = {
        "status": int,
        "user_id": str,
        "system_approval": bool,
        "reason": str,
        "field_values": List[ProcessFormVariable],
    }

    def __init__(self, d=None):
        self.status: Optional[int] = None
        self.user_id: Optional[str] = None
        self.system_approval: Optional[bool] = None
        self.reason: Optional[str] = None
        self.field_values: Optional[List[ProcessFormVariable]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProcessApproverBuilder":
        return ProcessApproverBuilder()


class ProcessApproverBuilder(object):
    def __init__(self) -> None:
        self._process_approver = ProcessApprover()

    def status(self, status: int) -> "ProcessApproverBuilder":
        self._process_approver.status = status
        return self

    def user_id(self, user_id: str) -> "ProcessApproverBuilder":
        self._process_approver.user_id = user_id
        return self

    def system_approval(self, system_approval: bool) -> "ProcessApproverBuilder":
        self._process_approver.system_approval = system_approval
        return self

    def reason(self, reason: str) -> "ProcessApproverBuilder":
        self._process_approver.reason = reason
        return self

    def field_values(self, field_values: List[ProcessFormVariable]) -> "ProcessApproverBuilder":
        self._process_approver.field_values = field_values
        return self

    def build(self) -> "ProcessApprover":
        return self._process_approver
