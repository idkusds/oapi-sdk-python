# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .correct_pair import CorrectPair


class CorrectError(object):
    _types = {
        "type": int,
        "total": int,
        "correct_pairs": List[CorrectPair],
    }

    def __init__(self, d=None):
        self.type: Optional[int] = None
        self.total: Optional[int] = None
        self.correct_pairs: Optional[List[CorrectPair]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CorrectErrorBuilder":
        return CorrectErrorBuilder()


class CorrectErrorBuilder(object):
    def __init__(self) -> None:
        self._correct_error = CorrectError()

    def type(self, type: int) -> "CorrectErrorBuilder":
        self._correct_error.type = type
        return self

    def total(self, total: int) -> "CorrectErrorBuilder":
        self._correct_error.total = total
        return self

    def correct_pairs(self, correct_pairs: List[CorrectPair]) -> "CorrectErrorBuilder":
        self._correct_error.correct_pairs = correct_pairs
        return self

    def build(self) -> "CorrectError":
        return self._correct_error
