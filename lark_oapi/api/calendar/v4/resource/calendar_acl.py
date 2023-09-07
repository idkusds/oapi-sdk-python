# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_calendar_acl_request import CreateCalendarAclRequest
from ..model.create_calendar_acl_response import CreateCalendarAclResponse
from ..model.delete_calendar_acl_request import DeleteCalendarAclRequest
from ..model.delete_calendar_acl_response import DeleteCalendarAclResponse
from ..model.list_calendar_acl_request import ListCalendarAclRequest
from ..model.list_calendar_acl_response import ListCalendarAclResponse
from ..model.subscription_calendar_acl_request import SubscriptionCalendarAclRequest
from ..model.subscription_calendar_acl_response import SubscriptionCalendarAclResponse
from ..model.unsubscription_calendar_acl_request import UnsubscriptionCalendarAclRequest
from ..model.unsubscription_calendar_acl_response import UnsubscriptionCalendarAclResponse


class CalendarAcl(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateCalendarAclRequest,
               option: Optional[RequestOption] = None) -> CreateCalendarAclResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateCalendarAclResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateCalendarAclResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteCalendarAclRequest,
               option: Optional[RequestOption] = None) -> DeleteCalendarAclResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteCalendarAclResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteCalendarAclResponse)
        response.raw = resp

        return response

    def list(self, request: ListCalendarAclRequest, option: Optional[RequestOption] = None) -> ListCalendarAclResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListCalendarAclResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCalendarAclResponse)
        response.raw = resp

        return response

    def subscription(self, request: SubscriptionCalendarAclRequest,
                     option: Optional[RequestOption] = None) -> SubscriptionCalendarAclResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SubscriptionCalendarAclResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   SubscriptionCalendarAclResponse)
        response.raw = resp

        return response

    def unsubscription(self, request: UnsubscriptionCalendarAclRequest,
                       option: Optional[RequestOption] = None) -> UnsubscriptionCalendarAclResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UnsubscriptionCalendarAclResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     UnsubscriptionCalendarAclResponse)
        response.raw = resp

        return response
