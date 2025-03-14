import os
from dotenv import load_dotenv

load_dotenv()
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def is_user_subscribed(user_id, bot):
    try:
        user = await bot.get_chat_member(CHANNEL_ID, user_id)
        return user.status in ["member", "administrator", "creator"]
    except:
        return False