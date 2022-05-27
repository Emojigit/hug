# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/hug"
__description__ = "Give you a hug! 🤗"
__dname__ = "hug"

from telethon import events, utils
import config, sys, os.path
hug = "🤗"
hug_requested = ["抱抱","貼貼","贴贴"]
def setup(bot,storage):
    @bot.on(events.NewMessage())
    async def hug_check(event):
        text = event.text
        for x in hug_requested:
            if x in text:
                await bot.send_message(event.chat,hug,reply_to=(await event.get_reply_message()) or event.message)
                break
