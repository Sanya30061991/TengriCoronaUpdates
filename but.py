from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

lang_button1 = KeyboardButton('Русский')
lang_button2 = KeyboardButton('English')

keyboarr = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboarr.add(lang_button1, lang_button2)
