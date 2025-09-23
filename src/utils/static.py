import re
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
        """Get server time from a string."""
        if not keywords:
            return "🕒 00:00"

        match = re.search(r"\b\d{1,2}:\d{2}\b", keywords)
        server_time = match.group(0) if match else "00:00"

        if "05:00" <= server_time < "20:00":
            return f"🌤️ {server_time}"
        return f"🌙 {server_time}"

    @staticmethod
    def get_server_queue(keywords: str) -> int:
        """Get server queue from a string."""
        if not keywords:
            return 0

        match = re.search(r"lqs(\d+)", keywords)
        return int(match.group(1)) if match else 0
