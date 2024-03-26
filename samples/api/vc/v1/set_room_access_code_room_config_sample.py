# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: SetRoomAccessCodeRoomConfigRequest = SetRoomAccessCodeRoomConfigRequest.builder() \
		.request_body(SetRoomAccessCodeRoomConfigRequestBody.builder()
					  .scope(5)
					  .country_id("1")
					  .district_id("2")
					  .building_id("3")
					  .floor_name("4")
					  .room_id("67687262867363")
					  .valid_day(1)
					  .build()) \
		.build()

	# 发起请求
	response: SetRoomAccessCodeRoomConfigResponse = client.vc.v1.room_config.set_room_access_code(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.vc.v1.room_config.set_room_access_code failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: SetRoomAccessCodeRoomConfigRequest = SetRoomAccessCodeRoomConfigRequest.builder() \
		.request_body(SetRoomAccessCodeRoomConfigRequestBody.builder()
					  .scope(5)
					  .country_id("1")
					  .district_id("2")
					  .building_id("3")
					  .floor_name("4")
					  .room_id("67687262867363")
					  .valid_day(1)
					  .build()) \
		.build()

	# 发起请求
	response: SetRoomAccessCodeRoomConfigResponse = await client.vc.v1.room_config.aset_room_access_code(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.vc.v1.room_config.aset_room_access_code failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
