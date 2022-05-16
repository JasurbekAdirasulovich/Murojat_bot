from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command,Text
from keyboards.default.startmenu import start
from keyboards.default.elementmenu import menyu

from loader import dp

@dp.message_handler(text = 'Menyu')
async def back_menyu(message: Message):
    await message.answer('Valyutalarni tanlang:',reply_markup=menyu)


@dp.message_handler(text = 'Biz Haqimizda')
async def back_menyu(message: Message):
    await message.answer('Biz bu botni yaxshi niyatda odamlarning ishini yengillashtirish va qulaylik yaratish uchun yaratdik.'
                         'Bizning jamoamiz mendan tashkil topgan 😅😅😅. Mening ismim Jasurbek. Men 1999-yil Surxondaryo viloyatida tug`ulganman. Hozir talabaman. Qiziqishlarim `Dasturlash`, `Qo`shiq hirgoyi qilish`, `Multfilm tomosha qilish` va hakozalar')


@dp.message_handler(text = 'Aloqa')
async def back_menyu(message: Message):
    await message.answer(f"@Jasurbekakam     @jascoderuz")


@dp.message_handler(text = 'Ulashish')
async def back_menyu(message: Message):
    await message.answer("Ulashish uchun havolamiz: @ValyutalarUZS_bot")

@dp.message_handler(text = 'Orqaga')
async def start_menuga(message: Message):
    await message.answer('Bosh menyuga qaytdingiz:',reply_markup=start)

@dp.message_handler(text = 'Yopish')
async def start_menuga(message: Message):
    await message.answer('Siz enyuni yopib qo`ydingiz. unga qaytish uchun /menyu buyrug`ini bosing',reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands='menyu')
async def start_menuga(message: Message):
    await message.answer('Qoyil siz yana menyuga qaytdingiz. Valyutani tanlang:',reply_markup=menyu)


