# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: RemoveCustomFieldRequest = RemoveCustomFieldRequest.builder() \
        .custom_field_guid("0110a4bd-f24b-4a93-8c1a-1732b94f9593") \
        .request_body(RemoveCustomFieldRequestBody.builder()
                      .resource_type("tasklist")
                      .resource_id("0110a4bd-f24b-4a93-8c1a-1732b94f9593")
                      .build()) \
        .build()

    # 发起请求
    response: RemoveCustomFieldResponse = client.task.v2.custom_field.remove(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.custom_field.remove failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()