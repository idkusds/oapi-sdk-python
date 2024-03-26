# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .eco_background_check_report_file import EcoBackgroundCheckReportFile


class UpdateProgressEcoBackgroundCheckRequestBody(object):
    _types = {
        "background_check_id": str,
        "stage_id": str,
        "stage_en_name": str,
        "stage_name": str,
        "stage_time": str,
        "result": str,
        "report_file_list": List[EcoBackgroundCheckReportFile],
    }

    def __init__(self, d=None):
        self.background_check_id: Optional[str] = None
        self.stage_id: Optional[str] = None
        self.stage_en_name: Optional[str] = None
        self.stage_name: Optional[str] = None
        self.stage_time: Optional[str] = None
        self.result: Optional[str] = None
        self.report_file_list: Optional[List[EcoBackgroundCheckReportFile]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        return UpdateProgressEcoBackgroundCheckRequestBodyBuilder()


class UpdateProgressEcoBackgroundCheckRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._update_progress_eco_background_check_request_body = UpdateProgressEcoBackgroundCheckRequestBody()

    def background_check_id(self, background_check_id: str) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.background_check_id = background_check_id
        return self

    def stage_id(self, stage_id: str) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.stage_id = stage_id
        return self

    def stage_en_name(self, stage_en_name: str) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.stage_en_name = stage_en_name
        return self

    def stage_name(self, stage_name: str) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.stage_name = stage_name
        return self

    def stage_time(self, stage_time: str) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.stage_time = stage_time
        return self

    def result(self, result: str) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.result = result
        return self

    def report_file_list(self, report_file_list: List[
        EcoBackgroundCheckReportFile]) -> "UpdateProgressEcoBackgroundCheckRequestBodyBuilder":
        self._update_progress_eco_background_check_request_body.report_file_list = report_file_list
        return self

    def build(self) -> "UpdateProgressEcoBackgroundCheckRequestBody":
        return self._update_progress_eco_background_check_request_body
