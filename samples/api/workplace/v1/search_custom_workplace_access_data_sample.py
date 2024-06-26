# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.workplace.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: SearchCustomWorkplaceAccessDataRequest = SearchCustomWorkplaceAccessDataRequest.builder() \
        .from_date("2023-03-01") \
        .to_date("2023-03-22") \
        .page_size(20) \
        .page_token("ddowkdkl9w2d") \
        .custom_workplace_id("tpl_647184b585400013254c4ea6") \
        .build()

    # 发起请求
    response: SearchCustomWorkplaceAccessDataResponse = client.workplace.v1.custom_workplace_access_data.search(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.workplace.v1.custom_workplace_access_data.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: SearchCustomWorkplaceAccessDataRequest = SearchCustomWorkplaceAccessDataRequest.builder() \
        .from_date("2023-03-01") \
        .to_date("2023-03-22") \
        .page_size(20) \
        .page_token("ddowkdkl9w2d") \
        .custom_workplace_id("tpl_647184b585400013254c4ea6") \
        .build()

    # 发起请求
    response: SearchCustomWorkplaceAccessDataResponse = await client.workplace.v1.custom_workplace_access_data.asearch(
        request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.workplace.v1.custom_workplace_access_data.asearch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
