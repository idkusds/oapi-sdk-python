# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DownloadExportRequest = DownloadExportRequest.builder() \
        .file_token("6yHu7Igp7Igy62Ez6fLr6IJz7j9i5WMe6fHq5yZeY2Jz6yLqYAMAY46fZfEz64Lr5fYyYQ==") \
        .build()

    # 发起请求
    response: DownloadExportResponse = client.vc.v1.export.download(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.export.download failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: DownloadExportRequest = DownloadExportRequest.builder() \
        .file_token("6yHu7Igp7Igy62Ez6fLr6IJz7j9i5WMe6fHq5yZeY2Jz6yLqYAMAY46fZfEz64Lr5fYyYQ==") \
        .build()

    # 发起请求
    response: DownloadExportResponse = await client.vc.v1.export.adownload(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.export.adownload failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    f = open(f"/file_path/{response.file_name}", "wb")
    f.write(response.file.read())
    f.close()


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
