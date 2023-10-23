from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('Python')
btn2 = KeyboardButton('Java')
btn3 = KeyboardButton('JavaScript')
btn4 = KeyboardButton('C++')
btn5 = KeyboardButton('C#')
menu = (ReplyKeyboardMarkup(resize_keyboard=True)
        .add(btn1, btn2).add(btn3).add(btn4, btn5))


