import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from app.handlers import rt

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Bot Start")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")