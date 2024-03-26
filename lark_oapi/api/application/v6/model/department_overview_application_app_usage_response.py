# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .department_overview_application_app_usage_response_body import DepartmentOverviewApplicationAppUsageResponseBody


class DepartmentOverviewApplicationAppUsageResponse(BaseResponse):
    _types = {
        "data": DepartmentOverviewApplicationAppUsageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[DepartmentOverviewApplicationAppUsageResponseBody] = None
        init(self, d, self._types)
