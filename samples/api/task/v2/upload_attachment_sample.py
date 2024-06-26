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
    file = open("file_path", "rb")
    request: UploadAttachmentRequest = UploadAttachmentRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputAttachment.builder()
                      .resource_type("task")
                      .resource_id("fe96108d-b004-4a47-b2f8-6886e758b3a5")
                      .file(file)
                      .build()) \
        .build()

    # 发起请求
    response: UploadAttachmentResponse = client.task.v2.attachment.upload(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.attachment.upload failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    file = open("file_path", "rb")
    request: UploadAttachmentRequest = UploadAttachmentRequest.builder() \
        .user_id_type("open_id") \
        .request_body(InputAttachment.builder()
                      .resource_type("task")
                      .resource_id("fe96108d-b004-4a47-b2f8-6886e758b3a5")
                      .file(file)
                      .build()) \
        .build()

    # 发起请求
    response: UploadAttachmentResponse = await client.task.v2.attachment.aupload(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.attachment.aupload failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
