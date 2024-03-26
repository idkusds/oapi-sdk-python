# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_app_recommend_rule_response_body import ListAppRecommendRuleResponseBody


class ListAppRecommendRuleResponse(BaseResponse):
    _types = {
        "data": ListAppRecommendRuleResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAppRecommendRuleResponseBody] = None
        init(self, d, self._types)
