# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MetricUnit(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
        "ja_jp": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        self.ja_jp: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetricUnitBuilder":
        return MetricUnitBuilder()


class MetricUnitBuilder(object):
    def __init__(self) -> None:
        self._metric_unit = MetricUnit()

    def zh_cn(self, zh_cn: str) -> "MetricUnitBuilder":
        self._metric_unit.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "MetricUnitBuilder":
        self._metric_unit.en_us = en_us
        return self

    def ja_jp(self, ja_jp: str) -> "MetricUnitBuilder":
        self._metric_unit.ja_jp = ja_jp
        return self

    def build(self) -> "MetricUnit":
        return self._metric_unit
