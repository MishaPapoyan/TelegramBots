# import telebot
# from telebot import types
# import requests
# import json
#
# bot = telebot.TeleBot('6331851978:AAHJidKJI4WJVkDdPMcvR0IJA-Ap638YNfo')
# API = "https://restcountries.com/v2/all"
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,'hello write your city and know their capital')
#
# @bot.message_handler()
# def getCountriesCapital(message):
#     res = requests.get(f'https://restcountries.com/v2/name/{message.text}')
#     data = json.loads(res.text)
#     for country_name in data:
#         if message.text.capitalize().strip() == country_name['name']:
#             bot.send_message(message.chat.id,
#              f'The capital of {message.text.capitalize()} is {country_name["capital"]}.')
#             break
#         else:
#             bot.send_message(message.chat.id, 'Please enter a valid country name.')
#             break
#
#
# bot.polling(none_stop=True)
