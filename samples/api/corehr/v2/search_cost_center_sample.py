# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: SearchCostCenterRequest = SearchCostCenterRequest.builder() \
		.page_size(100) \
		.page_token("6891251722631890445") \
		.user_id_type("people_corehr_id") \
		.request_body(SearchCostCenterRequestBody.builder()
					  .cost_center_id_list([])
					  .name_list([])
					  .code("MDPD00000023")
					  .parent_cost_center_id("6862995757234914824")
					  .get_all_version(False)
					  .build()) \
		.build()

	# 发起请求
	response: SearchCostCenterResponse = client.corehr.v2.cost_center.search(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v2.cost_center.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: SearchCostCenterRequest = SearchCostCenterRequest.builder() \
		.page_size(100) \
		.page_token("6891251722631890445") \
		.user_id_type("people_corehr_id") \
		.request_body(SearchCostCenterRequestBody.builder()
					  .cost_center_id_list([])
					  .name_list([])
					  .code("MDPD00000023")
					  .parent_cost_center_id("6862995757234914824")
					  .get_all_version(False)
					  .build()) \
		.build()

	# 发起请求
	response: SearchCostCenterResponse = await client.corehr.v2.cost_center.asearch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v2.cost_center.asearch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
