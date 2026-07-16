from abc import ABC, abstractmethod

from src.common import Frame, Detection


class BaseDetector(ABC):
    """
    Base interface for all object detectors.
    """

    @abstractmethod
    def load(self) -> None:
        """
        Load the AI model into memory.
        """
        pass

    @abstractmethod
    def detect(self, frame: Frame) -> list[Detection]:
        """
        Run inference on a single frame.
        """
        pass