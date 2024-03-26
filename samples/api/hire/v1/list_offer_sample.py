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
	request: ListOfferRequest = ListOfferRequest.builder() \
		.page_token("1231231987") \
		.page_size(1) \
		.talent_id("7096320678581242123") \
		.user_id_type("user_id") \
		.employee_type_id_type("people_admin_employee_type_id") \
		.build()

	# 发起请求
	response: ListOfferResponse = client.hire.v1.offer.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.offer.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: ListOfferRequest = ListOfferRequest.builder() \
		.page_token("1231231987") \
		.page_size(1) \
		.talent_id("7096320678581242123") \
		.user_id_type("user_id") \
		.employee_type_id_type("people_admin_employee_type_id") \
		.build()

	# 发起请求
	response: ListOfferResponse = await client.hire.v1.offer.alist(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.offer.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
