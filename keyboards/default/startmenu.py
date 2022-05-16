from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Menyu')
        ],
        [
            KeyboardButton('Biz Haqimizda'),
            KeyboardButton('Aloqa')
        ],
        [
            KeyboardButton('Ulashish')
        ]
    ]
)
start.resize_keyboard = True