# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteRuleExternalRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.rule_id: Optional[int] = None

    @staticmethod
    def builder() -> "DeleteRuleExternalRequestBuilder":
        return DeleteRuleExternalRequestBuilder()


class DeleteRuleExternalRequestBuilder(object):

    def __init__(self) -> None:
        delete_rule_external_request = DeleteRuleExternalRequest()
        delete_rule_external_request.http_method = HttpMethod.DELETE
        delete_rule_external_request.uri = "/open-apis/acs/v1/rule_external"
        delete_rule_external_request.token_types = {AccessTokenType.USER}
        self._delete_rule_external_request: DeleteRuleExternalRequest = delete_rule_external_request

    def rule_id(self, rule_id: int) -> "DeleteRuleExternalRequestBuilder":
        self._delete_rule_external_request.rule_id = rule_id
        self._delete_rule_external_request.add_query("rule_id", rule_id)
        return self

    def build(self) -> DeleteRuleExternalRequest:
        return self._delete_rule_external_request
