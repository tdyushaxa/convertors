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
        [
            KeyboardButton(text='PDF ➡️ Get image'),
            KeyboardButton(text='Excel ➡️ PDF')
        ]
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

get_images_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Get Image')
        ],
    ],
    resize_keyboard=True
)

ex_pdf_conv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Converor Pdf')
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



cencelbtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor qilish.")
        ]
    ],
    resize_keyboard=True
)


agree = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)

adminpanelbtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📊 Statistika"),
            KeyboardButton(text="📤 Tarqatish"),
        ],
        [
            KeyboardButton(text="Xabar yuborish")
        ],
        [
            KeyboardButton(text="✅ Majburiy obuna")
        ],
    ],
    resize_keyboard=True
)