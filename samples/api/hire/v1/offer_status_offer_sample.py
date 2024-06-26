# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: OfferStatusOfferRequest = OfferStatusOfferRequest.builder() \
        .offer_id("6930815272790114324") \
        .request_body(OfferStatusOfferRequestBody.builder()
                      .offer_status(2)
                      .expiration_date("2023-01-01")
                      .termination_reason_id_list([])
                      .termination_reason_note("不符合期望")
                      .build()) \
        .build()

    # 发起请求
    response: OfferStatusOfferResponse = client.hire.v1.offer.offer_status(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.offer.offer_status failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: OfferStatusOfferRequest = OfferStatusOfferRequest.builder() \
        .offer_id("6930815272790114324") \
        .request_body(OfferStatusOfferRequestBody.builder()
                      .offer_status(2)
                      .expiration_date("2023-01-01")
                      .termination_reason_id_list([])
                      .termination_reason_note("不符合期望")
                      .build()) \
        .build()

    # 发起请求
    response: OfferStatusOfferResponse = await client.hire.v1.offer.aoffer_status(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.offer.aoffer_status failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
