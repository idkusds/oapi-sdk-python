# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .external_interview_assessment_dimension import ExternalInterviewAssessmentDimension


class ExternalInterviewAssessment(object):
    _types = {
        "id": str,
        "external_id": str,
        "username": str,
        "conclusion": int,
        "assessment_dimension_list": List[ExternalInterviewAssessmentDimension],
        "content": str,
        "external_interview_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.external_id: Optional[str] = None
        self.username: Optional[str] = None
        self.conclusion: Optional[int] = None
        self.assessment_dimension_list: Optional[List[ExternalInterviewAssessmentDimension]] = None
        self.content: Optional[str] = None
        self.external_interview_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalInterviewAssessmentBuilder":
        return ExternalInterviewAssessmentBuilder()


class ExternalInterviewAssessmentBuilder(object):
    def __init__(self) -> None:
        self._external_interview_assessment = ExternalInterviewAssessment()

    def id(self, id: str) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.id = id
        return self

    def external_id(self, external_id: str) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.external_id = external_id
        return self

    def username(self, username: str) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.username = username
        return self

    def conclusion(self, conclusion: int) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.conclusion = conclusion
        return self

    def assessment_dimension_list(self, assessment_dimension_list: List[
        ExternalInterviewAssessmentDimension]) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.assessment_dimension_list = assessment_dimension_list
        return self

    def content(self, content: str) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.content = content
        return self

    def external_interview_id(self, external_interview_id: str) -> "ExternalInterviewAssessmentBuilder":
        self._external_interview_assessment.external_interview_id = external_interview_id
        return self

    def build(self) -> "ExternalInterviewAssessment":
        return self._external_interview_assessment
