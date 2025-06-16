from pathlib import Path


class LogStorage:
    def __init__(self, path: Path):
        self.path = path
        self.path.mkdir(parents=True, exist_ok=True)

    def files(self) -> list[Path]:
        return [
            path for path in sorted(self.path.iterdir())
            if self.is_log_file(path)
        ]

    def is_log_file(self, path: Path) -> bool:
        return path.is_file() and path.suffix == '.json'
