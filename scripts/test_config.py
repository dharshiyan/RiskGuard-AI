from src.infrastructure.config import ConfigManager


def main():
    config = ConfigManager()

    print("=" * 50)
    print(config.app)
    print("=" * 50)


if __name__ == "__main__":
    main()