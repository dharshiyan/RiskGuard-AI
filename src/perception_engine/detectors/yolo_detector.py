from ultralytics import YOLO

from src.common import BoundingBox, Detection, Frame
from src.infrastructure.config import ConfigManager

from .base_detector import BaseDetector


class YOLODetector(BaseDetector):

    def __init__(self):
        self.model = None

        config = ConfigManager()

        self.cfg = config.detection["detection"]

    def load(self):

        self.model = YOLO(
            self.cfg["model"]["name"]
        )

    def detect(self, frame: Frame) -> list[Detection]:

        results = self.model(
            frame.image,
            conf=self.cfg["model"]["confidence"],
            iou=self.cfg["model"]["iou"],
            device=self.cfg["model"]["device"],
            imgsz=self.cfg["inference"]["image_size"],
            verbose=self.cfg["inference"]["verbose"],
        )

        detections = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls.item())

                if self.cfg["classes"]["person_only"]:
                    if class_id != self.cfg["classes"]["person_class_id"]:
                        continue

                bbox = BoundingBox(
                    x1=float(box.xyxy[0][0]),
                    y1=float(box.xyxy[0][1]),
                    x2=float(box.xyxy[0][2]),
                    y2=float(box.xyxy[0][3]),
                )

                detection = Detection(
                    class_id=class_id,
                    class_name=result.names[class_id],
                    confidence=float(box.conf.item()),
                    bbox=bbox,
                )

                detections.append(detection)

        return detections