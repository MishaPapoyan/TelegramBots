#
# from aiogram import Bot, Dispatcher, executor, types
# import requests
# import json
#
# apiKey = '711da8fa9d4bc079b8c66b00863926fa'
# key = '6331851978:AAHJidKJI4WJVkDdPMcvR0IJA-Ap638YNfo'
# bot = Bot(key)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def info(message: types.Message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Get weather', callback_data='city'))
#     markup.add(types.InlineKeyboardButton('commands list', callback_data='list'))
#     await message.reply('Hi here we know weather', reply_markup=markup)
#
#
# @dp.message_handler(commands='listCity')
# async def city_list(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add('London', 'Minsk', 'Mogilev')
#     await message.reply('Choose a city:', reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == 'list')
# async def callback_list(call: types.CallbackQuery):
#     await call.message.answer('/listCity\n/start')
#
#
# @dp.callback_query_handler(lambda c: c.data == 'city')
# async def callback_city(call: types.CallbackQuery):
#     await call.message.answer('Input city name')
#
#
# @dp.message_handler(lambda message: message.text.lower())
# async def get_weather(message: types.Message):
#     city = message.text.lower().strip()
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric'
#     res = requests.get(url)
#     print(res.status_code)
#
#     if res.status_code == 200:
#         data = json.loads(res.text)
#         temp = data['main']['temp']
#         humidity = data['main']['humidity']
#         pressure = data['main']['pressure']
#         wind_speed = data['wind']['speed']
#         desc = data['weather'][0]['description']
#         listEmoji = ['❄️', '🥵', '⛈️', '☁️', '⛅']
#         await message.reply(f'Weather in city {message.text}\n'
#                             f'temperature {temp} C {listEmoji[0]}\n'
#                             f'humidity {humidity}% {listEmoji[2]}\n'
#                             f'pressure {pressure} Pa\n'
#                             f'wind speed {wind_speed} m/s {listEmoji[2]}\n'
#                             f'description {desc}')
#     elif res.status_code != 200:
#         await message.answer('city doesnt have')
#     else:
#         await message.reply(f"City not found or error in fetching data")
#
#
# executor.start_polling(dp)
