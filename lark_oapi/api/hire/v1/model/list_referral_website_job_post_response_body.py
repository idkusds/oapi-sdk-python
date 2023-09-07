# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .portal_job_post import PortalJobPost


class ListReferralWebsiteJobPostResponseBody(object):
    _types = {
        "items": List[PortalJobPost],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[PortalJobPost]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListReferralWebsiteJobPostResponseBodyBuilder":
        return ListReferralWebsiteJobPostResponseBodyBuilder()


class ListReferralWebsiteJobPostResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_referral_website_job_post_response_body = ListReferralWebsiteJobPostResponseBody()

    def items(self, items: List[PortalJobPost]) -> "ListReferralWebsiteJobPostResponseBodyBuilder":
        self._list_referral_website_job_post_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListReferralWebsiteJobPostResponseBodyBuilder":
        self._list_referral_website_job_post_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListReferralWebsiteJobPostResponseBodyBuilder":
        self._list_referral_website_job_post_response_body.page_token = page_token
        return self

    def build(self) -> "ListReferralWebsiteJobPostResponseBody":
        return self._list_referral_website_job_post_response_body
