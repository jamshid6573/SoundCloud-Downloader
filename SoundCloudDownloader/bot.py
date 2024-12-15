import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import rt

bot = Bot(token=TOKEN)
dp = Dispatcher()
bot.send_audio

async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Bot Start")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")