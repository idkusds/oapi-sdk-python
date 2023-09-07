# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class TalentIdentificationInfo(object):
    _types = {
        "identification_type": int,
        "identification_number": str,
    }

    def __init__(self, d=None):
        self.identification_type: Optional[int] = None
        self.identification_number: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentIdentificationInfoBuilder":
        return TalentIdentificationInfoBuilder()


class TalentIdentificationInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_identification_info = TalentIdentificationInfo()

    def identification_type(self, identification_type: int) -> "TalentIdentificationInfoBuilder":
        self._talent_identification_info.identification_type = identification_type
        return self

    def identification_number(self, identification_number: str) -> "TalentIdentificationInfoBuilder":
        self._talent_identification_info.identification_number = identification_number
        return self

    def build(self) -> "TalentIdentificationInfo":
        return self._talent_identification_info
