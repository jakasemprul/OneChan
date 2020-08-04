import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.neko(?: |$)(.*)')
async def typewriter(wannasee):
	await wannasee.edit("[DiSini](https://del.dog/ucrypur) Striming Paling Ga but.")
