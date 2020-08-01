#made by @DneZyeK
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^\.kill(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Mau Saya KILL ? Wait Bro :)`")
	sleep(4)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   `Proses`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Menembak`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   `KONTOL`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   `Anda`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Yang`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Sedang`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Ngaceng`")
	number = number+ 1
	sleep(0.05)
	await typew.edit(str(number) + "%  `Processing...`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Tunggu Njirr`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Berhasil`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%  `Menembak`")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   `MAMPUSSS!!!`")
	sleep(1)
	await typew.edit("`Yhahaha, ga bisa ngeue lagi wkwkw.. dah ku kill anumu :v hahahaa mampus cok...")
	# I did it for two hours :D just ctrl+c - crtl+v






CMD_HELP.update({
    'fakeload':
    '.kill\
        \nUsage: Untuk Menembak Pacar Orang.'
})
