# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BaseDistrict(object):
    _types = {
        "zh_name": str,
        "en_name": str,
        "code": str,
        "location_type": int,
    }

    def __init__(self, d=None):
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.code: Optional[str] = None
        self.location_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BaseDistrictBuilder":
        return BaseDistrictBuilder()


class BaseDistrictBuilder(object):
    def __init__(self) -> None:
        self._base_district = BaseDistrict()

    def zh_name(self, zh_name: str) -> "BaseDistrictBuilder":
        self._base_district.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "BaseDistrictBuilder":
        self._base_district.en_name = en_name
        return self

    def code(self, code: str) -> "BaseDistrictBuilder":
        self._base_district.code = code
        return self

    def location_type(self, location_type: int) -> "BaseDistrictBuilder":
        self._base_district.location_type = location_type
        return self

    def build(self) -> "BaseDistrict":
        return self._base_district
