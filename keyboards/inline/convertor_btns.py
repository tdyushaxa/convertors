from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

convertor_inline = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text='Convertor',callback_data='Convertor'),

        ],
    ],
    resize_keyboard=True
)


typepost = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="TEXT", callback_data="text"),
            InlineKeyboardButton(text="PHOTO", callback_data="photo")
        ]
    ]
)


keyboard_admin_obuna = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="➕ Qo'shish", callback_data="kanal_qoshish"),
            InlineKeyboardButton(text="➖ Olib tashlash", callback_data="kanal_olib_tashlash"),
        ]
    ]
)

check_button_subs = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs")
    ]]
)
