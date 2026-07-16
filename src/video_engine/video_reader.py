from .video_factory import VideoFactory


class VideoReader:

    def __init__(self, source):

        self.source = VideoFactory.create(source)

    def open(self):
        self.source.open()

    def read(self):
        return self.source.read()

    def release(self):
        self.source.release()