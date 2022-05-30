from aiogram.dispatcher.filters.state import StatesGroup, State

class Admin(StatesGroup):
    admin = State()
    javob = State()

class Qoida(StatesGroup):
    qoida_uz = State()
    qoida_ru = State()
    qoida_en = State()