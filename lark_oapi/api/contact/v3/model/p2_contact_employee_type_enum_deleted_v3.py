# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .employee_type_enum import EmployeeTypeEnum


class P2ContactEmployeeTypeEnumDeletedV3Data(object):
    _types = {
        "old_enum": EmployeeTypeEnum,
    }

    def __init__(self, d=None):
        self.old_enum: Optional[EmployeeTypeEnum] = None
        init(self, d, self._types)


class P2ContactEmployeeTypeEnumDeletedV3(EventContext):
    _types = {
        "event": P2ContactEmployeeTypeEnumDeletedV3Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ContactEmployeeTypeEnumDeletedV3Data] = None
        init(self, d, self._types)
