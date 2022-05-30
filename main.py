from aiogram import executor
import  sqlite3
from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    try:
        db.create_table_message()
    except Exception as err:
        print(err)


    try:
        db.create_table_pravila()
    except Exception as err:
        print(err)

    try:
        db.add_pravila(Qoida_uz='Savol yoki murojat qisqa va lo`nda bo`lsin', Qoida_en='The question or appeal should be short and concise', Qoida_ru='Вопрос или обращение должны быть краткими и лаконичными.')
    except sqlite3.IntegrityError as err:
        print(err)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
