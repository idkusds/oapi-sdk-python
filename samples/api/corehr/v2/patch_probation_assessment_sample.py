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
	request: PatchProbationAssessmentRequest = PatchProbationAssessmentRequest.builder() \
		.assessment_id("7140964208476371331") \
		.client_token("6822122262122064111") \
		.request_body(AssessmentForCreate.builder()
					  .assessment_status("completed")
					  .assessment_result("approved")
					  .assessment_score(99.9)
					  .assessment_grade("grade_a")
					  .assessment_comment("超出预期")
					  .assessment_detail("暂无示例")
					  .is_final_asssessment(False)
					  .build()) \
		.build()

	# 发起请求
	response: PatchProbationAssessmentResponse = client.corehr.v2.probation_assessment.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v2.probation_assessment.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
	request: PatchProbationAssessmentRequest = PatchProbationAssessmentRequest.builder() \
		.assessment_id("7140964208476371331") \
		.client_token("6822122262122064111") \
		.request_body(AssessmentForCreate.builder()
					  .assessment_status("completed")
					  .assessment_result("approved")
					  .assessment_score(99.9)
					  .assessment_grade("grade_a")
					  .assessment_comment("超出预期")
					  .assessment_detail("暂无示例")
					  .is_final_asssessment(False)
					  .build()) \
		.build()

	# 发起请求
	response: PatchProbationAssessmentResponse = await client.corehr.v2.probation_assessment.apatch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v2.probation_assessment.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	# asyncio.run(amain()) 异步方式
	main()
