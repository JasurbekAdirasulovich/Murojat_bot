from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
import datetime

from data.config import ADMINS

from states.users import Get_data_en

from keyboards.default.userskeydef import phone


from loader import dp



@dp.message_handler(state=Get_data_en.en_name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer('Send your phone number.\n'
                         'Example (+998) 90 1234567', reply_markup=phone)
    await Get_data_en.phone_num.set()


@dp.message_handler(state=Get_data_en.phone_num)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {
            'phone': phone
        }
    )
    await message.answer('Enter your address')
    await Get_data_en.manzil.set()


@dp.message_handler(state=Get_data_en.manzil)
async def get_phone(message: Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {
            'manzil': manzil
        }
    )

    await message.answer('Please send your question briefly and clearly.')
    await Get_data_en.murojat.set()


@dp.message_handler(state=Get_data_en.murojat)
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
        msg = f'<b><i>👤From whom:</i></b>  {FISH}\n\n' \
              f'<b><i>📱Phone:</i></b>  {FISH}\n\n' \
              f'<b><i>📍Address:</i></b>  {FISH}\n\n' \
              f'<b><i>⌚Time:</i></b>  <i>{sana} | {vaqt}</i>'

        return msg

    for admin in ADMINS:
        await dp.bot.send_message(admin, f'{send_data(data)}\n\n'
                                         f'\n<b><i>📌Message:</i></b>  {req}.')
