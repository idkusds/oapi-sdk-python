# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class CreateProbationAssessmentResponseBody(object):
    _types = {
        "assessment_ids": List[str],
    }

    def __init__(self, d=None):
        self.assessment_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateProbationAssessmentResponseBodyBuilder":
        return CreateProbationAssessmentResponseBodyBuilder()


class CreateProbationAssessmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_probation_assessment_response_body = CreateProbationAssessmentResponseBody()

    def assessment_ids(self, assessment_ids: List[str]) -> "CreateProbationAssessmentResponseBodyBuilder":
        self._create_probation_assessment_response_body.assessment_ids = assessment_ids
        return self

    def build(self) -> "CreateProbationAssessmentResponseBody":
        return self._create_probation_assessment_response_body