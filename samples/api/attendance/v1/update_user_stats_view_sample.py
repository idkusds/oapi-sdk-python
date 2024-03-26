# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.attendance.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UpdateUserStatsViewRequest = UpdateUserStatsViewRequest.builder() \
		.user_stats_view_id("TmpZNU5qTTJORFF6T1RnNU5UTTNOakV6TWl0dGIyNTBhQT09") \
		.employee_type("employee_id") \
		.request_body(UpdateUserStatsViewRequestBody.builder()
					  .view(UserStatsView.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: UpdateUserStatsViewResponse = client.attendance.v1.user_stats_view.update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.attendance.v1.user_stats_view.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: UpdateUserStatsViewRequest = UpdateUserStatsViewRequest.builder() \
		.user_stats_view_id("TmpZNU5qTTJORFF6T1RnNU5UTTNOakV6TWl0dGIyNTBhQT09") \
		.employee_type("employee_id") \
		.request_body(UpdateUserStatsViewRequestBody.builder()
					  .view(UserStatsView.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: UpdateUserStatsViewResponse = await client.attendance.v1.user_stats_view.aupdate(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.attendance.v1.user_stats_view.aupdate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
