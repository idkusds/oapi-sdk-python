# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateEcoAccountCustomFieldRequest = CreateEcoAccountCustomFieldRequest.builder() \
		.request_body(EcoAccountCustomField.builder()
					  .scope(1)
					  .custom_field_list([])
					  .build()) \
		.build()

	# 发起请求
	response: CreateEcoAccountCustomFieldResponse = client.hire.v1.eco_account_custom_field.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.eco_account_custom_field.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: CreateEcoAccountCustomFieldRequest = CreateEcoAccountCustomFieldRequest.builder() \
		.request_body(EcoAccountCustomField.builder()
					  .scope(1)
					  .custom_field_list([])
					  .build()) \
		.build()

	# 发起请求
	response: CreateEcoAccountCustomFieldResponse = await client.hire.v1.eco_account_custom_field.acreate(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.eco_account_custom_field.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
