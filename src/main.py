import asyncio
from typing import Any

from bot import Bot
from utils import Static, log


async def start_bot(server: dict[str, Any]) -> None:
    """Initialize and start a bot instance for the given server configuration."""
    bot = Bot(server)
    await bot.start(server["token"])


async def main() -> None:
    """Entry point for launching multiple bot instances concurrently."""
    try:
        tasks = [
            asyncio.create_task(start_bot(server))
            for server in Static.load_json("servers.json")
        ]
        await asyncio.gather(*tasks)

    except Exception as e:
        log.error("Failed to start bot", exc_info=e)
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    asyncio.run(main())
