# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: PatchAppTableRequest = PatchAppTableRequest.builder() \
		.app_token("str") \
		.table_id("str") \
		.request_body(PatchAppTableRequestBody.builder()
					  .name("str")
					  .build()) \
		.build()

	# 发起请求
	response: PatchAppTableResponse = client.bitable.v1.app_table.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.bitable.v1.app_table.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: PatchAppTableRequest = PatchAppTableRequest.builder() \
		.app_token("str") \
		.table_id("str") \
		.request_body(PatchAppTableRequestBody.builder()
					  .name("str")
					  .build()) \
		.build()

	# 发起请求
	response: PatchAppTableResponse = await client.bitable.v1.app_table.apatch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.bitable.v1.app_table.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
