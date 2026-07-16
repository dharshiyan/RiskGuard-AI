import cv2

from src.common import Frame
from src.perception_engine import DetectorFactory

detector = DetectorFactory.create("yolo")

detector.load()

image = cv2.imread("assets/sample.jpeg")

frame = Frame(
    frame_id=1,
    camera_id=1,
    image=image,
)

detections = detector.detect(frame)

print("=" * 50)

print(f"Total Detections : {len(detections)}")

print("=" * 50)

for detection in detections:
    print(detection)