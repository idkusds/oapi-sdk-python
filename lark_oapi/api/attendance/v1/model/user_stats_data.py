# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_stats_data_cell import UserStatsDataCell


class UserStatsData(object):
    _types = {
        "name": str,
        "user_id": str,
        "datas": List[UserStatsDataCell],
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.user_id: Optional[str] = None
        self.datas: Optional[List[UserStatsDataCell]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserStatsDataBuilder":
        return UserStatsDataBuilder()


class UserStatsDataBuilder(object):
    def __init__(self) -> None:
        self._user_stats_data = UserStatsData()

    def name(self, name: str) -> "UserStatsDataBuilder":
        self._user_stats_data.name = name
        return self

    def user_id(self, user_id: str) -> "UserStatsDataBuilder":
        self._user_stats_data.user_id = user_id
        return self

    def datas(self, datas: List[UserStatsDataCell]) -> "UserStatsDataBuilder":
        self._user_stats_data.datas = datas
        return self

    def build(self) -> "UserStatsData":
        return self._user_stats_data
