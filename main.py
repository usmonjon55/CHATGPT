import logging

from aiogram import Bot, Dispatcher, executor, types
from test import new_text

API_TOKEN = '6290512650:AAEseEyo-5CEI4cZWspRvrl691n8PsxBJIU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom")



@dp.message_handler()
async def echo(message: types.Message):
    javob = new_text(message.text)
    await message.answer(javob)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)