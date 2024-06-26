# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.helpdesk.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: AnswerUserQueryTicketRequest = AnswerUserQueryTicketRequest.builder() \
        .ticket_id("6945345902185807891") \
        .request_body(AnswerUserQueryTicketRequestBody.builder()
                      .event_id("abcd")
                      .faqs([])
                      .build()) \
        .build()

    # 发起请求
    response: AnswerUserQueryTicketResponse = client.helpdesk.v1.ticket.answer_user_query(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.ticket.answer_user_query failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: AnswerUserQueryTicketRequest = AnswerUserQueryTicketRequest.builder() \
        .ticket_id("6945345902185807891") \
        .request_body(AnswerUserQueryTicketRequestBody.builder()
                      .event_id("abcd")
                      .faqs([])
                      .build()) \
        .build()

    # 发起请求
    response: AnswerUserQueryTicketResponse = await client.helpdesk.v1.ticket.aanswer_user_query(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.ticket.aanswer_user_query failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
