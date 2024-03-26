# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .website_delivery_attachment_indentification import WebsiteDeliveryAttachmentIndentification


class WebsiteDeliveryAttachment(object):
    _types = {
        "job_post_id": str,
        "user_id": str,
        "resume_file_id": str,
        "channel_id": str,
        "application_preferred_city_code_list": List[str],
        "mobile_country_code": str,
        "mobile": str,
        "email": str,
        "identification": WebsiteDeliveryAttachmentIndentification,
    }

    def __init__(self, d=None):
        self.job_post_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.resume_file_id: Optional[str] = None
        self.channel_id: Optional[str] = None
        self.application_preferred_city_code_list: Optional[List[str]] = None
        self.mobile_country_code: Optional[str] = None
        self.mobile: Optional[str] = None
        self.email: Optional[str] = None
        self.identification: Optional[WebsiteDeliveryAttachmentIndentification] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryAttachmentBuilder":
        return WebsiteDeliveryAttachmentBuilder()


class WebsiteDeliveryAttachmentBuilder(object):
    def __init__(self) -> None:
        self._website_delivery_attachment = WebsiteDeliveryAttachment()

    def job_post_id(self, job_post_id: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.job_post_id = job_post_id
        return self

    def user_id(self, user_id: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.user_id = user_id
        return self

    def resume_file_id(self, resume_file_id: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.resume_file_id = resume_file_id
        return self

    def channel_id(self, channel_id: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.channel_id = channel_id
        return self

    def application_preferred_city_code_list(self, application_preferred_city_code_list: List[
        str]) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.application_preferred_city_code_list = application_preferred_city_code_list
        return self

    def mobile_country_code(self, mobile_country_code: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.mobile_country_code = mobile_country_code
        return self

    def mobile(self, mobile: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.mobile = mobile
        return self

    def email(self, email: str) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.email = email
        return self

    def identification(self,
                       identification: WebsiteDeliveryAttachmentIndentification) -> "WebsiteDeliveryAttachmentBuilder":
        self._website_delivery_attachment.identification = identification
        return self

    def build(self) -> "WebsiteDeliveryAttachment":
        return self._website_delivery_attachment
