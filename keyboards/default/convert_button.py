from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

convertor_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='PDF ➡️ Word'),
            KeyboardButton(text='Word ➡️ PDF'),
        ],
        [
            KeyboardButton(text='Image  ➡️ text'),
            KeyboardButton(text='Image ➡️ Pdf')
        ],
    ],
    resize_keyboard=True
)

convertor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='️️️️️️️️️️️Convertor'),

        ],
    ],
    resize_keyboard=True
)

convert_word = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Convertor PDF')
        ],
    ],
    resize_keyboard=True
)


back_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 ortga')
        ],
    ],
    resize_keyboard=True
)

get_text = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Textga aylantirish!')
        ],
    ],
    resize_keyboard=True
)


get_pdf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📃 PDFga aylantirish!')
        ],
    ],
    resize_keyboard=True
)


