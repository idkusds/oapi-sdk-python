# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.mail.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: BatchCreateMailgroupMemberRequest = BatchCreateMailgroupMemberRequest.builder() \
        .mailgroup_id("xxxxxxxxxxxxxxx or test_mail_group@xxx.xx") \
        .user_id_type("open_id") \
        .department_id_type("department_id") \
        .request_body(BatchCreateMailgroupMemberRequestBody.builder()
                      .items([])
                      .build()) \
        .build()

    # 发起请求
    response: BatchCreateMailgroupMemberResponse = client.mail.v1.mailgroup_member.batch_create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.mail.v1.mailgroup_member.batch_create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: BatchCreateMailgroupMemberRequest = BatchCreateMailgroupMemberRequest.builder() \
        .mailgroup_id("xxxxxxxxxxxxxxx or test_mail_group@xxx.xx") \
        .user_id_type("open_id") \
        .department_id_type("department_id") \
        .request_body(BatchCreateMailgroupMemberRequestBody.builder()
                      .items([])
                      .build()) \
        .build()

    # 发起请求
    response: BatchCreateMailgroupMemberResponse = await client.mail.v1.mailgroup_member.abatch_create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.mail.v1.mailgroup_member.abatch_create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
