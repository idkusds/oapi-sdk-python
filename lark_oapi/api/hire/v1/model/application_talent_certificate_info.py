# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ApplicationTalentCertificateInfo(object):
    _types = {
        "id": str,
        "name": str,
        "desc": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.desc: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationTalentCertificateInfoBuilder":
        return ApplicationTalentCertificateInfoBuilder()


class ApplicationTalentCertificateInfoBuilder(object):
    def __init__(self) -> None:
        self._application_talent_certificate_info = ApplicationTalentCertificateInfo()

    def id(self, id: str) -> "ApplicationTalentCertificateInfoBuilder":
        self._application_talent_certificate_info.id = id
        return self

    def name(self, name: str) -> "ApplicationTalentCertificateInfoBuilder":
        self._application_talent_certificate_info.name = name
        return self

    def desc(self, desc: str) -> "ApplicationTalentCertificateInfoBuilder":
        self._application_talent_certificate_info.desc = desc
        return self

    def build(self) -> "ApplicationTalentCertificateInfo":
        return self._application_talent_certificate_info
