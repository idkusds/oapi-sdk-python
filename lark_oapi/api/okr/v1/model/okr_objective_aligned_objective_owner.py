# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class OkrObjectiveAlignedObjectiveOwner(object):
    _types = {
        "open_id": str,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.open_id: Optional[str] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrObjectiveAlignedObjectiveOwnerBuilder":
        return OkrObjectiveAlignedObjectiveOwnerBuilder()


class OkrObjectiveAlignedObjectiveOwnerBuilder(object):
    def __init__(self) -> None:
        self._okr_objective_aligned_objective_owner = OkrObjectiveAlignedObjectiveOwner()

    def open_id(self, open_id: str) -> "OkrObjectiveAlignedObjectiveOwnerBuilder":
        self._okr_objective_aligned_objective_owner.open_id = open_id
        return self

    def user_id(self, user_id: str) -> "OkrObjectiveAlignedObjectiveOwnerBuilder":
        self._okr_objective_aligned_objective_owner.user_id = user_id
        return self

    def build(self) -> "OkrObjectiveAlignedObjectiveOwner":
        return self._okr_objective_aligned_objective_owner
