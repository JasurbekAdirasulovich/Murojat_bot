from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove




from keyboards.inline.userskey import roziman

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):


    await dp.bot.send_message(message.from_user.id ,f'Salom {message.from_user.username} botga xush kelibsiz!\n')
    await dp.bot.send_message(message.from_user.id,f'Quyidagi qoidalar bilan tanishib chiqib maqul bo`lsa pastdagi tugmani bosing.\n'
                            '1. qoida bir. \n'
                            '2. Qoida ikki. \n'
                            '3. Qoida uch. \n'
                            '4. Qoida tort', reply_markup=roziman)
