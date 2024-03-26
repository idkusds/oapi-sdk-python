# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .okr_objective_aligned_objective_owner import OkrObjectiveAlignedObjectiveOwner


class OkrObjectiveAlignedObjective(object):
    _types = {
        "id": int,
        "okr_id": int,
        "owner": OkrObjectiveAlignedObjectiveOwner,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.okr_id: Optional[int] = None
        self.owner: Optional[OkrObjectiveAlignedObjectiveOwner] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrObjectiveAlignedObjectiveBuilder":
        return OkrObjectiveAlignedObjectiveBuilder()


class OkrObjectiveAlignedObjectiveBuilder(object):
    def __init__(self) -> None:
        self._okr_objective_aligned_objective = OkrObjectiveAlignedObjective()

    def id(self, id: int) -> "OkrObjectiveAlignedObjectiveBuilder":
        self._okr_objective_aligned_objective.id = id
        return self

    def okr_id(self, okr_id: int) -> "OkrObjectiveAlignedObjectiveBuilder":
        self._okr_objective_aligned_objective.okr_id = okr_id
        return self

    def owner(self, owner: OkrObjectiveAlignedObjectiveOwner) -> "OkrObjectiveAlignedObjectiveBuilder":
        self._okr_objective_aligned_objective.owner = owner
        return self

    def build(self) -> "OkrObjectiveAlignedObjective":
        return self._okr_objective_aligned_objective
