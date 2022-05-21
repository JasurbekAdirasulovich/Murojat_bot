import logging

from aiogram import Dispatcher

from data.config import ADMINS

from keyboards.inline.adminkey import admin_go

from states.adminstate import Admin


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi",reply_markup=admin_go)
        except Exception as err:
            logging.exception(err)
