import datetime
from datetime import date
import telebot
from telebot import types
bot = telebot.TeleBot('7188911878:AAFnoejmzi8IqQdDSkYDXsgS4zWQCEz7o_o')
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,"Ничем не могу помочь")

datee = date.today()
weeknumb = datee.isocalendar().week
weekdey = datee.weekday()
if (weeknumb%2 ==0 and (weekdey == 3 or weekdey == 5))or (weeknumb%2 ==1 and weekdey ==6) or weekdey ==1 or weekdey ==4:
    odd = 1
else:
    odd = 0
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'посуда' or message.text ==  'Посуда':
        if odd == 0:
            bot.send_message(message.chat.id, "Сегодня посудой занимается Вова")
        else:
            bot.send_message(message.chat.id, "Сегодня посудой занимается Наташа")
            
bot.infinity_polling()
