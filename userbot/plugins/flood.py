"""COMMAND : .floodwarn"""

from telethon import events
import asyncio
from collections import deque

from userbot.cmdhelp imprt CmdHelp
CmdHelp("floodwarn").add_command(
    "floodwarn", None, "Flood warn"
).add()
@borg.on(events.NewMessage(pattern=r".floodwarn", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("💙💛💓💔💘💕💜💚💝💞💟"))
	for _ in range(100000000):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
