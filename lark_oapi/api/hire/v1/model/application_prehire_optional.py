# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ApplicationPrehireOptional(object):
    _types = {
        "with_talent_basic": bool,
        "with_talent_extend": bool,
        "with_job": bool,
        "with_offer": bool,
    }

    def __init__(self, d=None):
        self.with_talent_basic: Optional[bool] = None
        self.with_talent_extend: Optional[bool] = None
        self.with_job: Optional[bool] = None
        self.with_offer: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationPrehireOptionalBuilder":
        return ApplicationPrehireOptionalBuilder()


class ApplicationPrehireOptionalBuilder(object):
    def __init__(self) -> None:
        self._application_prehire_optional = ApplicationPrehireOptional()

    def with_talent_basic(self, with_talent_basic: bool) -> "ApplicationPrehireOptionalBuilder":
        self._application_prehire_optional.with_talent_basic = with_talent_basic
        return self

    def with_talent_extend(self, with_talent_extend: bool) -> "ApplicationPrehireOptionalBuilder":
        self._application_prehire_optional.with_talent_extend = with_talent_extend
        return self

    def with_job(self, with_job: bool) -> "ApplicationPrehireOptionalBuilder":
        self._application_prehire_optional.with_job = with_job
        return self

    def with_offer(self, with_offer: bool) -> "ApplicationPrehireOptionalBuilder":
        self._application_prehire_optional.with_offer = with_offer
        return self

    def build(self) -> "ApplicationPrehireOptional":
        return self._application_prehire_optional
