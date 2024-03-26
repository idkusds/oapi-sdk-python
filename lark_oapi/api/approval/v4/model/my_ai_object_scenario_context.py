# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .object_context import ObjectContext


class MyAiObjectScenarioContext(object):
    _types = {
        "object": ObjectContext,
    }

    def __init__(self, d=None):
        self.object: Optional[ObjectContext] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiObjectScenarioContextBuilder":
        return MyAiObjectScenarioContextBuilder()


class MyAiObjectScenarioContextBuilder(object):
    def __init__(self) -> None:
        self._my_ai_object_scenario_context = MyAiObjectScenarioContext()

    def object(self, object: ObjectContext) -> "MyAiObjectScenarioContextBuilder":
        self._my_ai_object_scenario_context.object = object
        return self

    def build(self) -> "MyAiObjectScenarioContext":
        return self._my_ai_object_scenario_context
