# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .id_name_object import IdNameObject


class Subject(object):
    _types = {
        "id": str,
        "name": I18n,
        "create_time": str,
        "active_status": int,
        "application_limit": int,
        "creator": IdNameObject,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.create_time: Optional[str] = None
        self.active_status: Optional[int] = None
        self.application_limit: Optional[int] = None
        self.creator: Optional[IdNameObject] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubjectBuilder":
        return SubjectBuilder()


class SubjectBuilder(object):
    def __init__(self) -> None:
        self._subject = Subject()

    def id(self, id: str) -> "SubjectBuilder":
        self._subject.id = id
        return self

    def name(self, name: I18n) -> "SubjectBuilder":
        self._subject.name = name
        return self

    def create_time(self, create_time: str) -> "SubjectBuilder":
        self._subject.create_time = create_time
        return self

    def active_status(self, active_status: int) -> "SubjectBuilder":
        self._subject.active_status = active_status
        return self

    def application_limit(self, application_limit: int) -> "SubjectBuilder":
        self._subject.application_limit = application_limit
        return self

    def creator(self, creator: IdNameObject) -> "SubjectBuilder":
        self._subject.creator = creator
        return self

    def build(self) -> "Subject":
        return self._subject
