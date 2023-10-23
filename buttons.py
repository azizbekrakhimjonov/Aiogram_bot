from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

r_btn = KeyboardButton('Random Number')
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(r_btn)


