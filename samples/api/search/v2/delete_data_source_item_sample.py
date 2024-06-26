# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.search.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteDataSourceItemRequest = DeleteDataSourceItemRequest.builder() \
        .data_source_id("service_ticket") \
        .item_id("01010111") \
        .build()

    # 发起请求
    response: DeleteDataSourceItemResponse = client.search.v2.data_source_item.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.search.v2.data_source_item.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: DeleteDataSourceItemRequest = DeleteDataSourceItemRequest.builder() \
        .data_source_id("service_ticket") \
        .item_id("01010111") \
        .build()

    # 发起请求
    response: DeleteDataSourceItemResponse = await client.search.v2.data_source_item.adelete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.search.v2.data_source_item.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
