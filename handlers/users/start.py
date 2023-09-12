from aiogram import types
from data.config import CHANNELS
from keyboards.default.convert_button import convertor_btn
from keyboards.inline.convertor_btns import check_button_subs
from loader import dp, db, bot
from utils.misc.check_subs import check


@dp.message_handler(commands=['start'],state='*')
async def show_channels(message: types.Message):
    id = message.from_user.id
    fullname = message.from_user.full_name
    try:
        db.add_user(id=id,name=fullname)
    except:
        pass
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button_subs,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, reply_markup=convertor_btn,disable_web_page_preview=True)

