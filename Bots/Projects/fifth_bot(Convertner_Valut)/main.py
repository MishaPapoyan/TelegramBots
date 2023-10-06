# import telebot
# from telebot import types
# from  currency_converter import CurrencyConverter
#
# bot = telebot.TeleBot('6331851978:AAHJidKJI4WJVkDdPMcvR0IJA-Ap638YNfo')
# currency = CurrencyConverter()
# API = "https://restcountries.com/v2/all"
# amount = 0
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'input price')
#     bot.register_next_step_handler(message,summa)
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'input only number')
#         return
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
#         btn4 = types.InlineKeyboardButton('other', callback_data='else')
#
#         markup.add(btn1,btn2,btn3,btn4)
#         bot.send_message(message.chat.id, "choose valuta",reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'input only positive number')
#         bot.register_next_step_handler(message, summa)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f"{round(res, 2)}.")
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, 'write your valut in thar xyz/zyx')
#         bot.register_next_step_handler(call.message, my_currency)
#
#
# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f"{round(res, 2)}.")
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, 'write your valut in thar xyz/zyx')
#         bot.register_next_step_handler(message, my_currency)
#
# bot.polling(none_stop=True)