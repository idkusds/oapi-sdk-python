# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class Follower(object):
    _types = {
        "id": str,
        "id_list": List[str],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FollowerBuilder":
        return FollowerBuilder()


class FollowerBuilder(object):
    def __init__(self) -> None:
        self._follower = Follower()

    def id(self, id: str) -> "FollowerBuilder":
        self._follower.id = id
        return self

    def id_list(self, id_list: List[str]) -> "FollowerBuilder":
        self._follower.id_list = id_list
        return self

    def build(self) -> "Follower":
        return self._follower
