from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

convertor_inline = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text='Convertor',callback_data='Convertor'),

        ],
    ],
    resize_keyboard=True
)