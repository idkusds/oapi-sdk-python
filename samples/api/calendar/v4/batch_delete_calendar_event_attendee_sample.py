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
	request: BatchDeleteCalendarEventAttendeeRequest = BatchDeleteCalendarEventAttendeeRequest.builder() \
		.calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
		.event_id("xxxxxxxxx_0") \
		.user_id_type("user_id") \
		.request_body(BatchDeleteCalendarEventAttendeeRequestBody.builder()
					  .attendee_ids([])
					  .delete_ids([])
					  .need_notification(False)
					  .instance_start_time_admin("1647320400")
					  .is_enable_admin(False)
					  .build()) \
		.build()

	# 发起请求
	response: BatchDeleteCalendarEventAttendeeResponse = client.calendar.v4.calendar_event_attendee.batch_delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.calendar.v4.calendar_event_attendee.batch_delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: BatchDeleteCalendarEventAttendeeRequest = BatchDeleteCalendarEventAttendeeRequest.builder() \
		.calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
		.event_id("xxxxxxxxx_0") \
		.user_id_type("user_id") \
		.request_body(BatchDeleteCalendarEventAttendeeRequestBody.builder()
					  .attendee_ids([])
					  .delete_ids([])
					  .need_notification(False)
					  .instance_start_time_admin("1647320400")
					  .is_enable_admin(False)
					  .build()) \
		.build()

	# 发起请求
	response: BatchDeleteCalendarEventAttendeeResponse = await client.calendar.v4.calendar_event_attendee.abatch_delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.calendar.v4.calendar_event_attendee.abatch_delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
