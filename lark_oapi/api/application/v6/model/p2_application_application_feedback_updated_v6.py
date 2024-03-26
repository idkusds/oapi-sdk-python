# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId


class P2ApplicationApplicationFeedbackUpdatedV6Data(object):
    _types = {
        "feedback_ids": List[str],
        "status": int,
        "app_id": str,
        "update_time": str,
        "operator_id": UserId,
    }

    def __init__(self, d=None):
        self.feedback_ids: Optional[List[str]] = None
        self.status: Optional[int] = None
        self.app_id: Optional[str] = None
        self.update_time: Optional[str] = None
        self.operator_id: Optional[UserId] = None
        init(self, d, self._types)


class P2ApplicationApplicationFeedbackUpdatedV6(EventContext):
    _types = {
        "event": P2ApplicationApplicationFeedbackUpdatedV6Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ApplicationApplicationFeedbackUpdatedV6Data] = None
        init(self, d, self._types)
