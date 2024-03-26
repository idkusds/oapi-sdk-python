# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .trade_detail import TradeDetail


class ReconciliationReferralAccountRequestBody(object):
    _types = {
        "start_trans_time": str,
        "end_trans_time": str,
        "trade_details": List[TradeDetail],
    }

    def __init__(self, d=None):
        self.start_trans_time: Optional[str] = None
        self.end_trans_time: Optional[str] = None
        self.trade_details: Optional[List[TradeDetail]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReconciliationReferralAccountRequestBodyBuilder":
        return ReconciliationReferralAccountRequestBodyBuilder()


class ReconciliationReferralAccountRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._reconciliation_referral_account_request_body = ReconciliationReferralAccountRequestBody()

    def start_trans_time(self, start_trans_time: str) -> "ReconciliationReferralAccountRequestBodyBuilder":
        self._reconciliation_referral_account_request_body.start_trans_time = start_trans_time
        return self

    def end_trans_time(self, end_trans_time: str) -> "ReconciliationReferralAccountRequestBodyBuilder":
        self._reconciliation_referral_account_request_body.end_trans_time = end_trans_time
        return self

    def trade_details(self, trade_details: List[TradeDetail]) -> "ReconciliationReferralAccountRequestBodyBuilder":
        self._reconciliation_referral_account_request_body.trade_details = trade_details
        return self

    def build(self) -> "ReconciliationReferralAccountRequestBody":
        return self._reconciliation_referral_account_request_body
