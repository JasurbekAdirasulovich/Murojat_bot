from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
import datetime

from data.config import ADMINS

from states.users import Get_data_ru

from keyboards.default.userskeydef import phone
from keyboards.inline.userskey import lang

from loader import dp





@dp.message_handler(state=Get_data_ru.ru_name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer('Отправьте свой номер телефона.\n'
                         'Например (+998) 90 1234567', reply_markup=phone)
    await Get_data_ru.phone_num.set()


@dp.message_handler(state=Get_data_ru.phone_num)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {
            'phone': phone
        }
    )
    await message.answer('Введите свой адрес')
    await Get_data_ru.manzil.set()


@dp.message_handler(state=Get_data_ru.manzil)
async def get_phone(message: Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {
            'manzil': manzil
        }
    )

    await message.answer('Пожалуйста, присылайте свой вопрос кратко и четко.')
    await Get_data_ru.murojat.set()


@dp.message_handler(state=Get_data_ru.murojat)
async def go_murojat(message: Message, state: FSMContext):
    req = message.text
    user_id = message.from_user.id
    await state.update_data({
        'req': req,
        'user_id': user_id
    })

    data = await state.get_data()

    def send_data(data):
        FISH = data.get('name')
        tel = data.get('phone')
        manzil = data.get('manzil')
        user_id = data.get('user_id')
        sana_vaqt = datetime.datetime.now()
        sana = sana_vaqt.date()
        vaqt = f'{sana_vaqt.hour}:{sana_vaqt.minute}:{sana_vaqt.second}'
        msg = f'<b><i>👤Kто:</i></b>  {FISH}\n\n' \
              f'<b><i>📱Телефон:</i></b>  {FISH}\n\n' \
              f'<b><i>📍Адрес:</i></b>  {FISH}\n\n' \
              f'<b><i>⌚Время:</i></b>  <i>{sana} | {vaqt}</i>'

        return msg

    for admin in ADMINS:
        await dp.bot.send_message(admin, f'{send_data(data)}\n\n'
                                         f'\n<b><i>📌Сообщение:</i></b>  {req}.')
