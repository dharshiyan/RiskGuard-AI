from dataclasses import dataclass

from .bbox import BoundingBox


@dataclass(slots=True)
class Detection:
    """
    Represents one object detected in a frame.
    """

    class_id: int
    class_name: str

    confidence: float

    bbox: BoundingBox