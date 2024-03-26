# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .offer_apply_form_pre_object_config_info import OfferApplyFormPreObjectConfigInfo


class OfferApplyFormObjectDisplayConfigInfo(object):
    _types = {
        "display_condition": int,
        "pre_object_config_list": List[OfferApplyFormPreObjectConfigInfo],
    }

    def __init__(self, d=None):
        self.display_condition: Optional[int] = None
        self.pre_object_config_list: Optional[List[OfferApplyFormPreObjectConfigInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormObjectDisplayConfigInfoBuilder":
        return OfferApplyFormObjectDisplayConfigInfoBuilder()


class OfferApplyFormObjectDisplayConfigInfoBuilder(object):
    def __init__(self) -> None:
        self._offer_apply_form_object_display_config_info = OfferApplyFormObjectDisplayConfigInfo()

    def display_condition(self, display_condition: int) -> "OfferApplyFormObjectDisplayConfigInfoBuilder":
        self._offer_apply_form_object_display_config_info.display_condition = display_condition
        return self

    def pre_object_config_list(self, pre_object_config_list: List[
        OfferApplyFormPreObjectConfigInfo]) -> "OfferApplyFormObjectDisplayConfigInfoBuilder":
        self._offer_apply_form_object_display_config_info.pre_object_config_list = pre_object_config_list
        return self

    def build(self) -> "OfferApplyFormObjectDisplayConfigInfo":
        return self._offer_apply_form_object_display_config_info
