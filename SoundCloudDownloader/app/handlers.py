from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, URLInputFile, InputFile, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from functions.SoundCloud import SoundCloud
from aiogram.methods.send_audio import SendAudio
from aiogram.utils.chat_action import ChatActionSender
from app.db_handlers import register_user, is_user_registered, get_all_users
from functions.functions import is_user_subscribed
from app.keyboards import sub_button
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=TOKEN)

sc = SoundCloud()
rt = Router()

class St(StatesGroup):
    url = State()






@rt.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    if not is_user_registered(user_id):
        register_user(user_id)
        await message.answer("👋 Привет! Ты был зарегистрирован в системе.")
    else:
        await message.answer("👋 Ты уже зарегистрирован в системе.")

@rt.message(F.text == 'Download Soundloud')
async def get_url(message: Message, state: FSMContext):
    await message.answer("Пришли ссылку на трек:")
    await state.set_state(St.url)

@rt.message(Command("broadcast"))
async def broadcast_message(message: Message):
    user_id = message.from_user.id

    if user_id != ADMIN_ID:
        return None

    #Проверяем, есть ли текст или фото в сообщении
    if message.photo:
        file_id = message.photo[-1].file_id
        text = message.caption[11:]
    elif message.text:
        text = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
        if text is None:
            await message.answer("🔧 Формат команды: /broadcast <сообщение>")
            return
    else:
        await message.answer("Нет текста или изображения для рассылки.")
        return

    user_ids = get_all_users()

    for user in user_ids:
        try:
            if message.photo:
                await message.bot.send_photo(user, file_id, caption=text)
            else:
                await message.bot.send_message(user, f"{text}")

        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user}: {str(e)}")

    await message.answer("✅ Сообщение было успешно отправлено всем пользователям.")

@rt.message(St.url) 
@rt.message()
async def send_audio(message: Message):
    if CHANNEL_ID:
        if not await is_user_subscribed(message.from_user.id, bot):
            await message.answer("❌ Для использования бота необходимо подписаться на канал.", reply_markup=sub_button)
        else:
            if sc.validate_url(message.text):
                    async with ChatActionSender.upload_voice(chat_id=message.chat.id, bot=bot):
                        await message.answer("Скачивание...") 
                        file = sc.dowlnload(message.text)
                        audio = FSInputFile(path=f"D:\My_projects\SoundCloudDownloader/{file['rename']}")
                        thumnail = URLInputFile(url=f"{file['thumbnail']}", filename='thumnail.jpg')
                        await bot.send_audio(message.chat.id, audio=audio, thumbnail=thumnail, performer=f"{file['uploader']}")
                        sc.delete_file(f"{file['rename']}")
            else:
                await message.answer("Неверная ссылка")
    else: 
        if sc.validate_url(message.text):
                async with ChatActionSender.upload_voice(chat_id=message.chat.id, bot=bot):
                    await message.answer("Скачивание...") 
                    file = sc.dowlnload(message.text)
                    audio = FSInputFile(path=f"downloads/{file['rename']}")
                    thumnail = URLInputFile(url=f"{file['thumbnail']}", filename='thumnail.jpg')
                    await bot.send_audio(message.chat.id, audio=audio, thumbnail=thumnail, performer=f"{file['uploader']}")
                    sc.delete_file(f"{file['rename']}")

@rt.callback_query(F.data == "check")
async def check(callback: CallbackQuery):
    if not await is_user_subscribed(callback.from_user.id, bot):
        await callback.answer("❌Не подписались")
    else:
        await callback.message.delete()
        await callback.answer("✅Вы подписались")
        await callback.bot.send_message(callback.message.from_user.id, 'Пришлите ссылку')
    

