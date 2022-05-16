from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menyu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('USD-UZS'),
            KeyboardButton('RUB-UZS')
        ],
        [
            KeyboardButton('EUR-UZS'),
            KeyboardButton('TENGE-UZS')
        ],
        [
            KeyboardButton('Orqaga'),
            KeyboardButton('Yopish')

        ]
    ]
)
menyu.resize_keyboard = True