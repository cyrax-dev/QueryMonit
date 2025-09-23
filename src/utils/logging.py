import logging
import sys

log_level = logging.INFO
formatter = logging.Formatter(
    fmt="[%(asctime)s] %(module)5s:%(lineno)-3d (%(levelname)-4s) - %(message)s",
    datefmt="%Y-%m-%d / %H:%M:%S",
)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(log_level)

logging.basicConfig(level=log_level, handlers=[handler])
logging.getLogger("disnake").setLevel(logging.ERROR)
logging.getLogger("discord").setLevel(logging.ERROR)
logging.getLogger("websockets").setLevel(logging.ERROR)

log = logging.getLogger()
