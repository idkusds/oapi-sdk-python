# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .mobile import Mobile


class CreateReferralAccountRequestBody(object):
    _types = {
        "mobile": Mobile,
        "email": str,
    }

    def __init__(self, d=None):
        self.mobile: Optional[Mobile] = None
        self.email: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateReferralAccountRequestBodyBuilder":
        return CreateReferralAccountRequestBodyBuilder()


class CreateReferralAccountRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_referral_account_request_body = CreateReferralAccountRequestBody()

    def mobile(self, mobile: Mobile) -> "CreateReferralAccountRequestBodyBuilder":
        self._create_referral_account_request_body.mobile = mobile
        return self

    def email(self, email: str) -> "CreateReferralAccountRequestBodyBuilder":
        self._create_referral_account_request_body.email = email
        return self

    def build(self) -> "CreateReferralAccountRequestBody":
        return self._create_referral_account_request_body
