import telebot
from telebot import types


bot = telebot.TeleBot("1573024390:AAE_pgyDydpY2OpE1b8Uc0OzQy0S05xRb5c")


@bot.message_handler(commands=['start'])
def start(message):
    bt = types.InlineKeyboardMarkup()
    send = types.InlineKeyboardButton(text='Начать рассылку')
    bt.add(send)
    bot.send_message(message.chat.id, 'Нажми на кнопку и рассылка начнется через пару секунд', reply_markup=bt)


bot.polling()
