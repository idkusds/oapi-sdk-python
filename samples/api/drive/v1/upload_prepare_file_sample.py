# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id(lark.APP_ID) \
		.app_secret(lark.APP_SECRET) \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UploadPrepareFileRequest = UploadPrepareFileRequest.builder() \
		.request_body(FileUploadInfo.builder()
					  .file_name("str")
					  .parent_type("explorer")
					  .parent_node("str")
					  .size(int)
					  .build()) \
		.build()

	# 发起请求
	response: UploadPrepareFileResponse = client.drive.v1.file.upload_prepare(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.file.upload_prepare failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: UploadPrepareFileRequest = UploadPrepareFileRequest.builder() \
		.request_body(FileUploadInfo.builder()
					  .file_name("str")
					  .parent_type("explorer")
					  .parent_node("str")
					  .size(int)
					  .build()) \
		.build()

	# 发起请求
	response: UploadPrepareFileResponse = await client.drive.v1.file.aupload_prepare(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.file.aupload_prepare failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
