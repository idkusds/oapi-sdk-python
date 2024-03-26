# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Dummy(object):
    _types = {
        "foo": str,
    }

    def __init__(self, d=None):
        self.foo: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DummyBuilder":
        return DummyBuilder()


class DummyBuilder(object):
    def __init__(self) -> None:
        self._dummy = Dummy()

    def foo(self, foo: str) -> "DummyBuilder":
        self._dummy.foo = foo
        return self

    def build(self) -> "Dummy":
        return self._dummy
