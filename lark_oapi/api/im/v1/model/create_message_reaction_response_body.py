# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .operator import Operator
from .emoji import Emoji


class CreateMessageReactionResponseBody(object):
    _types = {
        "reaction_id": str,
        "operator": Operator,
        "action_time": int,
        "reaction_type": Emoji,
    }

    def __init__(self, d=None):
        self.reaction_id: Optional[str] = None
        self.operator: Optional[Operator] = None
        self.action_time: Optional[int] = None
        self.reaction_type: Optional[Emoji] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMessageReactionResponseBodyBuilder":
        return CreateMessageReactionResponseBodyBuilder()


class CreateMessageReactionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_message_reaction_response_body = CreateMessageReactionResponseBody()

    def reaction_id(self, reaction_id: str) -> "CreateMessageReactionResponseBodyBuilder":
        self._create_message_reaction_response_body.reaction_id = reaction_id
        return self

    def operator(self, operator: Operator) -> "CreateMessageReactionResponseBodyBuilder":
        self._create_message_reaction_response_body.operator = operator
        return self

    def action_time(self, action_time: int) -> "CreateMessageReactionResponseBodyBuilder":
        self._create_message_reaction_response_body.action_time = action_time
        return self

    def reaction_type(self, reaction_type: Emoji) -> "CreateMessageReactionResponseBodyBuilder":
        self._create_message_reaction_response_body.reaction_type = reaction_type
        return self

    def build(self) -> "CreateMessageReactionResponseBody":
        return self._create_message_reaction_response_body
