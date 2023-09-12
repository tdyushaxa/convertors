import os
import time

from PIL import Image
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.convert_button import back_button, convertor_btn, get_pdf
from loader import dp, bot
from states.file_state import ImageTopdf


@dp.message_handler(Text(equals='Image ➡️ Pdf'))
async def bot_start_img_to_pdf(message: types.Message):
    await message.answer('📸 Rasm yuboring  men PDFga aylantiraman ', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Bot hozirgi holatida faqat 📸 rasm qabul qiladi!!!', reply_markup=back_button)
    await ImageTopdf.image.set()
    time.sleep(2)


@dp.message_handler(content_types='photo', state=ImageTopdf.image)
async def get_photo(msg: types.Message, state: FSMContext):
    global photo_name1
    photo_name1 = msg.photo[-1].file_unique_id
    photo_file_id = msg.photo[-1].file_id
    time.sleep(5)
    await bot.download_file_by_id(photo_file_id, destination=f'{photo_name1}')
    await state.finish()
    await msg.answer('✅ Rasm qabul qilindi... ', reply_markup=get_pdf)


@dp.message_handler(Text(equals='📃 PDFga aylantirish!'))
async def convert_to_text(msg: types.Message):
    photo_names = f'{photo_name1}.pdf'
    try:

        img = Image.open(photo_name1)
        save = img.convert('RGB')
        save.save(photo_names)
        time.sleep(1)
        with open(photo_names, 'rb') as file:
            await msg.answer_document(document=file, caption=photo_names, reply_markup=convertor_btn)
            time.sleep(1)
    except:
        await msg.answer('🚫 Rasm sifatini tekshiring !!!', reply_markup=ReplyKeyboardRemove())
        await msg.answer(text='orqaga', reply_markup=back_button)
    try:
        os.remove(photo_names)
        os.remove(photo_name1)
    except:
        pass
