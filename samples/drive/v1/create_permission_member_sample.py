# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreatePermissionMemberRequest = lark.drive.v1.CreatePermissionMemberRequest.builder() \
		.token("doccnBKgoMyY5OMbUG6FioTXuBe") \
		.type("doc") \
		.need_notification(False) \
		.request_body(lark.drive.v1.BaseMember.builder()
					  .member_type("openid")
					  .member_id("string")
					  .perm("view")
					  .build()) \
		.build()

	# 发起请求
	response: CreatePermissionMemberResponse = client.drive.v1.permission_member.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.permission_member.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()