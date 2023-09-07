# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .background_check_custom_field_data_value import BackgroundCheckCustomFieldDataValue
from .background_check_item_info import BackgroundCheckItemInfo
from .background_check_order_creator import BackgroundCheckOrderCreator
from .background_check_order_feedback_info import BackgroundCheckOrderFeedbackInfo
from .background_check_order_process_info import BackgroundCheckOrderProcessInfo
from .eco_background_check_custom_field_data import EcoBackgroundCheckCustomFieldData
from .id_name_object import IdNameObject
from .user_contact_info import UserContactInfo


class BackgroundCheckOrder(object):
    _types = {
        "order_id": str,
        "application_id": str,
        "order_status": int,
        "account_third_type": int,
        "package": str,
        "name": str,
        "feedback_info_list": List[BackgroundCheckOrderFeedbackInfo],
        "process_info_list": List[BackgroundCheckOrderProcessInfo],
        "upload_time": str,
        "candidate_info": UserContactInfo,
        "creator_info": BackgroundCheckOrderCreator,
        "contactor_info": UserContactInfo,
        "begin_time": str,
        "end_time": str,
        "conclusion": str,
        "provider_info": IdNameObject,
        "custom_field_list": List[EcoBackgroundCheckCustomFieldData],
        "custom_data_list": List[BackgroundCheckCustomFieldDataValue],
        "ext_item_info_list": List[BackgroundCheckItemInfo],
        "update_time": str,
        "geo": str,
        "location_code": str,
        "remark": str,
    }

    def __init__(self, d=None):
        self.order_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.order_status: Optional[int] = None
        self.account_third_type: Optional[int] = None
        self.package: Optional[str] = None
        self.name: Optional[str] = None
        self.feedback_info_list: Optional[List[BackgroundCheckOrderFeedbackInfo]] = None
        self.process_info_list: Optional[List[BackgroundCheckOrderProcessInfo]] = None
        self.upload_time: Optional[str] = None
        self.candidate_info: Optional[UserContactInfo] = None
        self.creator_info: Optional[BackgroundCheckOrderCreator] = None
        self.contactor_info: Optional[UserContactInfo] = None
        self.begin_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.conclusion: Optional[str] = None
        self.provider_info: Optional[IdNameObject] = None
        self.custom_field_list: Optional[List[EcoBackgroundCheckCustomFieldData]] = None
        self.custom_data_list: Optional[List[BackgroundCheckCustomFieldDataValue]] = None
        self.ext_item_info_list: Optional[List[BackgroundCheckItemInfo]] = None
        self.update_time: Optional[str] = None
        self.geo: Optional[str] = None
        self.location_code: Optional[str] = None
        self.remark: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckOrderBuilder":
        return BackgroundCheckOrderBuilder()


class BackgroundCheckOrderBuilder(object):
    def __init__(self) -> None:
        self._background_check_order = BackgroundCheckOrder()

    def order_id(self, order_id: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.order_id = order_id
        return self

    def application_id(self, application_id: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.application_id = application_id
        return self

    def order_status(self, order_status: int) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.order_status = order_status
        return self

    def account_third_type(self, account_third_type: int) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.account_third_type = account_third_type
        return self

    def package(self, package: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.package = package
        return self

    def name(self, name: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.name = name
        return self

    def feedback_info_list(self,
                           feedback_info_list: List[BackgroundCheckOrderFeedbackInfo]) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.feedback_info_list = feedback_info_list
        return self

    def process_info_list(self,
                          process_info_list: List[BackgroundCheckOrderProcessInfo]) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.process_info_list = process_info_list
        return self

    def upload_time(self, upload_time: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.upload_time = upload_time
        return self

    def candidate_info(self, candidate_info: UserContactInfo) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.candidate_info = candidate_info
        return self

    def creator_info(self, creator_info: BackgroundCheckOrderCreator) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.creator_info = creator_info
        return self

    def contactor_info(self, contactor_info: UserContactInfo) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.contactor_info = contactor_info
        return self

    def begin_time(self, begin_time: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.begin_time = begin_time
        return self

    def end_time(self, end_time: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.end_time = end_time
        return self

    def conclusion(self, conclusion: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.conclusion = conclusion
        return self

    def provider_info(self, provider_info: IdNameObject) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.provider_info = provider_info
        return self

    def custom_field_list(self,
                          custom_field_list: List[EcoBackgroundCheckCustomFieldData]) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.custom_field_list = custom_field_list
        return self

    def custom_data_list(self,
                         custom_data_list: List[BackgroundCheckCustomFieldDataValue]) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.custom_data_list = custom_data_list
        return self

    def ext_item_info_list(self, ext_item_info_list: List[BackgroundCheckItemInfo]) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.ext_item_info_list = ext_item_info_list
        return self

    def update_time(self, update_time: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.update_time = update_time
        return self

    def geo(self, geo: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.geo = geo
        return self

    def location_code(self, location_code: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.location_code = location_code
        return self

    def remark(self, remark: str) -> "BackgroundCheckOrderBuilder":
        self._background_check_order.remark = remark
        return self

    def build(self) -> "BackgroundCheckOrder":
        return self._background_check_order
