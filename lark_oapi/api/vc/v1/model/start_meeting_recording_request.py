# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .start_meeting_recording_request_body import StartMeetingRecordingRequestBody


class StartMeetingRecordingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.meeting_id: Optional[int] = None
        self.request_body: Optional[StartMeetingRecordingRequestBody] = None

    @staticmethod
    def builder() -> "StartMeetingRecordingRequestBuilder":
        return StartMeetingRecordingRequestBuilder()


class StartMeetingRecordingRequestBuilder(object):

    def __init__(self) -> None:
        start_meeting_recording_request = StartMeetingRecordingRequest()
        start_meeting_recording_request.http_method = HttpMethod.PATCH
        start_meeting_recording_request.uri = "/open-apis/vc/v1/meetings/:meeting_id/recording/start"
        start_meeting_recording_request.token_types = {AccessTokenType.USER}
        self._start_meeting_recording_request: StartMeetingRecordingRequest = start_meeting_recording_request

    def meeting_id(self, meeting_id: int) -> "StartMeetingRecordingRequestBuilder":
        self._start_meeting_recording_request.meeting_id = meeting_id
        self._start_meeting_recording_request.paths["meeting_id"] = str(meeting_id)
        return self

    def request_body(self, request_body: StartMeetingRecordingRequestBody) -> "StartMeetingRecordingRequestBuilder":
        self._start_meeting_recording_request.request_body = request_body
        self._start_meeting_recording_request.body = request_body
        return self

    def build(self) -> StartMeetingRecordingRequest:
        return self._start_meeting_recording_request
