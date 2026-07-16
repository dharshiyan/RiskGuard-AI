from pathlib import Path
import yaml


class ConfigLoader:
    """
    Loads YAML configuration files.
    """

    @staticmethod
    def load(config_path: str | Path) -> dict:
        config_path = Path(config_path)

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with open(config_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return data or {}