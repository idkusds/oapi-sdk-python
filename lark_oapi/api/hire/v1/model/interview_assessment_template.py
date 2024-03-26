# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .interview_assessment_template_args import InterviewAssessmentTemplateArgs


class InterviewAssessmentTemplate(object):
    _types = {
        "id": str,
        "name": I18n,
        "args": InterviewAssessmentTemplateArgs,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.args: Optional[InterviewAssessmentTemplateArgs] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewAssessmentTemplateBuilder":
        return InterviewAssessmentTemplateBuilder()


class InterviewAssessmentTemplateBuilder(object):
    def __init__(self) -> None:
        self._interview_assessment_template = InterviewAssessmentTemplate()

    def id(self, id: str) -> "InterviewAssessmentTemplateBuilder":
        self._interview_assessment_template.id = id
        return self

    def name(self, name: I18n) -> "InterviewAssessmentTemplateBuilder":
        self._interview_assessment_template.name = name
        return self

    def args(self, args: InterviewAssessmentTemplateArgs) -> "InterviewAssessmentTemplateBuilder":
        self._interview_assessment_template.args = args
        return self

    def build(self) -> "InterviewAssessmentTemplate":
        return self._interview_assessment_template
