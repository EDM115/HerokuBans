import asyncio
from pyrogram import Client, filters, idle
from pyromod import listen

from config import Config

async def main():
    SAMPLE = Client(
        "SAMPLE",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=10
    )
    
    @Client.on_message(filters.command("start"))
    async def start_bot(client, message):
        await message.reply_text(text=f"Hello {message.from_user.mention}")
    
    SAMPLE.start()
    
    await idle()
    
asyncio.run(main())
