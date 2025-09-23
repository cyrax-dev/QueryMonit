import asyncio
from typing import Any

from disnake import CustomActivity
from disnake.ext import commands, tasks

from server import GameServer
from utils import log


class Bot(commands.InteractionBot):
    """Class for bot."""

    def __init__(self, server: dict[str, Any]) -> None:
        """Initialize bot."""
        self.ipv4 = server["ip"]
        self.port = server["query_port"]
        self.template = server["status_template"]
        super().__init__()

    async def on_ready(self) -> None:
        """Event handler called when the bot is ready."""
        log.info("%s connected", self.user.display_name)
        await asyncio.sleep(5)
        await self.update_status_loop.start()

    async def update_status(self) -> None:
        """Update the bot's presence status with current server statistics."""
        try:
            game_server = await GameServer.get_server_info(self.ipv4, self.port)
            status = self.template.format(
                players=game_server.players,
                slots=game_server.slots,
                queue=game_server.queue,
                time=game_server.time,
            ) if game_server.status else "🔴 Server OFF"

            await self.change_presence(activity=CustomActivity(name=status))
            log.info("%s: %s", self.user.display_name, status)

        except Exception as e:
            log.error("Failed to update status", exc_info=e)
            log.warning("Restarting bot...")
            await asyncio.sleep(10)
            await self.update_status()

    @tasks.loop(seconds=10)
    async def update_status_loop(self) -> None:
        """Periodically update the bot's status every 10 seconds."""
        await self.update_status()
