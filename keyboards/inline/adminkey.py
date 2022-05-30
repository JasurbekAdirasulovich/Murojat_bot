from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

admin_go = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Admin panelga o`tish",callback_data='admin')
        ]
    ]
)

boshqaruv = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xabarlar', callback_data='xabarlar'),
            InlineKeyboardButton(text='Statistica',callback_data='statistica'),
        ],
        [
            InlineKeyboardButton(text='Qoidalarni qo`shish', callback_data='qoida qosh')
        ]
    ]
)




settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 Qoidaning O`zbekchasi:',callback_data='qoida_uz'),
            InlineKeyboardButton(text='🇷🇺 Qoidaning ruschasi',callback_data='qoida_ru'),
        ],
        [
            InlineKeyboardButton(text='🇺🇸Qoidani ingilischasi',callback_data='qoida_en'),
            InlineKeyboardButton(text='🗑Qoidani o`chirish',callback_data='qoida_del')
        ],
        [
            InlineKeyboardButton(text='🔙 Orqaga', callback_data='orqaga')
        ]
    ]
)