import telebot
import key
from telebot import types

bot = telebot.TeleBot(key.token)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    start_keyboard = types.InlineKeyboardMarkup()
    PENTAGON = types.InlineKeyboardButton(text='Взлом Пентагона', callback_data='VP')
    LIFE = types.InlineKeyboardButton(text='Лайфхак', callback_data='HL')
    start_keyboard.add(PENTAGON, LIFE)
    bot.send_message(message.chat.id, "Выберай", reply_markup=start_keyboard)

@bot.callback_query_handler(func=lambda c: c.data)
def answer_callback(callback):
    if callback.data == "VP":
        start_keyboard = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Результат', url='https://www.defense.gov/')
        start_keyboard.add(btn_my_site)
        bot.send_message(callback.message.chat.id, "На те", reply_markup=start_keyboard)
    elif callback.data == 'LH':
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Результат', url='https://whoer.net/ru')
        markup.add(btn_my_site)
        bot.send_message(callback.message.chat.id, "Твоя жизнь взломана", reply_markup=markup)


# lol

bot.polling()
