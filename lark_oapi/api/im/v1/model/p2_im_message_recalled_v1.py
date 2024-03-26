# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2ImMessageRecalledV1Data(object):
    _types = {
        "message_id": str,
        "chat_id": str,
        "recall_time": str,
        "recall_type": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.recall_time: Optional[str] = None
        self.recall_type: Optional[str] = None
        init(self, d, self._types)


class P2ImMessageRecalledV1(EventContext):
    _types = {
        "event": P2ImMessageRecalledV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ImMessageRecalledV1Data] = None
        init(self, d, self._types)
