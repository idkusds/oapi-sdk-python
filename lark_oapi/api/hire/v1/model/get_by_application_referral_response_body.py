# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .referral import Referral


class GetByApplicationReferralResponseBody(object):
    _types = {
        "referral": Referral,
    }

    def __init__(self, d=None):
        self.referral: Optional[Referral] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetByApplicationReferralResponseBodyBuilder":
        return GetByApplicationReferralResponseBodyBuilder()


class GetByApplicationReferralResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_by_application_referral_response_body = GetByApplicationReferralResponseBody()

    def referral(self, referral: Referral) -> "GetByApplicationReferralResponseBodyBuilder":
        self._get_by_application_referral_response_body.referral = referral
        return self

    def build(self) -> "GetByApplicationReferralResponseBody":
        return self._get_by_application_referral_response_body
