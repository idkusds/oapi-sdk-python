# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId
from .i18n_names import I18nNames


class P2ImChatDisbandedV1Data(object):
    _types = {
        "chat_id": str,
        "operator_id": UserId,
        "external": bool,
        "operator_tenant_key": str,
        "name": str,
        "i18n_names": I18nNames,
    }

    def __init__(self, d=None):
        self.chat_id: Optional[str] = None
        self.operator_id: Optional[UserId] = None
        self.external: Optional[bool] = None
        self.operator_tenant_key: Optional[str] = None
        self.name: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        init(self, d, self._types)


class P2ImChatDisbandedV1(EventContext):
    _types = {
        "event": P2ImChatDisbandedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ImChatDisbandedV1Data] = None
        init(self, d, self._types)
