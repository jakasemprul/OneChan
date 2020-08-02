import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
	await typew.edit("[DiSini](https://telegra.ph/il-ham-08-02-2) Generate Session String")
        sleep(1)
	await typew.edit("`Ucap Salam Goblok...`")
	sleep(1)
	await typew.edit("`Assalamualaikum`")
