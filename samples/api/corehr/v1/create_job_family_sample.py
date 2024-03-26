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
	request: CreateJobFamilyRequest = CreateJobFamilyRequest.builder() \
		.client_token("12454646") \
		.request_body(JobFamily.builder()
					  .name([])
					  .active(True)
					  .parent_id("4698020757495316313")
					  .effective_time("2020-05-01 00:00:00")
					  .expiration_time("2020-05-02 00:00:00")
					  .code("123456")
					  .custom_fields([])
					  .build()) \
		.build()

	# 发起请求
	response: CreateJobFamilyResponse = client.corehr.v1.job_family.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.job_family.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: CreateJobFamilyRequest = CreateJobFamilyRequest.builder() \
		.client_token("12454646") \
		.request_body(JobFamily.builder()
					  .name([])
					  .active(True)
					  .parent_id("4698020757495316313")
					  .effective_time("2020-05-01 00:00:00")
					  .expiration_time("2020-05-02 00:00:00")
					  .code("123456")
					  .custom_fields([])
					  .build()) \
		.build()

	# 发起请求
	response: CreateJobFamilyResponse = await client.corehr.v1.job_family.acreate(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.job_family.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
