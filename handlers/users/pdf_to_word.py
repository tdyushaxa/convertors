import os
import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from pdf2docx import Converter

from keyboards.default.convert_button import back_button, convertor, convertor_btn
from loader import dp, bot
from states.file_state import FileState


@dp.message_handler(Text(equals='PDF ➡️ Word'))
async def bot_start(message: types.Message):
    a = message.chat.id
    await message.answer('📃 <b>Pdf file yuboring...</b> ', reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
    await message.answer(text='Bot hozirgi holatida faqat 📃 Document qabul qiladi !', reply_markup=back_button,
                         parse_mode='HTML')

    await FileState.file.set()
    time.sleep(2)






@dp.message_handler(content_types='document', state=FileState.file)
async def set_data(msg: types.Message, state: FSMContext):
    global file_name_1
    file_name = msg.document.file_name
    file_name_1 = file_name.split('.pdf')[0]
    if file_name.endswith('.pdf'):
        fil_id = msg.document.file_id
        await bot.download_file_by_id(file_id=fil_id, destination=f'{msg.from_user.id}.pdf')
        await msg.answer('👌 File qabul qilindi', reply_markup=convertor)
        await state.finish()
        time.sleep(3)
    else:
        await msg.answer('🚫 <b>Faqat PDF filelar qabul qilinadi</b>', reply_markup=back_button, parse_mode='HTML')
        await msg.answer(' 📃 Pdf file yuboring')


@dp.message_handler(Text(equals='️️️️️️️️️️️Convertor'))
async def converter_to_word(msg: types.Message):
    try:
        await msg.answer('<b>PDF file wordga o\'zgarmoqda! Biroz kuting...</b>', parse_mode="HTML")
        file_path = f'{msg.from_user.id}.pdf'
        cv = Converter(file_path)
        cv.convert(f'{file_name_1}.docx')
        cv.close()
        time.sleep(2)
        docx_file = f'{file_name_1}.docx'
        with open(docx_file, 'rb') as file:
            await msg.answer_document(document=file, caption=file_name_1, reply_markup=ReplyKeyboardRemove())
            await msg.answer('✏️ <b>File o\'zgartirldi</b>', reply_markup=convertor_btn)
            time.sleep(1)
        os.remove(file_path)
        os.remove(docx_file)
    except:
        await msg.answer('🙅‍♂️ Xatolik yuz berdi file bilan  qaytadan urunib ko\'ring', reply_markup=convertor_btn)

