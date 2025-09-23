from a2s import ainfo

from utils import Static, log

from .server_info import ServerInfo


class GameServer:
    """Game server class."""

    @staticmethod
    async def get_server_info(ipv4: str, query_port: int) -> ServerInfo:
        """Get server info."""
        try:
            default_response = ServerInfo()
            server_info = await ainfo(address=(ipv4, query_port), timeout=5)

            server_time = Static.get_server_time(server_info.keywords)
            server_queue = Static.get_server_queue(server_info.keywords)

            return ServerInfo(
                players=server_info.player_count,
                slots=server_info.max_players,
                queue=server_queue,
                time=server_time,
                status=True,
            )

        except TimeoutError:
            log.error("Timeout error while getting server info")
            return default_response

        except Exception as e:
            log.error("Failed to get server info", exc_info=e)
            return default_response
