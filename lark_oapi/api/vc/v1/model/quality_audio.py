# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class QualityAudio(object):
    _types = {
        "time": str,
        "mic_input_volume": str,
        "speaker_volume": str,
        "bitrate_received": str,
        "latency_received": str,
        "jitter_received": str,
        "bitrate_sent": str,
        "latency_sent": str,
        "jitter_sent": str,
    }

    def __init__(self, d=None):
        self.time: Optional[str] = None
        self.mic_input_volume: Optional[str] = None
        self.speaker_volume: Optional[str] = None
        self.bitrate_received: Optional[str] = None
        self.latency_received: Optional[str] = None
        self.jitter_received: Optional[str] = None
        self.bitrate_sent: Optional[str] = None
        self.latency_sent: Optional[str] = None
        self.jitter_sent: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QualityAudioBuilder":
        return QualityAudioBuilder()


class QualityAudioBuilder(object):
    def __init__(self) -> None:
        self._quality_audio = QualityAudio()

    def time(self, time: str) -> "QualityAudioBuilder":
        self._quality_audio.time = time
        return self

    def mic_input_volume(self, mic_input_volume: str) -> "QualityAudioBuilder":
        self._quality_audio.mic_input_volume = mic_input_volume
        return self

    def speaker_volume(self, speaker_volume: str) -> "QualityAudioBuilder":
        self._quality_audio.speaker_volume = speaker_volume
        return self

    def bitrate_received(self, bitrate_received: str) -> "QualityAudioBuilder":
        self._quality_audio.bitrate_received = bitrate_received
        return self

    def latency_received(self, latency_received: str) -> "QualityAudioBuilder":
        self._quality_audio.latency_received = latency_received
        return self

    def jitter_received(self, jitter_received: str) -> "QualityAudioBuilder":
        self._quality_audio.jitter_received = jitter_received
        return self

    def bitrate_sent(self, bitrate_sent: str) -> "QualityAudioBuilder":
        self._quality_audio.bitrate_sent = bitrate_sent
        return self

    def latency_sent(self, latency_sent: str) -> "QualityAudioBuilder":
        self._quality_audio.latency_sent = latency_sent
        return self

    def jitter_sent(self, jitter_sent: str) -> "QualityAudioBuilder":
        self._quality_audio.jitter_sent = jitter_sent
        return self

    def build(self) -> "QualityAudio":
        return self._quality_audio
