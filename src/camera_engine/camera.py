from dataclasses import dataclass

from .camera_status import CameraStatus
from src.video_engine import VideoReader


@dataclass
class Camera:
    camera_id: int
    name: str
    source: str

    def __post_init__(self):
        self.status = CameraStatus.DISCONNECTED
        self.reader = VideoReader(self.source)

    def connect(self):
        self.status = CameraStatus.CONNECTING

        self.reader.open()

        self.status = CameraStatus.CONNECTED

    def read(self):
        frame = self.reader.read()

        if frame is None:
            return None

        self.status = CameraStatus.STREAMING

        return frame

    def disconnect(self):
        self.reader.release()

        self.status = CameraStatus.DISCONNECTED