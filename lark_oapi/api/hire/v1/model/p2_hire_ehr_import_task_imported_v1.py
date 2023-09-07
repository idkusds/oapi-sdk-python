# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .department_id import DepartmentId
from .user_id import UserId


class P2HireEhrImportTaskImportedV1Data(object):
    _types = {
        "task_id": str,
        "application_id": str,
        "ehr_department_id": str,
        "ehr_requirement_id": str,
        "operator_id": str,
        "operator_user_id": UserId,
        "ehr_department": DepartmentId,
    }

    def __init__(self, d=None):
        self.task_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.ehr_department_id: Optional[str] = None
        self.ehr_requirement_id: Optional[str] = None
        self.operator_id: Optional[str] = None
        self.operator_user_id: Optional[UserId] = None
        self.ehr_department: Optional[DepartmentId] = None
        init(self, d, self._types)


class P2HireEhrImportTaskImportedV1(EventContext):
    _types = {
        "event": P2HireEhrImportTaskImportedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2HireEhrImportTaskImportedV1Data] = None
        init(self, d, self._types)
