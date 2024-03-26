# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CareerInfo(object):
    _types = {
        "career_type": int,
        "company": str,
        "desc": str,
        "end_time": int,
        "start_time": int,
        "title": str,
    }

    def __init__(self, d=None):
        self.career_type: Optional[int] = None
        self.company: Optional[str] = None
        self.desc: Optional[str] = None
        self.end_time: Optional[int] = None
        self.start_time: Optional[int] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CareerInfoBuilder":
        return CareerInfoBuilder()


class CareerInfoBuilder(object):
    def __init__(self) -> None:
        self._career_info = CareerInfo()

    def career_type(self, career_type: int) -> "CareerInfoBuilder":
        self._career_info.career_type = career_type
        return self

    def company(self, company: str) -> "CareerInfoBuilder":
        self._career_info.company = company
        return self

    def desc(self, desc: str) -> "CareerInfoBuilder":
        self._career_info.desc = desc
        return self

    def end_time(self, end_time: int) -> "CareerInfoBuilder":
        self._career_info.end_time = end_time
        return self

    def start_time(self, start_time: int) -> "CareerInfoBuilder":
        self._career_info.start_time = start_time
        return self

    def title(self, title: str) -> "CareerInfoBuilder":
        self._career_info.title = title
        return self

    def build(self) -> "CareerInfo":
        return self._career_info
