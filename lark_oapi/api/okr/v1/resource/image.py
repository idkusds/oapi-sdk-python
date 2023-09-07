# Code generated by Lark OpenAPI.

from typing import Optional

from requests_toolbelt import MultipartEncoder

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.upload_image_request import UploadImageRequest
from ..model.upload_image_response import UploadImageResponse


class Image(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def upload(self, request: UploadImageRequest, option: Optional[RequestOption] = None) -> UploadImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 处理 form-data
        if request.body is not None:
            form_data = MultipartEncoder(Files.parse_form_data(request.body))
            option.headers[CONTENT_TYPE] = form_data.content_type
            request.body = form_data

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UploadImageResponse = JSON.unmarshal(str(resp.content, UTF_8), UploadImageResponse)
        response.raw = resp

        return response
