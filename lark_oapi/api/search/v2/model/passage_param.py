# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .doc_passage_param import DocPassageParam
from .helpdesk_passage_param import HelpdeskPassageParam
from .web_passage_param import WebPassageParam
from .wiki_passage_param import WikiPassageParam


class PassageParam(object):
    _types = {
        "doc_param": DocPassageParam,
        "wiki_param": WikiPassageParam,
        "web_param": WebPassageParam,
        "helpdesk_param": HelpdeskPassageParam,
    }

    def __init__(self, d=None):
        self.doc_param: Optional[DocPassageParam] = None
        self.wiki_param: Optional[WikiPassageParam] = None
        self.web_param: Optional[WebPassageParam] = None
        self.helpdesk_param: Optional[HelpdeskPassageParam] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PassageParamBuilder":
        return PassageParamBuilder()


class PassageParamBuilder(object):
    def __init__(self) -> None:
        self._passage_param = PassageParam()

    def doc_param(self, doc_param: DocPassageParam) -> "PassageParamBuilder":
        self._passage_param.doc_param = doc_param
        return self

    def wiki_param(self, wiki_param: WikiPassageParam) -> "PassageParamBuilder":
        self._passage_param.wiki_param = wiki_param
        return self

    def web_param(self, web_param: WebPassageParam) -> "PassageParamBuilder":
        self._passage_param.web_param = web_param
        return self

    def helpdesk_param(self, helpdesk_param: HelpdeskPassageParam) -> "PassageParamBuilder":
        self._passage_param.helpdesk_param = helpdesk_param
        return self

    def build(self) -> "PassageParam":
        return self._passage_param
