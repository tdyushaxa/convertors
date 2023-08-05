import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import ReplyKeyboardRemove
from pdf2docx import Converter
from keyboards.default.convert_button import convertor_btn, convertor, back_button, get_text, get_pdf, \
    convert_word
from loader import dp, bot
from states.file_state import FileState, FileStateWord, ImageTotext, ImageTopdf
from PIL import Image
from pytesseract import pytesseract

from utils.misc.convert_word_to_pdf import convert_to


@dp.message_handler(Text(equals='PDF ➡️ Word'))
async def bot_start(message: types.Message):
    await message.answer('📃 <b>Pdf file yuboring...</b> ', reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
    await message.answer(text='Bot hozirgi holatida faqat 📃 Document qabul qiladi !', reply_markup=back_button,
                         parse_mode='HTML')
    await FileState.file.set()


@dp.message_handler(Text(equals='🔙 ortga'), state=FileState.file)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Ortgaa ', reply_markup=convertor_btn)


@dp.message_handler(Text(equals='🔙 ortga'), state=FileStateWord.file)
async def bot_start_word(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Ortgaa ', reply_markup=convertor_btn)


@dp.message_handler(Text(equals='🔙 ortga'), state=ImageTotext.image)
async def bot_start_image(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Ortgaa ', reply_markup=convertor_btn)


@dp.message_handler(Text(equals='🔙 ortga'))
async def bot_start_word(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Ortga ', reply_markup=convertor_btn)


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
        docx_file = f'{file_name_1}.docx'
        with open(docx_file, 'rb') as file:
            await msg.answer_document(document=file, caption=file_name_1, reply_markup=ReplyKeyboardRemove())
            await msg.answer('✏️ <b>File o\'zgartirldi</b>', reply_markup=convertor_btn)
        os.remove(file_path)
        os.remove(docx_file)
    except:
        await msg.answer('🙅‍♂️ Xatolik yuz berdi file bilan  qaytadan urunib ko\'ring', reply_markup=convertor_btn)


@dp.message_handler(Text(equals='Word ➡️ PDF'))
async def bot_start(message: types.Message):
    await message.answer('📁 Word file yuboring...', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Bot hozirgi holatida faqat 📁 Document  qabul qiladi !', reply_markup=back_button)
    await FileStateWord.file.set()


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
    else:
        await msg.answer('🙅‍ ️Faqat word filelar qabul qilinadi!!!', reply_markup=back_button)
        await msg.answer('📁 Word file yuboring')


@dp.message_handler(Text(equals='Convertor PDF'))
async def converter_to_word(msg: types.Message):
    try:
        await msg.answer('✏️ Word file PDF o\'zgarmoqda! Biroz kuting...')
        file_path = f'{msg.from_user.id}.docx'

        convert_to('convertor', file_path, timeout=15)
        pdf_file = f'convertor/{msg.from_user.id}.pdf'

        with open(pdf_file, 'rb') as file:
            await msg.answer_document(document=file, caption=file_name_2, reply_markup=ReplyKeyboardRemove())
            await msg.answer('✏️ File o\'zgartirldi!!!', reply_markup=convertor_btn)
        os.remove(file_path)
        os.remove(pdf_file)
    except:
        await msg.answer('🚫 Xatolik yuz berdi. Word file shifrlangan bo\'lishi mumkin!!!', reply_markup=convertor_btn)


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
    except:
        await msg.answer('🚫 Rasm sifatini tekshiring !!!', reply_markup=ReplyKeyboardRemove())
        await msg.answer(text='orqaga', reply_markup=back_button)
    os.remove(photo_name)


@dp.message_handler(Text(equals='Image ➡️ Pdf'))
async def bot_start_img_to_pdf(message: types.Message):
    await message.answer('📸 Rasm yuboring  men PDFga aylantiraman ', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Bot hozirgi holatida faqat 📸 rasm qabul qiladi!!!', reply_markup=back_button)
    await ImageTopdf.image.set()


@dp.message_handler(content_types='photo', state=ImageTopdf.image)
async def get_photo(msg: types.Message, state: FSMContext):
    global photo_name1
    photo_name1 = msg.photo[-1].file_unique_id
    photo_file_id = msg.photo[-1].file_id
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
        with open(photo_names, 'rb') as file:
            await msg.answer_document(document=file, caption=photo_names, reply_markup=convertor_btn)
    except:
        await msg.answer('🚫 Rasm sifatini tekshiring !!!', reply_markup=ReplyKeyboardRemove())
        await msg.answer(text='orqaga', reply_markup=back_button)
    os.remove(photo_names)
    os.remove(photo_name1)
