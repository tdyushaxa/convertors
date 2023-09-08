import os
import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.convert_button import convertor_btn, convert_word, back_button
from loader import dp, bot
from states.file_state import FileStateWord
from utils.misc.convert_word_to_pdf import convert_to


@dp.message_handler(Text(equals='Word ➡️ PDF'))
async def bot_start(message: types.Message):
    await message.answer('📁 Word file yuboring...', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Bot hozirgi holatida faqat 📁 Document  qabul qiladi !', reply_markup=back_button)
    await FileStateWord.file.set()
    time.sleep(1)


@dp.message_handler(content_types='document', state=FileStateWord.file)
async def set_data_word(msg: types.Message, state: FSMContext):
    global file_name_2
    file_name = msg.document.file_name
    file_name_2 = file_name.split('.doc')[0]
    if file_name.endswith('.doc') or file_name.endswith('docx'):
        file_id = msg.document.file_id
        await bot.download_file_by_id(file_id=file_id, destination=f'{msg.from_user.id}.docx')
        await msg.answer('✅ File qabul qilindi', reply_markup=convert_word)
        await state.finish()
        time.sleep(1)
    else:
        await msg.answer('🙅‍ ️Faqat word filelar qabul qilinadi!!!', reply_markup=back_button)
        await msg.answer('📁 Word file yuboring')


@dp.message_handler(Text(equals='Convertor PDF'))
async def converter_to_word(msg: types.Message):
    try:
        await msg.answer('✏️ Word file PDF o\'zgarmoqda! Biroz kuting...')
        file_path = f'{msg.from_user.id}.docx'
        convert_to('convertor', file_path, timeout=5)
        time.sleep(1)
        pdf_file = f'convertor/{msg.from_user.id}.pdf'
        with open(pdf_file, 'rb') as file:
            await msg.answer_document(document=file, caption=file_name_2, reply_markup=ReplyKeyboardRemove())
            await msg.answer('✏️ File o\'zgartirldi!!!', reply_markup=convertor_btn)
            time.sleep(1)
        os.remove(file_path)
        os.remove(pdf_file)
    except:
        await msg.answer('🚫 Xatolik yuz berdi. Word file shifrlangan bo\'lishi mumkin!!!', reply_markup=convertor_btn)
