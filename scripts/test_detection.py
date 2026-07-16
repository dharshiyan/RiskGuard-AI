from src.common import BoundingBox, Detection

bbox = BoundingBox(
    120,
    50,
    280,
    410
)

det = Detection(
    class_id=0,
    class_name="person",
    confidence=0.94,
    bbox=bbox
)

print(det)