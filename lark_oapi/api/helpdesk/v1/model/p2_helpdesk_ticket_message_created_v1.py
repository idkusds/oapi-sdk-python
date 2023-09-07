# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .ticket import Ticket
from .ticket_message_content import TicketMessageContent
from .user_id import UserId


class P2HelpdeskTicketMessageCreatedV1Data(object):
    _types = {
        "ticket_message_id": str,
        "message_id": str,
        "msg_type": str,
        "position": str,
        "sender_id": UserId,
        "sender_type": int,
        "text": str,
        "ticket": Ticket,
        "event_id": str,
        "chat_id": str,
        "content": TicketMessageContent,
    }

    def __init__(self, d=None):
        self.ticket_message_id: Optional[str] = None
        self.message_id: Optional[str] = None
        self.msg_type: Optional[str] = None
        self.position: Optional[str] = None
        self.sender_id: Optional[UserId] = None
        self.sender_type: Optional[int] = None
        self.text: Optional[str] = None
        self.ticket: Optional[Ticket] = None
        self.event_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.content: Optional[TicketMessageContent] = None
        init(self, d, self._types)


class P2HelpdeskTicketMessageCreatedV1(EventContext):
    _types = {
        "event": P2HelpdeskTicketMessageCreatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2HelpdeskTicketMessageCreatedV1Data] = None
        init(self, d, self._types)
