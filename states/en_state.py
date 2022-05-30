from aiogram.dispatcher.filters.state import StatesGroup,State


class Get_data_en(StatesGroup):
    en_name = State()
    manzil_en = State()
    phone_num_en = State()
    murojat_en = State()