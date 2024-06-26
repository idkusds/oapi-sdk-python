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
    request: PatchCustomFieldRequest = PatchCustomFieldRequest.builder() \
        .custom_field_guid("5ffbe0ca-6600-41e0-a634-2b38cbcf13b8") \
        .user_id_type("open_id") \
        .request_body(PatchCustomFieldRequestBody.builder()
                      .custom_field(InputCustomField.builder().build())
                      .update_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchCustomFieldResponse = client.task.v2.custom_field.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.custom_field.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PatchCustomFieldRequest = PatchCustomFieldRequest.builder() \
        .custom_field_guid("5ffbe0ca-6600-41e0-a634-2b38cbcf13b8") \
        .user_id_type("open_id") \
        .request_body(PatchCustomFieldRequestBody.builder()
                      .custom_field(InputCustomField.builder().build())
                      .update_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchCustomFieldResponse = await client.task.v2.custom_field.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.custom_field.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
