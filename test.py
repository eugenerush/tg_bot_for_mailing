from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telethon.sync import TelegramClient
import time

bot = Bot(token='1506036423:AAF98ww6EdcLGPt2qqkbsQJcoDfvoNxPuB8')
dp = Dispatcher(bot)

api_id = 1200079
api_hash = 'e278d876a0cfdca2dc7705e1ec2f9d55'
client = TelegramClient('name', api_id, api_hash)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Старт')


@dp.message_handler(commands=['text_send'])
async def process_text_send_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Text send')

    async def send():
        await client.send_message(-1001461743664, 'Test text send')

    async with client:
        client.loop.run_until_complete(send())


if __name__ == '__main__':
    executor.start_polling(dp)
