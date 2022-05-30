
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData


from states.adminstate import Admin


from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove, ContentTypes
import datetime
import sqlite3

from data.config import ADMINS

from states.en_state import Get_data_en


from keyboards.default.userskeydef import phone


from loader import dp, db


@dp.message_handler(state=Get_data_en.en_name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer('Send your phone number.\n'
                         'Example (+998) 90 1234567', reply_markup=phone)
    await Get_data_en.phone_num_en.set()
    await message.delete()


@dp.message_handler(state=Get_data_en.phone_num_en,content_types=ContentTypes.CONTACT)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {
            'phone': phone
        }
    )
    await message.answer('Enter your address',reply_markup=ReplyKeyboardRemove())
    await Get_data_en.manzil_en.set()
    await message.delete()


@dp.message_handler(state=Get_data_en.manzil_en)
async def get_phone(message: Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {
            'manzil': manzil
        }
    )

    await message.answer('Please send your question briefly and clearly.')
    await Get_data_en.murojat_en.set()
    await message.delete()


chat_id = CallbackData('chek','id')

@dp.message_handler(state=Get_data_en.murojat_en)
async  def go_murojat(message: Message, state: FSMContext):
    req = message.text
    user_id = str(message.from_user.id)
    UserName = message.from_user.username
    await state.update_data({
        'req': req,
        'user_id': user_id,
        'UserName':UserName
    })

    data = await state.get_data()

    fish = data.get('name')
    tel = data.get('phone')
    manzil = data.get('manzil')
    userId = data.get('user_id')
    xabar = data.get('req')
    current_time = datetime.datetime.now()
    sana = str(current_time.date())
    vaqt = str(current_time.time())
    def send_data(data):
        fish = data.get('name')
        tel = data.get('phone')
        manzil = data.get('manzil')


        sana_vaqt = datetime.datetime.now()
        sana = sana_vaqt.date()
        vaqt = f'{sana_vaqt.hour}:{sana_vaqt.minute}:{sana_vaqt.second}'
        msg = f'<b><i>👤Kimdan:</i></b>  {fish}\n\n' \
              f'<b><i>📱Telfoni:</i></b>  {tel}\n\n' \
              f'<b><i>📍Manzili:</i></b>  {manzil}\n\n' \
              f'<b><i>⌚Vaqt:</i></b>  <i>{sana} | {vaqt}</i>'

        return msg


    javob = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Javob berish', callback_data= chat_id.new(id=user_id))
            ]

        ]
    )
    try:
        db.add_post(FISH=fish, tel_raqam=tel, manzil=manzil, userId=userId, xabar=xabar, sana=sana, vaqt=vaqt)
    except sqlite3.IntegrityError as err:
        print(err)

    for admin in ADMINS:
        await dp.bot.send_message(admin,f'{send_data(data)}\n\n'
                                        f'\n<b><i>📌Xabar:</i></b>  {req}.',reply_markup=javob)




@dp.callback_query_handler(chat_id.filter(), state=Admin.admin)
async def javob(call: CallbackQuery, callback_data: dict,state:FSMContext):

    user_id = int(callback_data.get('id'))
    await state.update_data({
        'user_id': user_id
    })
    await call.message.answer(f'Введите свой ответ: ')
    await Admin.javob.set()

@dp.message_handler(state=Admin.javob)
async def javobber(message: Message,state:FSMContext):
    javob = message.text

    await state.update_data({
        'javob':javob
    })
    otvet = await state.get_data()
    user_id = int(otvet.get('user_id'))

    await dp.bot.send_message(user_id,javob)
    await Admin.admin.set()


