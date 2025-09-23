from dataclasses import dataclass


@dataclass
class ServerInfo:
    """Represents server information with default values."""

    players: int = 0
    slots: int = 0
    queue: int = 0
    time: str = "00:00"
    status: bool = False
