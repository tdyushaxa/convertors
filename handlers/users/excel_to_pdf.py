import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.convert_button import back_button, convertor_btn, ex_pdf_conv
from loader import dp, bot
from states.file_state import Excel_to_pdf_state
from utils.misc.excel_to_pdf import excel_to_pdf


@dp.message_handler(Text(equals='Excel ➡️ PDF'))
async def bot_start(message: types.Message):
    a = message.chat.id
    await message.answer('📃 <b>Excel file yuboring...</b> ', reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')
    await message.answer(text='Bot hozirgi holatida faqat 📃 Document qabul qiladi !', reply_markup=back_button,
                         parse_mode='HTML')
    await Excel_to_pdf_state.file.set()


@dp.message_handler(content_types='document', state=Excel_to_pdf_state.file)
async def set_data(msg: types.Message, state: FSMContext):
    global file_name_5
    file_name = msg.document.file_name
    file_name_5 = file_name.split('.')[0]
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        fil_id = msg.document.file_id
        await bot.download_file_by_id(file_id=fil_id, destination=f'{msg.from_user.id}.xlsx')
        await msg.answer('👌 File qabul qilindi', reply_markup=ex_pdf_conv)
        await state.finish()
    else:
        await msg.answer('🚫 <b>Faqat Excel .xlsx, .xls formatdagi filelar qabul qilinadi</b>', reply_markup=back_button,
                         parse_mode='HTML')
        await msg.answer(' 📃 Excel file yuboring')
        await Excel_to_pdf_state.file.set()


@dp.message_handler(Text(equals='Converor Pdf'))
async def converter_to_word(msg: types.Message):
    excel_file = f'{msg.from_user.id}.xlsx'
    pdf_file = f'{msg.from_user.id}.pdf'
    try:
        output = excel_to_pdf(excel_file, pdf_file)
        with open(pdf_file, 'rb') as file:
            await msg.answer_document(file, caption=file_name_5, reply_markup=ReplyKeyboardRemove())
    except:
        await msg.answer('🙅‍♂️ Xatolik yuz berdi file bilan  qaytadan urunib ko\'ring', reply_markup=convertor_btn)
    try:
        os.remove(excel_file)
        os.remove(pdf_file)
    except:
        pass
