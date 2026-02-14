from dataclasses import dataclass


@dataclass
class ServerModel:
    """Server info dataclass."""

    players: int
    slots: int
    queue: int
    time: str
