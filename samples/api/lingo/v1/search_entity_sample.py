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
    request: SearchEntityRequest = SearchEntityRequest.builder() \
        .page_size(20) \
        .page_token("b152fa6e6f62a291019a04c3a93f365f8ac641910506ff15ff4cad6534e087cb4ed8fa2c") \
        .repo_id("7202510112396640276") \
        .user_id_type("user_id") \
        .request_body(SearchEntityRequestBody.builder()
                      .query("飞书词典")
                      .classification_filter(ClassificationFilter.builder().build())
                      .sources([])
                      .creators([])
                      .build()) \
        .build()

    # 发起请求
    response: SearchEntityResponse = client.lingo.v1.entity.search(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.lingo.v1.entity.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: SearchEntityRequest = SearchEntityRequest.builder() \
        .page_size(20) \
        .page_token("b152fa6e6f62a291019a04c3a93f365f8ac641910506ff15ff4cad6534e087cb4ed8fa2c") \
        .repo_id("7202510112396640276") \
        .user_id_type("user_id") \
        .request_body(SearchEntityRequestBody.builder()
                      .query("飞书词典")
                      .classification_filter(ClassificationFilter.builder().build())
                      .sources([])
                      .creators([])
                      .build()) \
        .build()

    # 发起请求
    response: SearchEntityResponse = await client.lingo.v1.entity.asearch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.lingo.v1.entity.asearch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
