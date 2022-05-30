from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandStart




import sqlite3




from keyboards.inline.userskey import lang

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):


    await message.answer(f'Salom {message.from_user.username} botga xush kelibsiz!\n')
    await message.answer(f'Choose one of the languages\n'
                              f'Tillardan birini tanlang\n'
                              f'\nВыберите один из языков',reply_markup=lang)

    username = message.from_user.username
    userid = message.from_user.id

    try:
        db.add_user(Username=username, UserId=userid)
    except sqlite3.IntegrityError as err:
        pass
