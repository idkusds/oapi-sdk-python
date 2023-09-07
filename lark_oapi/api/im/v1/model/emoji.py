# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Emoji(object):
    _types = {
        "emoji_type": str,
    }

    def __init__(self, d=None):
        self.emoji_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmojiBuilder":
        return EmojiBuilder()


class EmojiBuilder(object):
    def __init__(self) -> None:
        self._emoji = Emoji()

    def emoji_type(self, emoji_type: str) -> "EmojiBuilder":
        self._emoji.emoji_type = emoji_type
        return self

    def build(self) -> "Emoji":
        return self._emoji
