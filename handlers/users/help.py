from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.file_state import FileState, FileStateWord, ImageTotext, ImageTopdf

from loader import dp


@dp.message_handler(CommandHelp(), state=FileState.file)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=FileStateWord.file)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=ImageTotext.image)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=ImageTopdf.image)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
