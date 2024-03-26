# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateMessageRequest = CreateMessageRequest.builder() \
		.receive_id_type("open_id") \
		.request_body(CreateMessageRequestBody.builder()
					  .receive_id("ou_7d8a6e6df7621556ce0d21922b676706ccs")
					  .msg_type("text")
					  .content("")
					  .uuid("a0d69e20-1dd1-458b-k525-dfeca4015204")
					  .build()) \
		.build()

	# 发起请求
	response: CreateMessageResponse = client.im.v1.message.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.im.v1.message.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: CreateMessageRequest = CreateMessageRequest.builder() \
		.receive_id_type("open_id") \
		.request_body(CreateMessageRequestBody.builder()
					  .receive_id("ou_7d8a6e6df7621556ce0d21922b676706ccs")
					  .msg_type("text")
					  .content("")
					  .uuid("a0d69e20-1dd1-458b-k525-dfeca4015204")
					  .build()) \
		.build()

	# 发起请求
	response: CreateMessageResponse = await client.im.v1.message.acreate(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.im.v1.message.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
