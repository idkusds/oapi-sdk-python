# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AigcConfig(object):
    _types = {
        "need_review": bool,
        "repo_id": int,
    }

    def __init__(self, d=None):
        self.need_review: Optional[bool] = None
        self.repo_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AigcConfigBuilder":
        return AigcConfigBuilder()


class AigcConfigBuilder(object):
    def __init__(self) -> None:
        self._aigc_config = AigcConfig()

    def need_review(self, need_review: bool) -> "AigcConfigBuilder":
        self._aigc_config.need_review = need_review
        return self

    def repo_id(self, repo_id: int) -> "AigcConfigBuilder":
        self._aigc_config.repo_id = repo_id
        return self

    def build(self) -> "AigcConfig":
        return self._aigc_config
