# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_names import I18nNames


class Chat(object):
    _types = {
        "chat_id": str,
        "avatar": str,
        "name": str,
        "description": str,
        "i18n_names": I18nNames,
        "only_owner_add": bool,
        "share_allowed": bool,
        "only_owner_at_all": bool,
        "only_owner_edit": bool,
        "owner_user_id": str,
        "type": str,
    }

    def __init__(self, d=None):
        self.chat_id: Optional[str] = None
        self.avatar: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        self.only_owner_add: Optional[bool] = None
        self.share_allowed: Optional[bool] = None
        self.only_owner_at_all: Optional[bool] = None
        self.only_owner_edit: Optional[bool] = None
        self.owner_user_id: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatBuilder":
        return ChatBuilder()


class ChatBuilder(object):
    def __init__(self) -> None:
        self._chat = Chat()

    def chat_id(self, chat_id: str) -> "ChatBuilder":
        self._chat.chat_id = chat_id
        return self

    def avatar(self, avatar: str) -> "ChatBuilder":
        self._chat.avatar = avatar
        return self

    def name(self, name: str) -> "ChatBuilder":
        self._chat.name = name
        return self

    def description(self, description: str) -> "ChatBuilder":
        self._chat.description = description
        return self

    def i18n_names(self, i18n_names: I18nNames) -> "ChatBuilder":
        self._chat.i18n_names = i18n_names
        return self

    def only_owner_add(self, only_owner_add: bool) -> "ChatBuilder":
        self._chat.only_owner_add = only_owner_add
        return self

    def share_allowed(self, share_allowed: bool) -> "ChatBuilder":
        self._chat.share_allowed = share_allowed
        return self

    def only_owner_at_all(self, only_owner_at_all: bool) -> "ChatBuilder":
        self._chat.only_owner_at_all = only_owner_at_all
        return self

    def only_owner_edit(self, only_owner_edit: bool) -> "ChatBuilder":
        self._chat.only_owner_edit = only_owner_edit
        return self

    def owner_user_id(self, owner_user_id: str) -> "ChatBuilder":
        self._chat.owner_user_id = owner_user_id
        return self

    def type(self, type: str) -> "ChatBuilder":
        self._chat.type = type
        return self

    def build(self) -> "Chat":
        return self._chat
