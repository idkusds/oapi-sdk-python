# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteBatchMessageRequest = DeleteBatchMessageRequest.builder() \
        .batch_message_id("bm-dc13264520392913993dd051dba21dcf") \
        .build()

    # 发起请求
    response: DeleteBatchMessageResponse = client.im.v1.batch_message.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.batch_message.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: DeleteBatchMessageRequest = DeleteBatchMessageRequest.builder() \
        .batch_message_id("bm-dc13264520392913993dd051dba21dcf") \
        .build()

    # 发起请求
    response: DeleteBatchMessageResponse = await client.im.v1.batch_message.adelete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.batch_message.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
