from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove, ContentTypes
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import datetime
import  sqlite3

from data.config import ADMINS

from states.users import Get_data_uz,Qoida_state
from states.en_state import Get_data_en
from states.ru_state import Get_data_ru
from states.adminstate import Admin

from keyboards.default.userskeydef import phone
from keyboards.default.userskeydef import roziman, accept, Prinimayu


from loader import dp, db



@dp.callback_query_handler(text='uz')
async def go_uz_lang(call: CallbackQuery):
    await call.message.answer(f'Siz o`bek tilini tanladingiz')
    await call.message.answer(f'Quyidagi qoidalar bilan tanishib chiqib maqul bo`lsa pastdagi tugmani bosing.\n'
                                  '1. qoida bir. \n'
                                  '2. Qoida ikki. \n'
                                  '3. Qoida uch. \n'
                                  '4. Qoida tort', reply_markup=roziman)
    await Qoida_state.qoida.set()
    await call.message.delete()

@dp.callback_query_handler(text='ru')
async def go_uz_lang(call: CallbackQuery):

    await call.message.answer(f'Вы выбрали русский')
    await call.message.answer(f'Прочтите правила ниже и нажмите кнопку ниже, если вы согласны.\n'
                              '1. правило одно.\n'
                              '2. Правило второе. \n'
                              '3. Правило третье \n'
                              '4. Правило четвертое', reply_markup=Prinimayu)
    await Qoida_state.qoida.set()
    await call.message.delete()

@dp.callback_query_handler(text='en')
async def go_uz_lang(call: CallbackQuery):

    await call.message.answer(f'You have chosen English')
    await call.message.answer(f'Прочтите правила ниже и нажмите кнопку ниже, если вы согласны.\n'
                              '1. Rule one.\n'
                              '2. Rule twoo. \n'
                              '3. Rule three \n'
                              '4. Rule four', reply_markup=accept)
    await Qoida_state.qoida.set()
    await call.message.delete()

@dp.message_handler(state=Qoida_state.qoida)
async def go_name(message: Message):
    text = message.text
    if text == 'Roziman':
        await message.answer(f'Ism familyangizni yuboring:',reply_markup=ReplyKeyboardRemove())
        await Get_data_uz.uz_name.set()
        await message.delete()
    elif text == 'Accept':
        await message.answer(f'Send your first and last name',reply_markup=ReplyKeyboardRemove())
        await Get_data_en.en_name.set()
        await message.delete()
    elif text == 'Prinimayu':
        await message.answer(f'Отправьте свое имя и фамилию',reply_markup=ReplyKeyboardRemove())
        await Get_data_ru.ru_name.set()
        await message.delete()


@dp.message_handler(state=Get_data_uz.uz_name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer('Telefon raqamingizni yuboring.\n'
                         'Namuna (+998) 90 1234567', reply_markup=phone)
    await Get_data_uz.phone_num.set()
    await message.delete()


@dp.message_handler(state=Get_data_uz.phone_num, content_types=ContentTypes.CONTACT)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {
            'phone': phone
        }
    )
    await message.answer('Manzilingizni kiriting',reply_markup=ReplyKeyboardRemove())
    await Get_data_uz.manzil.set()
    await message.delete()

@dp.message_handler(state=Get_data_uz.manzil)
async def get_phone(message: Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {
            'manzil': manzil
        }
    )

    await message.answer('Iltimos Savolingizni qisqa va tushunarli qilib yuboring.')
    await Get_data_uz.murojat.set()
    await message.delete()

chat_id = CallbackData('chek','id')

@dp.message_handler(state=Get_data_uz.murojat)
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
    await call.message.answer(f'Javobingizni kiriting: ')
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




