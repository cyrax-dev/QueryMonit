from json import load
from pathlib import Path


class Static:
    """Static class help methods."""

    @staticmethod
    def load_json(path: str) -> list:
        """Load json file."""
        path_obj = Path(path)

        with path_obj.open(encoding="utf-8") as file:
            return load(file)

    @staticmethod
    def get_server_time(keywords: str) -> str:
        """Get server time."""
        if not keywords:
            return "🕒 00:00"

        server_time = keywords.split(",")[-1].strip()

        if "05:00" <= server_time < "20:00":
            return f"🌤️ {server_time}"
        return f"🌙 {server_time}"

    @staticmethod
    def get_server_queue(keywords: str) -> str:
        """Get server queue."""
        if not keywords:
            return 0

        server_queue = keywords.split(",")[-5].strip()
        return int("".join(c for c in server_queue if c.isdigit()))
