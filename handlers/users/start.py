from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.convert_button import convertor_btn
from loader import dp, db

from states.file_state import FileState, FileStateWord, ImageTotext, ImageTopdf


@dp.message_handler(CommandStart(), state=FileState.file)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=convertor_btn)


@dp.message_handler(CommandStart(), state=FileStateWord.file)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=convertor_btn)


@dp.message_handler(CommandStart(), state=ImageTotext.image)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=convertor_btn)


@dp.message_handler(CommandStart(), state=ImageTopdf.image)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=convertor_btn)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    fullname = message.from_user.full_name
    try:
        db.add_user(id=id, name=fullname)
    except:
        pass

    await message.answer(f"Salom, {fullname}!", reply_markup=convertor_btn)
