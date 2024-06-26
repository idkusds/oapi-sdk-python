# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchCostCenterVersionRequest = PatchCostCenterVersionRequest.builder() \
        .cost_center_id("6862995757234914824") \
        .version_id("6862995757234914824") \
        .user_id_type("people_corehr_id") \
        .request_body(PatchCostCenterVersionRequestBody.builder()
                      .name([])
                      .parent_cost_center_id("6862995757234914824")
                      .managers([])
                      .description([])
                      .effective_time("2020-01-01")
                      .operation_reason("强行操作")
                      .build()) \
        .build()

    # 发起请求
    response: PatchCostCenterVersionResponse = client.corehr.v2.cost_center_version.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.cost_center_version.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PatchCostCenterVersionRequest = PatchCostCenterVersionRequest.builder() \
        .cost_center_id("6862995757234914824") \
        .version_id("6862995757234914824") \
        .user_id_type("people_corehr_id") \
        .request_body(PatchCostCenterVersionRequestBody.builder()
                      .name([])
                      .parent_cost_center_id("6862995757234914824")
                      .managers([])
                      .description([])
                      .effective_time("2020-01-01")
                      .operation_reason("强行操作")
                      .build()) \
        .build()

    # 发起请求
    response: PatchCostCenterVersionResponse = await client.corehr.v2.cost_center_version.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.cost_center_version.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
