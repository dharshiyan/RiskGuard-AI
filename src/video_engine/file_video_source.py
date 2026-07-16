import cv2

from .base_video_source import BaseVideoSource


class FileVideoSource(BaseVideoSource):

    def __init__(self, video_path: str):
        self.video_path = video_path
        self.capture = None

    def open(self):
        self.capture = cv2.VideoCapture(self.video_path)

        if not self.capture.isOpened():
            raise RuntimeError(
                f"Unable to open video: {self.video_path}"
            )

    def read(self):
        success, frame = self.capture.read()

        if not success:
            return None

        return frame

    def release(self):
        if self.capture:
            self.capture.release()