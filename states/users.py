from aiogram.dispatcher.filters.state import State, StatesGroup


class Get_data_uz(StatesGroup):
    uz_name = State()
    name = State()
    manzil = State()
    phone_num = State()
    murojat = State()


class Qoida_state(StatesGroup):
    qoida = State()


