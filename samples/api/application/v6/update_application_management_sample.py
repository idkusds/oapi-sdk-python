# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.application.v6 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: UpdateApplicationManagementRequest = UpdateApplicationManagementRequest.builder() \
        .app_id("cli_a4517c8461f8100a") \
        .request_body(UpdateApplicationManagementRequestBody.builder()
                      .enable(True)
                      .build()) \
        .build()

    # 发起请求
    response: UpdateApplicationManagementResponse = client.application.v6.application_management.update(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application_management.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: UpdateApplicationManagementRequest = UpdateApplicationManagementRequest.builder() \
        .app_id("cli_a4517c8461f8100a") \
        .request_body(UpdateApplicationManagementRequestBody.builder()
                      .enable(True)
                      .build()) \
        .build()

    # 发起请求
    response: UpdateApplicationManagementResponse = await client.application.v6.application_management.aupdate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application_management.aupdate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
