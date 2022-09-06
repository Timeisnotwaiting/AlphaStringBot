import os
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

ses = Client(":Cli:", API_ID, API_HASH, BOT_TOKEN)

@ses.on_message(filters.command("start") & filters.private)
async def _start(_, m):
    start(_, m)

ses.start()
get = ses.get_me()
un = get.username
idle()

print(f"@{un} started successfully.....")
