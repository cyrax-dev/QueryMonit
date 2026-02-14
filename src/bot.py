from typing import Any

from disnake import CustomActivity
from disnake.ext import commands, tasks

from core import A2SUnavailableError, log
from services import GameServerService


class Bot(commands.InteractionBot):
    """Class for bot."""

    def __init__(self, server: dict[str, Any], game_server: GameServerService) -> None:
        """Initialize bot."""
        super().__init__()
        self.game_server = game_server
        self.ipv4 = server["ip"]
        self.port = server["port"]
        self.template = server["template"]
        self.offline = server["offline"]

    async def on_ready(self) -> None:
        """Event handler called when the bot is ready."""
        log.info("%s connected", self.user.display_name)
        await self.update_status_loop.start()

    async def update_status(self) -> None:
        """Update the bot's presence status with current server statistics."""
        try:
            info = await self.game_server.get_info(self.ipv4, self.port)
            status = self.template.format(players=info.players, slots=info.slots, queue=info.queue, time=info.time)

        except A2SUnavailableError:
            status = self.offline

        await self.change_presence(activity=CustomActivity(name=status))
        log.info("%s: %s", self.user.display_name, status)

    @tasks.loop(seconds=5)
    async def update_status_loop(self) -> None:
        """Update the bot's presence status with current server statistics."""
        await self.update_status()
