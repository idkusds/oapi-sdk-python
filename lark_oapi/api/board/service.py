# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v1.version import V1


class BoardService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)
