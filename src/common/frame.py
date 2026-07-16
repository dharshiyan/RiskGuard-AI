from dataclasses import dataclass, field
from datetime import datetime

import numpy as np


@dataclass(slots=True)
class Frame:
    """
    Represents a single video frame flowing through the AI pipeline.
    """

    frame_id: int
    camera_id: int

    image: np.ndarray

    timestamp: datetime = field(default_factory=datetime.now)