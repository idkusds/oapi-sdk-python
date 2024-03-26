# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.wiki.v2 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: DeleteSpaceMemberRequest = DeleteSpaceMemberRequest.builder() \
		.space_id("7008061636015554580") \
		.member_id("g64fb7g7") \
		.request_body(Member.builder()
					  .member_type("str")
					  .member_role("str")
					  .build()) \
		.build()

	# 发起请求
	response: DeleteSpaceMemberResponse = client.wiki.v2.space_member.delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.wiki.v2.space_member.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: DeleteSpaceMemberRequest = DeleteSpaceMemberRequest.builder() \
		.space_id("7008061636015554580") \
		.member_id("g64fb7g7") \
		.request_body(Member.builder()
					  .member_type("str")
					  .member_role("str")
					  .build()) \
		.build()

	# 发起请求
	response: DeleteSpaceMemberResponse = await client.wiki.v2.space_member.adelete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.wiki.v2.space_member.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
