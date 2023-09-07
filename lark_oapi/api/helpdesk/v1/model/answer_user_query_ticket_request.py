# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .answer_user_query_ticket_request_body import AnswerUserQueryTicketRequestBody


class AnswerUserQueryTicketRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_id: Optional[str] = None
        self.request_body: Optional[AnswerUserQueryTicketRequestBody] = None

    @staticmethod
    def builder() -> "AnswerUserQueryTicketRequestBuilder":
        return AnswerUserQueryTicketRequestBuilder()


class AnswerUserQueryTicketRequestBuilder(object):

    def __init__(self) -> None:
        answer_user_query_ticket_request = AnswerUserQueryTicketRequest()
        answer_user_query_ticket_request.http_method = HttpMethod.POST
        answer_user_query_ticket_request.uri = "/open-apis/helpdesk/v1/tickets/:ticket_id/answer_user_query"
        answer_user_query_ticket_request.token_types = {AccessTokenType.TENANT}
        self._answer_user_query_ticket_request: AnswerUserQueryTicketRequest = answer_user_query_ticket_request

    def ticket_id(self, ticket_id: str) -> "AnswerUserQueryTicketRequestBuilder":
        self._answer_user_query_ticket_request.ticket_id = ticket_id
        self._answer_user_query_ticket_request.paths["ticket_id"] = str(ticket_id)
        return self

    def request_body(self, request_body: AnswerUserQueryTicketRequestBody) -> "AnswerUserQueryTicketRequestBuilder":
        self._answer_user_query_ticket_request.request_body = request_body
        self._answer_user_query_ticket_request.body = request_body
        return self

    def build(self) -> AnswerUserQueryTicketRequest:
        return self._answer_user_query_ticket_request
