from pyrogram import Client, filters
from pyromod import listen

from config import Config

SAMPLE = Client(
        "SAMPLE",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=10
    )

SAMPLE.start()

@Client.on_message(filters.command("start"))
async def start_bot(client, message):
    await message.reply_text(text=f"Hello {message.from_user.mention}")
    
SAMPLE.idle()
