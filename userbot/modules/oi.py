import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(wannasee):
	await wannasee.edit("[DiSini](https://telegra.ph/il-ham-08-01-2) Generate Session String.")
