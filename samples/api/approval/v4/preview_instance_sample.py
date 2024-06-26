# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.approval.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PreviewInstanceRequest = PreviewInstanceRequest.builder() \
        .user_id_type("open_id") \
        .request_body(PreviewInstanceRequestBody.builder()
                      .user_id("发起审批用户id，按照user_id_type类型填写")
                      .approval_code("C2CAAA90-70D9-3214-906B-B6FFF947F00D")
                      .department_id("6982332863116876308")
                      .form("")
                      .instance_code("12345CA6-97AC-32BB-8231-47C33FFFCCFD")
                      .locale("zh-CN: 中文 en-US: 英文")
                      .task_id("6982332863116876308")
                      .build()) \
        .build()

    # 发起请求
    response: PreviewInstanceResponse = client.approval.v4.instance.preview(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.approval.v4.instance.preview failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PreviewInstanceRequest = PreviewInstanceRequest.builder() \
        .user_id_type("open_id") \
        .request_body(PreviewInstanceRequestBody.builder()
                      .user_id("发起审批用户id，按照user_id_type类型填写")
                      .approval_code("C2CAAA90-70D9-3214-906B-B6FFF947F00D")
                      .department_id("6982332863116876308")
                      .form("")
                      .instance_code("12345CA6-97AC-32BB-8231-47C33FFFCCFD")
                      .locale("zh-CN: 中文 en-US: 英文")
                      .task_id("6982332863116876308")
                      .build()) \
        .build()

    # 发起请求
    response: PreviewInstanceResponse = await client.approval.v4.instance.apreview(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.approval.v4.instance.apreview failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
