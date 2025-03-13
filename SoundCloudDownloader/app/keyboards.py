from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sub_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подписаться✅', url="https://t.me/your_channel_link"),],
    [InlineKeyboardButton(text='Проверить', callback_data="check"),]
])