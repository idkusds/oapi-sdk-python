# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .avatar_info import AvatarInfo


class ShareUser(object):
    _types = {
        "open_id": str,
        "name": str,
        "en_name": str,
        "avatar": AvatarInfo,
    }

    def __init__(self, d=None):
        self.open_id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.avatar: Optional[AvatarInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ShareUserBuilder":
        return ShareUserBuilder()


class ShareUserBuilder(object):
    def __init__(self) -> None:
        self._share_user = ShareUser()

    def open_id(self, open_id: str) -> "ShareUserBuilder":
        self._share_user.open_id = open_id
        return self

    def name(self, name: str) -> "ShareUserBuilder":
        self._share_user.name = name
        return self

    def en_name(self, en_name: str) -> "ShareUserBuilder":
        self._share_user.en_name = en_name
        return self

    def avatar(self, avatar: AvatarInfo) -> "ShareUserBuilder":
        self._share_user.avatar = avatar
        return self

    def build(self) -> "ShareUser":
        return self._share_user
