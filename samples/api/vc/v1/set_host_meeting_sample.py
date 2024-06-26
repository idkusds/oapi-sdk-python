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
    request: SetHostMeetingRequest = SetHostMeetingRequest.builder() \
        .meeting_id("6911188411932033028") \
        .user_id_type("user_id") \
        .request_body(SetHostMeetingRequestBody.builder()
                      .host_user(MeetingUser.builder().build())
                      .old_host_user(MeetingUser.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: SetHostMeetingResponse = client.vc.v1.meeting.set_host(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.meeting.set_host failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: SetHostMeetingRequest = SetHostMeetingRequest.builder() \
        .meeting_id("6911188411932033028") \
        .user_id_type("user_id") \
        .request_body(SetHostMeetingRequestBody.builder()
                      .host_user(MeetingUser.builder().build())
                      .old_host_user(MeetingUser.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: SetHostMeetingResponse = await client.vc.v1.meeting.aset_host(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.meeting.aset_host failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
