import asyncio
import contextlib
from json import loads
from pathlib import Path
from typing import Any

from bot import Bot
from core import AppError, log
from services import GameServerService


def load_servers() -> list[dict[str, Any]]:
    """Load server configurations from the JSON file."""
    return loads(Path("servers.json").read_text("utf-8"))


async def start_bot(server: dict[str, Any], service: GameServerService) -> None:
    """Initialize and start a bot instance for the given server configuration."""
    try:
        bot = Bot(server, service)
        await bot.start(server["token"])
    except Exception as e:
        log.error("Bot crashed for server %s: %s", server.get("name", "unknown"), e)


async def main() -> None:
    """Entry point for launching multiple bot instances concurrently."""
    servers = load_servers()
    service = GameServerService()

    tasks = [asyncio.create_task(start_bot(server, service)) for server in servers]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        with contextlib.suppress(KeyboardInterrupt):
            asyncio.run(main())

    except AppError as e:
        log.error("Application error", exc_info=e)

    except Exception as e:
        log.critical("Unexpected fatal error", exc_info=e)
