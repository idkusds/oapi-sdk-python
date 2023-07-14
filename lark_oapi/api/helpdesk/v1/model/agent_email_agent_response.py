# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .agent_email_agent_response_body import AgentEmailAgentResponseBody


class AgentEmailAgentResponse(BaseResponse):
    _types = {
        "data": AgentEmailAgentResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[AgentEmailAgentResponseBody] = None
        init(self, d, self._types)