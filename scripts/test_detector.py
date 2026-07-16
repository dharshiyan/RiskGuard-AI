from src.perception_engine import DetectorFactory

detector = DetectorFactory.create("yolo")

detector.load()

print(type(detector).__name__)