# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DownloadMediaRequest = DownloadMediaRequest.builder() \
        .file_token("boxcnrHpsg1QDqXAAAyachabcef") \
        .extra(
        "[请参考-上传点类型及对应Extra说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/introduction)") \
        .build()

    # 发起请求
    response: DownloadMediaResponse = client.drive.v1.media.download(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.media.download failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: DownloadMediaRequest = DownloadMediaRequest.builder() \
        .file_token("boxcnrHpsg1QDqXAAAyachabcef") \
        .extra(
        "[请参考-上传点类型及对应Extra说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/introduction)") \
        .build()

    # 发起请求
    response: DownloadMediaResponse = await client.drive.v1.media.adownload(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.media.adownload failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    f = open(f"/file_path/{response.file_name}", "wb")
    f.write(response.file.read())
    f.close()


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
