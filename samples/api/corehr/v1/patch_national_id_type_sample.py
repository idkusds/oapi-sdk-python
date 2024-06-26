# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchNationalIdTypeRequest = PatchNationalIdTypeRequest.builder() \
        .national_id_type_id("1616161616") \
        .client_token("12454646") \
        .request_body(NationalIdType.builder()
                      .country_region_id("6862995747139225096")
                      .name([])
                      .active(True)
                      .validation_rule("")
                      .validation_rule_description([])
                      .code("AUS-TFN")
                      .identification_type(Enum.builder().build())
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchNationalIdTypeResponse = client.corehr.v1.national_id_type.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.national_id_type.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PatchNationalIdTypeRequest = PatchNationalIdTypeRequest.builder() \
        .national_id_type_id("1616161616") \
        .client_token("12454646") \
        .request_body(NationalIdType.builder()
                      .country_region_id("6862995747139225096")
                      .name([])
                      .active(True)
                      .validation_rule("")
                      .validation_rule_description([])
                      .code("AUS-TFN")
                      .identification_type(Enum.builder().build())
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchNationalIdTypeResponse = await client.corehr.v1.national_id_type.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.national_id_type.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
