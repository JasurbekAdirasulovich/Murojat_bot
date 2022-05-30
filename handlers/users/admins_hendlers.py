
from aiogram.dispatcher import FSMContext

import datetime
import  sqlite3

from aiogram.types import Message, CallbackQuery

from keyboards.inline.adminkey import boshqaruv,settings



from states.adminstate import Admin
from states.adminstate import Qoida



from loader import dp, db



@dp.callback_query_handler(state = Admin.admin, text='xabarlar')
async def admin_state(call: CallbackQuery):
    await call.message.answer('Assalomu aleykum siz Xabarlar bo`limidasiz')
    now = datetime.datetime.now()
    now = str(now.date())
    items = db.select_all_post()
    i = 1
    msg1 = f'📬 #Xabarlar ro`yxati \n\n'
    for item in items:
        if item[2] == now:
            msg = (f'📌#{i}-xabar\n\n'
                                      f'🕵🏻FISH: {item[0]}\n\n'
                                      f'📅Sana: {item[2]}  {item[3]}\n\n'
                                      f'📩Xabar: {item[1]}\n\n\n')
            i+=1
            msg1 +=msg
    await call.message.answer(msg1,reply_markup=boshqaruv)








######################################################################################################################

##################################################################################################################################"""

@dp.callback_query_handler(state= Admin.admin, text='statistica')
async def admin_state(call: CallbackQuery):
    count_users = db.count_users()
    count_post = db.count_post()
    now = datetime.datetime.now()
    now = str(now.date())
    await call.message.answer(f'📅 Bugungi sana:\t {now}\n\n'
                              f'👥 Foydalanuvchilar soni:\t {count_users[0]}\n\n'
                              f'✍ Xabarlar soni:\t {count_post[0]}',reply_markup=boshqaruv)






#################################################################################################################

@dp.callback_query_handler(state= Admin.admin, text='qoida qosh')
async def admin_state(call: CallbackQuery):
    await call.message.answer('Assalomu aleykum siz qoidalarni sozlash bo`limidasiz',reply_markup=settings)

@dp.callback_query_handler(state= Admin.admin, text='qoida_uz')
async def admin_state(call: CallbackQuery):
    await call.message.answer('Qoidaning o`zbekchasini kiriting')
    await Qoida.qoida_uz.set()

@dp.message_handler(state=Qoida.qoida_uz)
async def qoida_uz(message: Message,state:FSMContext):
    qoida_uz = message.text
    await  state.update_data({
        'qoida_uz':qoida_uz
    })
    await message.answer("Siz qo`shgan qoida ro`yxatga olindi.",reply_markup=settings)
    await Admin.admin.set()

###########################################################################################################################
@dp.callback_query_handler(state= Admin.admin, text='qoida_ru')
async def admin_state(call: CallbackQuery):
    await call.message.answer('Введите русское правило\n'
                              'Qoidaning ruschasini kiriting')
    await Qoida.qoida_ru.set()


@dp.message_handler(state=Qoida.qoida_ru)
async def qoida_uz(message: Message,state:FSMContext):
    qoida_ru = message.text
    await  state.update_data({
        'qoida_ru': qoida_ru
    })
    await message.answer(f"Добавленное вами правило зарегистрировано.\n"
                         f"Siz qo`shgan qoida ro`yxatga olindi",reply_markup=settings)
    await Admin.admin.set()
#####################################################################################################

@dp.callback_query_handler(state= Admin.admin, text='qoida_en')
async def admin_state(call: CallbackQuery):
    await call.message.answer(f'Enter the English of the rule\n'
                              f'Qoidaning ingilischasini kiriting')
    await Qoida.qoida_en.set()


@dp.message_handler(state=Qoida.qoida_en)
async def qoida_uz(message: Message,state:FSMContext):
    qoida_en = message.text
    await  state.update_data({
        'qoida_en': qoida_en
    })
    await message.answer(f"The rule you added has been registered\n"
                         f"Siz qo`shgan qoida ro`yxatga olindi",reply_markup=settings)
    await Admin.admin.set()

    qoidalar = await state.get_data()
    Uzrule = qoidalar.get('qoida_uz')
    Rurule = qoidalar.get('qoida_ru')
    Enrule = qoidalar.get('qoida_en')
    try:
        db.add_pravila(Qoida_uz=Uzrule,Qoida_en=Enrule,Qoida_ru=Rurule)

    except sqlite3.IntegrityError as err:
        pass

    print(f'{Uzrule},{Rurule},{Enrule}')


#########################################################################################################

@dp.callback_query_handler(state= Admin.admin, text='qoida_del')
async def admin_state(call: CallbackQuery):
    await call.message.answer(f'Qoidalar o`chirildi.')


    await Admin.admin.set()







#########################################################################################################

@dp.callback_query_handler(state=Admin.admin, text='orqaga')
async def admin_state(call: CallbackQuery):
    await call.message.answer(f'Siz admin paneldasiz.',reply_markup=boshqaruv)










########################################################################################################



