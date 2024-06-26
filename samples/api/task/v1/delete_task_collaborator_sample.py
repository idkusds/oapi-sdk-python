# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteTaskCollaboratorRequest = DeleteTaskCollaboratorRequest.builder() \
        .task_id("83912691-2e43-47fc-94a4-d512e03984fa") \
        .collaborator_id("ou_99e1a581b36ecc4862cbfbce123f346a") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: DeleteTaskCollaboratorResponse = client.task.v1.task_collaborator.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v1.task_collaborator.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: DeleteTaskCollaboratorRequest = DeleteTaskCollaboratorRequest.builder() \
        .task_id("83912691-2e43-47fc-94a4-d512e03984fa") \
        .collaborator_id("ou_99e1a581b36ecc4862cbfbce123f346a") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: DeleteTaskCollaboratorResponse = await client.task.v1.task_collaborator.adelete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v1.task_collaborator.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
