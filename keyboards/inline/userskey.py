from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


lang = InlineKeyboardMarkup(
    inline_keyboard= [

            [
                InlineKeyboardButton(text = 'en', callback_data='en'),
                InlineKeyboardButton(text = 'uz', callback_data='uz'),
                InlineKeyboardButton(text = 'ru', callback_data='ru')
            ]

        ]
)

