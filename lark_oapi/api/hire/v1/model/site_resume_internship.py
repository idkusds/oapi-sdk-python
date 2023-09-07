# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class SiteResumeInternship(object):
    _types = {
        "company": str,
        "position": str,
        "description": str,
        "start_time": str,
        "end_time": str,
    }

    def __init__(self, d=None):
        self.company: Optional[str] = None
        self.position: Optional[str] = None
        self.description: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteResumeInternshipBuilder":
        return SiteResumeInternshipBuilder()


class SiteResumeInternshipBuilder(object):
    def __init__(self) -> None:
        self._site_resume_internship = SiteResumeInternship()

    def company(self, company: str) -> "SiteResumeInternshipBuilder":
        self._site_resume_internship.company = company
        return self

    def position(self, position: str) -> "SiteResumeInternshipBuilder":
        self._site_resume_internship.position = position
        return self

    def description(self, description: str) -> "SiteResumeInternshipBuilder":
        self._site_resume_internship.description = description
        return self

    def start_time(self, start_time: str) -> "SiteResumeInternshipBuilder":
        self._site_resume_internship.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "SiteResumeInternshipBuilder":
        self._site_resume_internship.end_time = end_time
        return self

    def build(self) -> "SiteResumeInternship":
        return self._site_resume_internship
