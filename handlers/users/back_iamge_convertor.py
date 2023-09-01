from PIL import Image
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.convert_button import convertor_btn, back_button, get_text
from loader import dp, bot
from states.file_state import  ImageTotext
from pytesseract import pytesseract
import os


@dp.message_handler(Text(equals='🔙 ortga'), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Ortgaa ', reply_markup=convertor_btn)

@dp.message_handler(Text(equals='Image  ➡️ text'))
async def get_photo_text(message: types.Message):
    await message.answer('Sizga istalgan 📸 textni bir zumda olib beraman...', reply_markup=ReplyKeyboardRemove())
    await message.answer('📸 Rasm yuboring ...', reply_markup=back_button)
    await ImageTotext.image.set()


@dp.message_handler(content_types='photo', state=ImageTotext.image)
async def get_photo(msg: types.Message, state: FSMContext):
    global photo_name
    photo_name = msg.photo[-1].file_unique_id
    photo_file_id = msg.photo[-1].file_id
    await bot.download_file_by_id(photo_file_id, destination=f'{photo_name}')
    await state.finish()
    await msg.answer('✅ Rasm qabul qilindi... ', reply_markup=get_text)


@dp.message_handler(Text(equals='📝 Textga aylantirish!'))
async def convert_to_text(msg: types.Message):
    try:
        img = Image.open(photo_name)
        text = pytesseract.image_to_string(img)
        await msg.answer(text, reply_markup=convertor_btn)
        os.remove(photo_name)
    except:
        await msg.answer('🚫 Rasm sifatini tekshiring !!!', reply_markup=ReplyKeyboardRemove())
        await msg.answer(text='orqaga', reply_markup=back_button)
        os.remove(photo_name)




