from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

roziman = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Roziman')
        ]
    ]
)
roziman.resize_keyboard=True


Prinimayu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Prinimayu')
        ]
    ]
)
Prinimayu.resize_keyboard=True


accept = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Accept')
        ]
    ]
)
accept.resize_keyboard=True

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telfon raqamni ulashish',request_contact=True),
        ],
    ]
)

phone.resize_keyboard = True

murojat = ReplyKeyboardMarkup(
    keyboard=[ 
        [ 
            KeyboardButton('murojat'),
        ],
    ]
)

murojat.resize_keyboard = True



