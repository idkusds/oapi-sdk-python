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
    request: FaqImageFaqRequest = FaqImageFaqRequest.builder() \
        .id("12345") \
        .image_key("img_b07ffac0-19c1-48a3-afca-599f8ea825fj") \
        .build()

    # 发起请求
    response: FaqImageFaqResponse = client.helpdesk.v1.faq.faq_image(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.faq.faq_image failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    f = open(f"/file_path/{response.file_name}", "wb")
    f.write(response.file.read())
    f.close()


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: FaqImageFaqRequest = FaqImageFaqRequest.builder() \
        .id("12345") \
        .image_key("img_b07ffac0-19c1-48a3-afca-599f8ea825fj") \
        .build()

    # 发起请求
    response: FaqImageFaqResponse = await client.helpdesk.v1.faq.afaq_image(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.faq.afaq_image failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    f = open(f"/file_path/{response.file_name}", "wb")
    f.write(response.file.read())
    f.close()


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
