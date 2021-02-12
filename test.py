from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


bot = Bot(token='1506036423:AAF98ww6EdcLGPt2qqkbsQJcoDfvoNxPuB8')
dp = Dispatcher(bot)
btn_start = KeyboardButton('Привет! 👋, Выбери, что ты хочешь сделать.')
btn_start_send = KeyboardButton('/start_send')
btn_stop_send = KeyboardButton('/stop_send')
btn_change = KeyboardButton('/change_text')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_start).add(btn_start_send, btn_stop_send)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Старт', reply_markup=greet_kb)


@dp.message_handler(commands=['start_send'])
async def process_start_send_command(message: types.Message):
    f = open('output.txt', 'r+')
    f.write('start_text_send')
    await bot.send_message(message.from_user.id, 'Рассылка вот-вот начнется', reply_markup=greet_kb)


@dp.message_handler(commands=['stop_send'])
async def process_stop_send_command(message: types.Message):
    f = open('output.txt', 'r+')
    f.write('stop_text_send')
    await bot.send_message(message.from_user.id, 'Рассылка становлена', reply_markup=greet_kb)


@dp.message_handler(commands=['change_text'])
async def process_change_command(message: types.Message):
    f = open('text.txt', 'r', encoding='utf-8')
    text = f.read()
    await bot.send_message(message.from_user.id, 'Отправь мне новый текст\n\tВот старый:\n' + text)
    f.write(message.text)


executor.start_polling(dp)
