from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message

from loader import dp

import requests

import requests

def valyuta_qaytar(valyuta):
    key = '6c9d958658b4362577022680'
    # Where USD is the base currency you want to use
    url = f'https://v6.exchangerate-api.com/v6/{key}/latest/{valyuta}'

    # Making our request
    response = requests.get(url)
    data = response.json()
    data1 = data["conversion_rates"]["UZS"]
    data2 = data1//1
    return data2

@dp.message_handler(text = 'USD-UZS')
async def uzs_qaytar1(message: Message):
    data3 = valyuta_qaytar('USD')
    await message.answer(f'1 dollar {data3} so`mga teng')

@dp.message_handler(text = 'RUB-UZS')
async def uzs_qaytar1(message: Message):
    data3 = valyuta_qaytar('RUB')
    await message.answer(f'1 Rubl {data3} so`mga teng')


@dp.message_handler(text = 'EUR-UZS')
async def uzs_qaytar1(message: Message):
    data3 = valyuta_qaytar('EUR')
    await message.answer(f'1 yevro {data3} so`mga teng')

@dp.message_handler(text = 'TENGE-UZS')
async def uzs_qaytar1(message: Message):
    data3 = valyuta_qaytar('KZT')
    await message.answer(f'1 tenge {data3} so`mga teng')

