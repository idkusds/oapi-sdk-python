# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.application.v6 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: PatchApplicationAppVersionRequest = PatchApplicationAppVersionRequest.builder() \
		.app_id("cli_9f3ca975326b501b") \
		.version_id("oav_d317f090b7258ad0372aa53963cda70d") \
		.user_id_type("user_id") \
		.operator_id("ou_4065981088f8ef67a504ba8bd6b24d85") \
		.reject_reason("拒绝理由") \
		.request_body(ApplicationAppVersion.builder()
					  .status(1)
					  .build()) \
		.build()

	# 发起请求
	response: PatchApplicationAppVersionResponse = client.application.v6.application_app_version.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.application.v6.application_app_version.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: PatchApplicationAppVersionRequest = PatchApplicationAppVersionRequest.builder() \
		.app_id("cli_9f3ca975326b501b") \
		.version_id("oav_d317f090b7258ad0372aa53963cda70d") \
		.user_id_type("user_id") \
		.operator_id("ou_4065981088f8ef67a504ba8bd6b24d85") \
		.reject_reason("拒绝理由") \
		.request_body(ApplicationAppVersion.builder()
					  .status(1)
					  .build()) \
		.build()

	# 发起请求
	response: PatchApplicationAppVersionResponse = await client.application.v6.application_app_version.apatch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.application.v6.application_app_version.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
