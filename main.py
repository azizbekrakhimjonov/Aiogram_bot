import logging
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from config import token
from buttons import menu

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Assalomu aleykum botga hush kelibsiz', reply_markup=menu)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Random Number':
        await message.answer(f"{randint(1, 100)}")
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
