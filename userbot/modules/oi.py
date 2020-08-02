import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(wannasee):
	message = wannasee.pattern_match.group(1)
	sleep(1)
	await wannasee.edit("`Click [here](https://github.com/Ilham94/OneChan)`")
	
