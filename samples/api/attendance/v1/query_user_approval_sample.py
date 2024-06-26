# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.attendance.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: QueryUserApprovalRequest = QueryUserApprovalRequest.builder() \
        .employee_type("employee_id") \
        .request_body(QueryUserApprovalRequestBody.builder()
                      .user_ids([])
                      .check_date_from(20190817)
                      .check_date_to(20190820)
                      .check_date_type("PeriodTime")
                      .status(2)
                      .check_time_from("1566641088")
                      .check_time_to("1592561088")
                      .build()) \
        .build()

    # 发起请求
    response: QueryUserApprovalResponse = client.attendance.v1.user_approval.query(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.attendance.v1.user_approval.query failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: QueryUserApprovalRequest = QueryUserApprovalRequest.builder() \
        .employee_type("employee_id") \
        .request_body(QueryUserApprovalRequestBody.builder()
                      .user_ids([])
                      .check_date_from(20190817)
                      .check_date_to(20190820)
                      .check_date_type("PeriodTime")
                      .status(2)
                      .check_time_from("1566641088")
                      .check_time_to("1592561088")
                      .build()) \
        .build()

    # 发起请求
    response: QueryUserApprovalResponse = await client.attendance.v1.user_approval.aquery(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.attendance.v1.user_approval.aquery failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
