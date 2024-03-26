# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: ListCalendarEventAttendeeRequest = ListCalendarEventAttendeeRequest.builder() \
		.calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
		.event_id("xxxxxxxxx_0") \
		.user_id_type("user_id") \
		.need_resource_customization(True) \
		.page_token("780TRhwXXXXX") \
		.page_size(20) \
		.build()

	# 发起请求
	response: ListCalendarEventAttendeeResponse = client.calendar.v4.calendar_event_attendee.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.calendar.v4.calendar_event_attendee.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: ListCalendarEventAttendeeRequest = ListCalendarEventAttendeeRequest.builder() \
		.calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
		.event_id("xxxxxxxxx_0") \
		.user_id_type("user_id") \
		.need_resource_customization(True) \
		.page_token("780TRhwXXXXX") \
		.page_size(20) \
		.build()

	# 发起请求
	response: ListCalendarEventAttendeeResponse = await client.calendar.v4.calendar_event_attendee.alist(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.calendar.v4.calendar_event_attendee.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
