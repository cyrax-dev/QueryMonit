from a2s import ainfo

from core import A2SRetry
from models import ServerModel


class GameServerService:
    """Service for querying game server via A2S."""

    TIMEOUT = 5

    @A2SRetry.decorator
    async def get_info(self, ipv4: str, query_port: int) -> ServerModel:
        """Query server info and return a ServerModel instance."""
        server_info = await ainfo((ipv4, query_port), timeout=self.TIMEOUT)
        return ServerModel(
            players=server_info.player_count,
            slots=server_info.max_players,
            queue=self._parse_queue(server_info.keywords),
            time=self._parse_time(server_info.keywords),
        )

    @staticmethod
    def _parse_time(keywords: str | None) -> str:
        if not keywords:
            return "🕒 00:00"

        time_part = next((p for p in keywords.split(",") if ":" in p), "00:00")
        icon = "🌤️" if "05:00" <= time_part < "20:00" else "🌙"
        return f"{icon} {time_part}"

    @staticmethod
    def _parse_queue(keywords: str | None) -> int:
        if not keywords:
            return 0
        return next((int(p[3:]) for p in keywords.split(",") if p.startswith("lqs")), 0)
