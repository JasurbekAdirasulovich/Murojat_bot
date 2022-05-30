from aiogram import types
from data.config import ADMINS

from states.adminstate import Admin

from keyboards.inline.adminkey import boshqaruv



from loader import dp, db

@dp.message_handler(chat_id = ADMINS , commands='start')
async def bot_admin(message: types.Message):
    await message.answer('Salom Admin botga xush kelibsiz...',reply_markup=boshqaruv)
    await Admin.admin.set()
