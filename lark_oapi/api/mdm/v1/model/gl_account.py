# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_struct import I18nStruct


class GlAccount(object):
    _types = {
        "gl_account_uid": str,
        "gl_account": str,
        "gl_account_name": str,
        "i18n_gl_account_name": List[I18nStruct],
        "type": str,
        "valid_to": str,
    }

    def __init__(self, d=None):
        self.gl_account_uid: Optional[str] = None
        self.gl_account: Optional[str] = None
        self.gl_account_name: Optional[str] = None
        self.i18n_gl_account_name: Optional[List[I18nStruct]] = None
        self.type: Optional[str] = None
        self.valid_to: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GlAccountBuilder":
        return GlAccountBuilder()


class GlAccountBuilder(object):
    def __init__(self) -> None:
        self._gl_account = GlAccount()

    def gl_account_uid(self, gl_account_uid: str) -> "GlAccountBuilder":
        self._gl_account.gl_account_uid = gl_account_uid
        return self

    def gl_account(self, gl_account: str) -> "GlAccountBuilder":
        self._gl_account.gl_account = gl_account
        return self

    def gl_account_name(self, gl_account_name: str) -> "GlAccountBuilder":
        self._gl_account.gl_account_name = gl_account_name
        return self

    def i18n_gl_account_name(self, i18n_gl_account_name: List[I18nStruct]) -> "GlAccountBuilder":
        self._gl_account.i18n_gl_account_name = i18n_gl_account_name
        return self

    def type(self, type: str) -> "GlAccountBuilder":
        self._gl_account.type = type
        return self

    def valid_to(self, valid_to: str) -> "GlAccountBuilder":
        self._gl_account.valid_to = valid_to
        return self

    def build(self) -> "GlAccount":
        return self._gl_account
