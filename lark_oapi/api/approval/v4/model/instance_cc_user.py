# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class InstanceCcUser(object):
    _types = {
        "user_id": str,
        "cc_id": str,
        "open_id": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.cc_id: Optional[str] = None
        self.open_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceCcUserBuilder":
        return InstanceCcUserBuilder()


class InstanceCcUserBuilder(object):
    def __init__(self) -> None:
        self._instance_cc_user = InstanceCcUser()

    def user_id(self, user_id: str) -> "InstanceCcUserBuilder":
        self._instance_cc_user.user_id = user_id
        return self

    def cc_id(self, cc_id: str) -> "InstanceCcUserBuilder":
        self._instance_cc_user.cc_id = cc_id
        return self

    def open_id(self, open_id: str) -> "InstanceCcUserBuilder":
        self._instance_cc_user.open_id = open_id
        return self

    def build(self) -> "InstanceCcUser":
        return self._instance_cc_user
