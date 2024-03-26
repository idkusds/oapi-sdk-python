# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class StartServiceTicketResponseBody(object):
    _types = {
        "chat_id": str,
    }

    def __init__(self, d=None):
        self.chat_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StartServiceTicketResponseBodyBuilder":
        return StartServiceTicketResponseBodyBuilder()


class StartServiceTicketResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._start_service_ticket_response_body = StartServiceTicketResponseBody()

    def chat_id(self, chat_id: str) -> "StartServiceTicketResponseBodyBuilder":
        self._start_service_ticket_response_body.chat_id = chat_id
        return self

    def build(self) -> "StartServiceTicketResponseBody":
        return self._start_service_ticket_response_body
