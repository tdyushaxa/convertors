import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from pikepdf import Name, PdfImage, Pdf

from keyboards.default.convert_button import back_button, get_images_key, convertor_btn
from loader import dp, bot
from states.file_state import ImageToGet_text


@dp.message_handler(Text(equals='PDF ➡️ Get image'))
async def get_images(msg: types.Message):
    await ImageToGet_text.file.set()
    await msg.answer('<b>📃 PDF file yuboring! Men sizga PDF filedan rasmlarni olib beraman.</b>')
    await msg.answer(text='Bot hozirgi holatida faqat 📃 PDF  qabul qiladi!!!', reply_markup=back_button)


@dp.message_handler(content_types='document', state=ImageToGet_text.file)
async def set_images(msg: types.Message, state: FSMContext):
    file_name = msg.document.file_name
    file_name_3 = file_name.split('.pdf')[0]
    try:
        if file_name.endswith('.pdf'):
            file_id = msg.document.file_id
            await bot.download_file_by_id(file_id=file_id, destination=f'{msg.from_user.id}.pdf')
            await msg.answer('✅ File qabul qilindi', reply_markup=get_images_key)
            await state.finish()
        else:
            await msg.answer('🙅‍ ️Faqat PDF filelar qabul qilinadi!!!', reply_markup=back_button)
            await msg.answer('📁 Word file yuboring')
    except:
        await msg.answer('<b>🚫 FIle hajmi katta yoki File bilan muammo bor!!</b>', reply_markup=ReplyKeyboardRemove())
        await msg.answer(text='orqaga', reply_markup=back_button)


@dp.message_handler(Text(equals='Get Image'))
async def converter_get_image(msg: types.Message):
    await msg.answer('✏️ Rasmlarni yuklab olinmoqda! Biroz kuting...')
    file_path = f'{msg.from_user.id}.pdf'
    try:
        pdf_page = Pdf.open(file_path)
        for page in pdf_page.pages:
            for image in page.images.keys():
                raw_image = page.images[image]
                pdf_image = PdfImage(raw_image)
                pdf_get_image = pdf_image.extract_to(fileprefix=f"{msg.chat.id}")
                with open(f'{msg.chat.id}.jpg', 'rb') as file:
                    await msg.answer_photo(file, caption=pdf_page.filename, reply_markup=ReplyKeyboardRemove())
        await msg.answer('📷 Rasmlar jo\'natildi', reply_markup=convertor_btn)

    except:
        await msg.answer('<b>🚫 FIle hajmi katta yoki File bilan muammo bor!!</b>', reply_markup=ReplyKeyboardRemove())
        await msg.answer(text='orqaga', reply_markup=back_button)
    try:
         os.remove(file_path)
         os.remove(f"{msg.chat.id}.jpg")
         os.remove(f"{msg.chat.id}.png")
    except:
         pass
