# import telebot
# from telebot import types
# import requests
# import json
#
# bot = telebot.TeleBot('6331851978:AAHJidKJI4WJVkDdPMcvR0IJA-Ap638YNfo')
# API = '711da8fa9d4bc079b8c66b00863926fa'
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'say City')
# #
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     if res.status_code == 200:
#         print(res.status_code)
#         data = json.loads(res.text)
#         feels_like = data['main']['feels_like']
#         temp_min = data['main']['temp_min']
#         temp_max = data['main']['temp_max']
#         pressure = data['main']['pressure']
#         humidity = data['main']['humidity']
#         wind_speed = data['wind']['speed']
#         description = data['weather'][0]['description']
#         icon = data['weather'][0]['icon']
#         city_name = data['name']
#         bot.reply_to(message, f'in city \t `{city_name}` \n'
#                                    f"temperature = {temp_max} \n"
#                                    f'pressure = {pressure} \n'
#                                    f'humidity = {humidity} \n'
#                                    f'wind speed = {wind_speed} m/s')
#
#     else:
#         bot.send_message(message.chat.id, 'City doesn\'t exist')
#
#
# bot.polling(none_stop=True)