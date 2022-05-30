
from aiogram.dispatcher.filters.state import StatesGroup, State


class Get_data_ru(StatesGroup):
    ru_name = State()
    manzil_ru = State()
    phone_num_ru = State()
    murojat_ru = State()