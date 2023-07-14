# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ImDepthData(object):
    _types = {
        "p_date": str,
        "department_id": str,
        "department_path": str,
        "send_msg_rate": float,
        "avg_send_msg_cnt": float,
        "pc_send_msg_rate": float,
        "pc_avg_send_msg_cnt": float,
        "mobile_send_msg_rate": float,
        "mobile_avg_send_msg_cnt": float,
        "meeting_group_send_msg_rate": float,
        "tenant_group_send_msg_rate": float,
        "dept_group_send_msg_rate": float,
        "topic_group_send_msg_rate": float,
        "group_at_msg_rate": float,
        "group_reply_msg_rate": float,
        "reaction_rate": float,
        "p2p_send_msg_rate": float,
        "img_send_msg_rate": float,
        "file_send_msg_rate": float,
        "sticker_send_msg_rate": float,
        "post_send_msg_rate": float,
    }

    def __init__(self, d):
        self.p_date: Optional[str] = None
        self.department_id: Optional[str] = None
        self.department_path: Optional[str] = None
        self.send_msg_rate: Optional[float] = None
        self.avg_send_msg_cnt: Optional[float] = None
        self.pc_send_msg_rate: Optional[float] = None
        self.pc_avg_send_msg_cnt: Optional[float] = None
        self.mobile_send_msg_rate: Optional[float] = None
        self.mobile_avg_send_msg_cnt: Optional[float] = None
        self.meeting_group_send_msg_rate: Optional[float] = None
        self.tenant_group_send_msg_rate: Optional[float] = None
        self.dept_group_send_msg_rate: Optional[float] = None
        self.topic_group_send_msg_rate: Optional[float] = None
        self.group_at_msg_rate: Optional[float] = None
        self.group_reply_msg_rate: Optional[float] = None
        self.reaction_rate: Optional[float] = None
        self.p2p_send_msg_rate: Optional[float] = None
        self.img_send_msg_rate: Optional[float] = None
        self.file_send_msg_rate: Optional[float] = None
        self.sticker_send_msg_rate: Optional[float] = None
        self.post_send_msg_rate: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImDepthDataBuilder":
        return ImDepthDataBuilder()


class ImDepthDataBuilder(object):
    def __init__(self, im_depth_data: ImDepthData = ImDepthData({})) -> None:
        self._im_depth_data: ImDepthData = im_depth_data
    
    def p_date(self, p_date: str) -> "ImDepthDataBuilder":
        self._im_depth_data.p_date = p_date
        return self
    
    def department_id(self, department_id: str) -> "ImDepthDataBuilder":
        self._im_depth_data.department_id = department_id
        return self
    
    def department_path(self, department_path: str) -> "ImDepthDataBuilder":
        self._im_depth_data.department_path = department_path
        return self
    
    def send_msg_rate(self, send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.send_msg_rate = send_msg_rate
        return self
    
    def avg_send_msg_cnt(self, avg_send_msg_cnt: float) -> "ImDepthDataBuilder":
        self._im_depth_data.avg_send_msg_cnt = avg_send_msg_cnt
        return self
    
    def pc_send_msg_rate(self, pc_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.pc_send_msg_rate = pc_send_msg_rate
        return self
    
    def pc_avg_send_msg_cnt(self, pc_avg_send_msg_cnt: float) -> "ImDepthDataBuilder":
        self._im_depth_data.pc_avg_send_msg_cnt = pc_avg_send_msg_cnt
        return self
    
    def mobile_send_msg_rate(self, mobile_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.mobile_send_msg_rate = mobile_send_msg_rate
        return self
    
    def mobile_avg_send_msg_cnt(self, mobile_avg_send_msg_cnt: float) -> "ImDepthDataBuilder":
        self._im_depth_data.mobile_avg_send_msg_cnt = mobile_avg_send_msg_cnt
        return self
    
    def meeting_group_send_msg_rate(self, meeting_group_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.meeting_group_send_msg_rate = meeting_group_send_msg_rate
        return self
    
    def tenant_group_send_msg_rate(self, tenant_group_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.tenant_group_send_msg_rate = tenant_group_send_msg_rate
        return self
    
    def dept_group_send_msg_rate(self, dept_group_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.dept_group_send_msg_rate = dept_group_send_msg_rate
        return self
    
    def topic_group_send_msg_rate(self, topic_group_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.topic_group_send_msg_rate = topic_group_send_msg_rate
        return self
    
    def group_at_msg_rate(self, group_at_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.group_at_msg_rate = group_at_msg_rate
        return self
    
    def group_reply_msg_rate(self, group_reply_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.group_reply_msg_rate = group_reply_msg_rate
        return self
    
    def reaction_rate(self, reaction_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.reaction_rate = reaction_rate
        return self
    
    def p2p_send_msg_rate(self, p2p_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.p2p_send_msg_rate = p2p_send_msg_rate
        return self
    
    def img_send_msg_rate(self, img_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.img_send_msg_rate = img_send_msg_rate
        return self
    
    def file_send_msg_rate(self, file_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.file_send_msg_rate = file_send_msg_rate
        return self
    
    def sticker_send_msg_rate(self, sticker_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.sticker_send_msg_rate = sticker_send_msg_rate
        return self
    
    def post_send_msg_rate(self, post_send_msg_rate: float) -> "ImDepthDataBuilder":
        self._im_depth_data.post_send_msg_rate = post_send_msg_rate
        return self
    
    def build(self) -> "ImDepthData":
        return self._im_depth_data