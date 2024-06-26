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
    request: CreateSectionRequest = CreateSectionRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputSection.builder()
                      .name("已经审核过的任务")
                      .resource_type("tasklist")
                      .resource_id("cc371766-6584-cf50-a222-c22cd9055004")
                      .insert_before("e6e37dcc-f75a-5936-f589-12fb4b5c80c2")
                      .insert_after("e6e37dcc-f75a-5936-f589-12fb4b5c80c2")
                      .build()) \
        .build()

    # 发起请求
    response: CreateSectionResponse = client.task.v2.section.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.section.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateSectionRequest = CreateSectionRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputSection.builder()
                      .name("已经审核过的任务")
                      .resource_type("tasklist")
                      .resource_id("cc371766-6584-cf50-a222-c22cd9055004")
                      .insert_before("e6e37dcc-f75a-5936-f589-12fb4b5c80c2")
                      .insert_after("e6e37dcc-f75a-5936-f589-12fb4b5c80c2")
                      .build()) \
        .build()

    # 发起请求
    response: CreateSectionResponse = await client.task.v2.section.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.section.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
