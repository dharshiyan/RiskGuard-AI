from pathlib import Path

from .config_loader import ConfigLoader


class ConfigManager:
    """
    Loads and stores all project configurations.
    """

    def __init__(self, config_directory: str = "configs/development"):
        self.config_directory = Path(config_directory)

        self.app = self._load("app.yaml")
        self.camera = self._load("camera.yaml")
        self.detection = self._load("detection.yaml")
        self.tracking = self._load("tracking.yaml")
        self.reid = self._load("reid.yaml")
        self.behavior = self._load("behavior.yaml")
        self.risk = self._load("risk.yaml")
        self.logging = self._load("logging.yaml")

    def _load(self, filename: str):
        return ConfigLoader.load(self.config_directory / filename)