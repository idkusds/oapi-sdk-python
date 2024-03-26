# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.personal_settings.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: ListSystemStatusRequest = ListSystemStatusRequest.builder() \
		.page_size(50) \
		.page_token("GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ==") \
		.build()

	# 发起请求
	response: ListSystemStatusResponse = client.personal_settings.v1.system_status.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.personal_settings.v1.system_status.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: ListSystemStatusRequest = ListSystemStatusRequest.builder() \
		.page_size(50) \
		.page_token("GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ==") \
		.build()

	# 发起请求
	response: ListSystemStatusResponse = await client.personal_settings.v1.system_status.alist(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.personal_settings.v1.system_status.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
