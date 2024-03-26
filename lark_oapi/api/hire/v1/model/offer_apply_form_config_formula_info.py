# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .offer_apply_form_formula_extra_map_info import OfferApplyFormFormulaExtraMapInfo


class OfferApplyFormConfigFormulaInfo(object):
    _types = {
        "value": str,
        "result": int,
        "extra_map": List[OfferApplyFormFormulaExtraMapInfo],
    }

    def __init__(self, d=None):
        self.value: Optional[str] = None
        self.result: Optional[int] = None
        self.extra_map: Optional[List[OfferApplyFormFormulaExtraMapInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormConfigFormulaInfoBuilder":
        return OfferApplyFormConfigFormulaInfoBuilder()


class OfferApplyFormConfigFormulaInfoBuilder(object):
    def __init__(self) -> None:
        self._offer_apply_form_config_formula_info = OfferApplyFormConfigFormulaInfo()

    def value(self, value: str) -> "OfferApplyFormConfigFormulaInfoBuilder":
        self._offer_apply_form_config_formula_info.value = value
        return self

    def result(self, result: int) -> "OfferApplyFormConfigFormulaInfoBuilder":
        self._offer_apply_form_config_formula_info.result = result
        return self

    def extra_map(self, extra_map: List[OfferApplyFormFormulaExtraMapInfo]) -> "OfferApplyFormConfigFormulaInfoBuilder":
        self._offer_apply_form_config_formula_info.extra_map = extra_map
        return self

    def build(self) -> "OfferApplyFormConfigFormulaInfo":
        return self._offer_apply_form_config_formula_info
