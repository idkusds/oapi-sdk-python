# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListAdminDeptStatRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        self.department_id: Optional[str] = None
        self.contains_child_dept: Optional[bool] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListAdminDeptStatRequestBuilder":
        return ListAdminDeptStatRequestBuilder()


class ListAdminDeptStatRequestBuilder(object):

    def __init__(self, list_admin_dept_stat_request: ListAdminDeptStatRequest = ListAdminDeptStatRequest()) -> None:
        list_admin_dept_stat_request.http_method = HttpMethod.GET
        list_admin_dept_stat_request.uri = "/open-apis/admin/v1/admin_dept_stats"
        list_admin_dept_stat_request.token_types = {AccessTokenType.TENANT}
        self._list_admin_dept_stat_request: ListAdminDeptStatRequest = list_admin_dept_stat_request
    
    def department_id_type(self, department_id_type: str) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.department_id_type = department_id_type
        self._list_admin_dept_stat_request.queries["department_id_type"] = str(department_id_type)
        return self
    
    def start_date(self, start_date: str) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.start_date = start_date
        self._list_admin_dept_stat_request.queries["start_date"] = str(start_date)
        return self
    
    def end_date(self, end_date: str) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.end_date = end_date
        self._list_admin_dept_stat_request.queries["end_date"] = str(end_date)
        return self
    
    def department_id(self, department_id: str) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.department_id = department_id
        self._list_admin_dept_stat_request.queries["department_id"] = str(department_id)
        return self
    
    def contains_child_dept(self, contains_child_dept: bool) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.contains_child_dept = contains_child_dept
        self._list_admin_dept_stat_request.queries["contains_child_dept"] = str(contains_child_dept)
        return self
    
    def page_size(self, page_size: int) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.page_size = page_size
        self._list_admin_dept_stat_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ListAdminDeptStatRequestBuilder":
        self._list_admin_dept_stat_request.page_token = page_token
        self._list_admin_dept_stat_request.queries["page_token"] = str(page_token)
        return self
    

    def build(self) -> ListAdminDeptStatRequest:
        return self._list_admin_dept_stat_request