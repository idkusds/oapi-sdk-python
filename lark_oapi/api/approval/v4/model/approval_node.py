# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .approval_approver_ccer import ApprovalApproverCcer
from .approver_range import ApproverRange
from .field_group import FieldGroup


class ApprovalNode(object):
    _types = {
        "id": str,
        "name": str,
        "node_type": str,
        "approver": List[ApprovalApproverCcer],
        "ccer": List[ApprovalApproverCcer],
        "privilege_field": FieldGroup,
        "approver_chosen_multi": bool,
        "approver_chosen_range": List[ApproverRange],
        "starter_assignee": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.node_type: Optional[str] = None
        self.approver: Optional[List[ApprovalApproverCcer]] = None
        self.ccer: Optional[List[ApprovalApproverCcer]] = None
        self.privilege_field: Optional[FieldGroup] = None
        self.approver_chosen_multi: Optional[bool] = None
        self.approver_chosen_range: Optional[List[ApproverRange]] = None
        self.starter_assignee: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalNodeBuilder":
        return ApprovalNodeBuilder()


class ApprovalNodeBuilder(object):
    def __init__(self) -> None:
        self._approval_node = ApprovalNode()

    def id(self, id: str) -> "ApprovalNodeBuilder":
        self._approval_node.id = id
        return self

    def name(self, name: str) -> "ApprovalNodeBuilder":
        self._approval_node.name = name
        return self

    def node_type(self, node_type: str) -> "ApprovalNodeBuilder":
        self._approval_node.node_type = node_type
        return self

    def approver(self, approver: List[ApprovalApproverCcer]) -> "ApprovalNodeBuilder":
        self._approval_node.approver = approver
        return self

    def ccer(self, ccer: List[ApprovalApproverCcer]) -> "ApprovalNodeBuilder":
        self._approval_node.ccer = ccer
        return self

    def privilege_field(self, privilege_field: FieldGroup) -> "ApprovalNodeBuilder":
        self._approval_node.privilege_field = privilege_field
        return self

    def approver_chosen_multi(self, approver_chosen_multi: bool) -> "ApprovalNodeBuilder":
        self._approval_node.approver_chosen_multi = approver_chosen_multi
        return self

    def approver_chosen_range(self, approver_chosen_range: List[ApproverRange]) -> "ApprovalNodeBuilder":
        self._approval_node.approver_chosen_range = approver_chosen_range
        return self

    def starter_assignee(self, starter_assignee: str) -> "ApprovalNodeBuilder":
        self._approval_node.starter_assignee = starter_assignee
        return self

    def build(self) -> "ApprovalNode":
        return self._approval_node
