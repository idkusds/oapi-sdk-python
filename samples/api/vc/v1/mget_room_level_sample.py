# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: MgetRoomLevelRequest = MgetRoomLevelRequest.builder() \
        .request_body(MgetRoomLevelRequestBody.builder()
                      .level_ids([])
                      .build()) \
        .build()

    # 发起请求
    response: MgetRoomLevelResponse = client.vc.v1.room_level.mget(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.room_level.mget failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: MgetRoomLevelRequest = MgetRoomLevelRequest.builder() \
        .request_body(MgetRoomLevelRequestBody.builder()
                      .level_ids([])
                      .build()) \
        .build()

    # 发起请求
    response: MgetRoomLevelResponse = await client.vc.v1.room_level.amget(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.room_level.amget failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
