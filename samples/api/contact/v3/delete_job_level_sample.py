# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.contact.v3 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: DeleteJobLevelRequest = DeleteJobLevelRequest.builder() \
		.job_level_id("mga5oa8ayjlp9rb") \
		.build()

	# 发起请求
	response: DeleteJobLevelResponse = client.contact.v3.job_level.delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.contact.v3.job_level.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: DeleteJobLevelRequest = DeleteJobLevelRequest.builder() \
		.job_level_id("mga5oa8ayjlp9rb") \
		.build()

	# 发起请求
	response: DeleteJobLevelResponse = await client.contact.v3.job_level.adelete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.contact.v3.job_level.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
