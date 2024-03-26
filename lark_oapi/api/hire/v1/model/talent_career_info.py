# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentCareerInfo(object):
    _types = {
        "id": str,
        "company": str,
        "title": str,
        "desc": str,
        "start_time": str,
        "end_time": str,
        "career_type": int,
        "tag_list": List[int],
        "customized_data_list": List[TalentCustomizedDataChild],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.company: Optional[str] = None
        self.title: Optional[str] = None
        self.desc: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.career_type: Optional[int] = None
        self.tag_list: Optional[List[int]] = None
        self.customized_data_list: Optional[List[TalentCustomizedDataChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCareerInfoBuilder":
        return TalentCareerInfoBuilder()


class TalentCareerInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_career_info = TalentCareerInfo()

    def id(self, id: str) -> "TalentCareerInfoBuilder":
        self._talent_career_info.id = id
        return self

    def company(self, company: str) -> "TalentCareerInfoBuilder":
        self._talent_career_info.company = company
        return self

    def title(self, title: str) -> "TalentCareerInfoBuilder":
        self._talent_career_info.title = title
        return self

    def desc(self, desc: str) -> "TalentCareerInfoBuilder":
        self._talent_career_info.desc = desc
        return self

    def start_time(self, start_time: str) -> "TalentCareerInfoBuilder":
        self._talent_career_info.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TalentCareerInfoBuilder":
        self._talent_career_info.end_time = end_time
        return self

    def career_type(self, career_type: int) -> "TalentCareerInfoBuilder":
        self._talent_career_info.career_type = career_type
        return self

    def tag_list(self, tag_list: List[int]) -> "TalentCareerInfoBuilder":
        self._talent_career_info.tag_list = tag_list
        return self

    def customized_data_list(self, customized_data_list: List[TalentCustomizedDataChild]) -> "TalentCareerInfoBuilder":
        self._talent_career_info.customized_data_list = customized_data_list
        return self

    def build(self) -> "TalentCareerInfo":
        return self._talent_career_info
