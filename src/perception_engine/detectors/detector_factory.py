from .yolo_detector import YOLODetector


class DetectorFactory:

    @staticmethod
    def create(detector_name: str):

        detector_name = detector_name.lower()

        if detector_name == "yolo":
            return YOLODetector()

        raise ValueError(f"Unsupported detector: {detector_name}")