# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class EcoExamResultDetail(object):
    _types = {
        "id": str,
        "name": str,
        "result": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.result: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoExamResultDetailBuilder":
        return EcoExamResultDetailBuilder()


class EcoExamResultDetailBuilder(object):
    def __init__(self) -> None:
        self._eco_exam_result_detail = EcoExamResultDetail()

    def id(self, id: str) -> "EcoExamResultDetailBuilder":
        self._eco_exam_result_detail.id = id
        return self

    def name(self, name: str) -> "EcoExamResultDetailBuilder":
        self._eco_exam_result_detail.name = name
        return self

    def result(self, result: str) -> "EcoExamResultDetailBuilder":
        self._eco_exam_result_detail.result = result
        return self

    def build(self) -> "EcoExamResultDetail":
        return self._eco_exam_result_detail
