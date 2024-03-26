# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .patch_agent_skill_request_body import PatchAgentSkillRequestBody


class PatchAgentSkillRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.agent_skill_id: Optional[str] = None
        self.request_body: Optional[PatchAgentSkillRequestBody] = None

    @staticmethod
    def builder() -> "PatchAgentSkillRequestBuilder":
        return PatchAgentSkillRequestBuilder()


class PatchAgentSkillRequestBuilder(object):

    def __init__(self) -> None:
        patch_agent_skill_request = PatchAgentSkillRequest()
        patch_agent_skill_request.http_method = HttpMethod.PATCH
        patch_agent_skill_request.uri = "/open-apis/helpdesk/v1/agent_skills/:agent_skill_id"
        patch_agent_skill_request.token_types = {AccessTokenType.USER}
        self._patch_agent_skill_request: PatchAgentSkillRequest = patch_agent_skill_request

    def agent_skill_id(self, agent_skill_id: str) -> "PatchAgentSkillRequestBuilder":
        self._patch_agent_skill_request.agent_skill_id = agent_skill_id
        self._patch_agent_skill_request.paths["agent_skill_id"] = str(agent_skill_id)
        return self

    def request_body(self, request_body: PatchAgentSkillRequestBody) -> "PatchAgentSkillRequestBuilder":
        self._patch_agent_skill_request.request_body = request_body
        self._patch_agent_skill_request.body = request_body
        return self

    def build(self) -> PatchAgentSkillRequest:
        return self._patch_agent_skill_request
