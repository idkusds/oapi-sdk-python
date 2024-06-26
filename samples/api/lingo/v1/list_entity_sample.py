# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.lingo.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListEntityRequest = ListEntityRequest.builder() \
        .page_size(20) \
        .page_token("408ecac018b2e3518db37275e812aad7bb8ad3e755fc886f322ac6c430ba") \
        .provider("星云") \
        .repo_id("7152790921053274113") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: ListEntityResponse = client.lingo.v1.entity.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.lingo.v1.entity.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListEntityRequest = ListEntityRequest.builder() \
        .page_size(20) \
        .page_token("408ecac018b2e3518db37275e812aad7bb8ad3e755fc886f322ac6c430ba") \
        .provider("星云") \
        .repo_id("7152790921053274113") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: ListEntityResponse = await client.lingo.v1.entity.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.lingo.v1.entity.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
