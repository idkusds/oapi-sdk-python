# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DataArchivingMessage(object):
    _types = {
        "seq_id": int,
        "limit": int,
    }

    def __init__(self, d=None):
        self.seq_id: Optional[int] = None
        self.limit: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DataArchivingMessageBuilder":
        return DataArchivingMessageBuilder()


class DataArchivingMessageBuilder(object):
    def __init__(self) -> None:
        self._data_archiving_message = DataArchivingMessage()

    def seq_id(self, seq_id: int) -> "DataArchivingMessageBuilder":
        self._data_archiving_message.seq_id = seq_id
        return self

    def limit(self, limit: int) -> "DataArchivingMessageBuilder":
        self._data_archiving_message.limit = limit
        return self

    def build(self) -> "DataArchivingMessage":
        return self._data_archiving_message
