from enum import Enum


class VideoSource(Enum):
    CAMERA = 0
    VIDEO_FILE = 1
    RTSP = 2