# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .comments import Comments
from .customized_field_display_item import CustomizedFieldDisplayItem
from .i18n import I18n
from .ticket_user import TicketUser


class Ticket(object):
    _types = {
        "ticket_id": str,
        "helpdesk_id": str,
        "guest": TicketUser,
        "comments": Comments,
        "ticket_type": int,
        "status": int,
        "score": int,
        "created_at": int,
        "updated_at": int,
        "closed_at": int,
        "dissatisfaction_reason": I18n,
        "agents": List[TicketUser],
        "channel": int,
        "solve": int,
        "closed_by": TicketUser,
        "collaborators": List[TicketUser],
        "customized_fields": List[CustomizedFieldDisplayItem],
        "agent_service_duration": float,
        "agent_first_response_duration": int,
        "bot_service_duration": int,
        "agent_resolution_time": int,
        "actual_processing_time": int,
        "agent_entry_time": int,
        "agent_first_response_time": int,
        "agent_last_response_time": int,
        "agent_owner": TicketUser,
    }

    def __init__(self, d=None):
        self.ticket_id: Optional[str] = None
        self.helpdesk_id: Optional[str] = None
        self.guest: Optional[TicketUser] = None
        self.comments: Optional[Comments] = None
        self.ticket_type: Optional[int] = None
        self.status: Optional[int] = None
        self.score: Optional[int] = None
        self.created_at: Optional[int] = None
        self.updated_at: Optional[int] = None
        self.closed_at: Optional[int] = None
        self.dissatisfaction_reason: Optional[I18n] = None
        self.agents: Optional[List[TicketUser]] = None
        self.channel: Optional[int] = None
        self.solve: Optional[int] = None
        self.closed_by: Optional[TicketUser] = None
        self.collaborators: Optional[List[TicketUser]] = None
        self.customized_fields: Optional[List[CustomizedFieldDisplayItem]] = None
        self.agent_service_duration: Optional[float] = None
        self.agent_first_response_duration: Optional[int] = None
        self.bot_service_duration: Optional[int] = None
        self.agent_resolution_time: Optional[int] = None
        self.actual_processing_time: Optional[int] = None
        self.agent_entry_time: Optional[int] = None
        self.agent_first_response_time: Optional[int] = None
        self.agent_last_response_time: Optional[int] = None
        self.agent_owner: Optional[TicketUser] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TicketBuilder":
        return TicketBuilder()


class TicketBuilder(object):
    def __init__(self) -> None:
        self._ticket = Ticket()

    def ticket_id(self, ticket_id: str) -> "TicketBuilder":
        self._ticket.ticket_id = ticket_id
        return self

    def helpdesk_id(self, helpdesk_id: str) -> "TicketBuilder":
        self._ticket.helpdesk_id = helpdesk_id
        return self

    def guest(self, guest: TicketUser) -> "TicketBuilder":
        self._ticket.guest = guest
        return self

    def comments(self, comments: Comments) -> "TicketBuilder":
        self._ticket.comments = comments
        return self

    def ticket_type(self, ticket_type: int) -> "TicketBuilder":
        self._ticket.ticket_type = ticket_type
        return self

    def status(self, status: int) -> "TicketBuilder":
        self._ticket.status = status
        return self

    def score(self, score: int) -> "TicketBuilder":
        self._ticket.score = score
        return self

    def created_at(self, created_at: int) -> "TicketBuilder":
        self._ticket.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> "TicketBuilder":
        self._ticket.updated_at = updated_at
        return self

    def closed_at(self, closed_at: int) -> "TicketBuilder":
        self._ticket.closed_at = closed_at
        return self

    def dissatisfaction_reason(self, dissatisfaction_reason: I18n) -> "TicketBuilder":
        self._ticket.dissatisfaction_reason = dissatisfaction_reason
        return self

    def agents(self, agents: List[TicketUser]) -> "TicketBuilder":
        self._ticket.agents = agents
        return self

    def channel(self, channel: int) -> "TicketBuilder":
        self._ticket.channel = channel
        return self

    def solve(self, solve: int) -> "TicketBuilder":
        self._ticket.solve = solve
        return self

    def closed_by(self, closed_by: TicketUser) -> "TicketBuilder":
        self._ticket.closed_by = closed_by
        return self

    def collaborators(self, collaborators: List[TicketUser]) -> "TicketBuilder":
        self._ticket.collaborators = collaborators
        return self

    def customized_fields(self, customized_fields: List[CustomizedFieldDisplayItem]) -> "TicketBuilder":
        self._ticket.customized_fields = customized_fields
        return self

    def agent_service_duration(self, agent_service_duration: float) -> "TicketBuilder":
        self._ticket.agent_service_duration = agent_service_duration
        return self

    def agent_first_response_duration(self, agent_first_response_duration: int) -> "TicketBuilder":
        self._ticket.agent_first_response_duration = agent_first_response_duration
        return self

    def bot_service_duration(self, bot_service_duration: int) -> "TicketBuilder":
        self._ticket.bot_service_duration = bot_service_duration
        return self

    def agent_resolution_time(self, agent_resolution_time: int) -> "TicketBuilder":
        self._ticket.agent_resolution_time = agent_resolution_time
        return self

    def actual_processing_time(self, actual_processing_time: int) -> "TicketBuilder":
        self._ticket.actual_processing_time = actual_processing_time
        return self

    def agent_entry_time(self, agent_entry_time: int) -> "TicketBuilder":
        self._ticket.agent_entry_time = agent_entry_time
        return self

    def agent_first_response_time(self, agent_first_response_time: int) -> "TicketBuilder":
        self._ticket.agent_first_response_time = agent_first_response_time
        return self

    def agent_last_response_time(self, agent_last_response_time: int) -> "TicketBuilder":
        self._ticket.agent_last_response_time = agent_last_response_time
        return self

    def agent_owner(self, agent_owner: TicketUser) -> "TicketBuilder":
        self._ticket.agent_owner = agent_owner
        return self

    def build(self) -> "Ticket":
        return self._ticket
