# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .application_prehire_offer_basic import ApplicationPrehireOfferBasic
from .appli_offer_onboard_profile import AppliOfferOnboardProfile
from .application_offer_attachment import ApplicationOfferAttachment


class ApplicationPrehireOffer(object):
    _types = {
        "basic_info": ApplicationPrehireOfferBasic,
        "offer_onboard_profile": AppliOfferOnboardProfile,
        "attachment_list": List[ApplicationOfferAttachment],
    }

    def __init__(self, d):
        self.basic_info: Optional[ApplicationPrehireOfferBasic] = None
        self.offer_onboard_profile: Optional[AppliOfferOnboardProfile] = None
        self.attachment_list: Optional[List[ApplicationOfferAttachment]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationPrehireOfferBuilder":
        return ApplicationPrehireOfferBuilder()


class ApplicationPrehireOfferBuilder(object):
    def __init__(self, application_prehire_offer: ApplicationPrehireOffer = ApplicationPrehireOffer({})) -> None:
        self._application_prehire_offer: ApplicationPrehireOffer = application_prehire_offer
    
    def basic_info(self, basic_info: ApplicationPrehireOfferBasic) -> "ApplicationPrehireOfferBuilder":
        self._application_prehire_offer.basic_info = basic_info
        return self
    
    def offer_onboard_profile(self, offer_onboard_profile: AppliOfferOnboardProfile) -> "ApplicationPrehireOfferBuilder":
        self._application_prehire_offer.offer_onboard_profile = offer_onboard_profile
        return self
    
    def attachment_list(self, attachment_list: List[ApplicationOfferAttachment]) -> "ApplicationPrehireOfferBuilder":
        self._application_prehire_offer.attachment_list = attachment_list
        return self
    
    def build(self) -> "ApplicationPrehireOffer":
        return self._application_prehire_offer