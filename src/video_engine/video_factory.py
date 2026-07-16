from .file_video_source import FileVideoSource


class VideoFactory:

    @staticmethod
    def create(source):

        if isinstance(source, str):
            return FileVideoSource(source)

        raise ValueError("Unsupported video source.")