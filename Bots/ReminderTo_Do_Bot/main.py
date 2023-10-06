# import time
# import logging
# from aiogram import Bot, Dispatcher, executor, types
#
# logging.basicConfig(level=logging.INFO)
#
# TOKEN = '6538602048:AAFifl3v1lIwVHNflw_gdYtfV0Ornp4QLD8'
# MSG = 'do yo programm today and if you did which language is?'
# MSG_True = 'Thats good keep working'
# MSG_Bad = 'Thats bad!!!!'
# MSG_language = "yess its cool That's interesting! Keep up the good work."
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot=bot)
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#    user_id = message.from_user.id
#    user_name = message.from_user.first_name
#    user_full_name = message.from_user.full_name
#    logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")
#
#    await message.reply(f"Hi!! {user_full_name}")
#    await bot.send_message(user_id, MSG.format(user_name))
#
# @dp.message_handler(commands=['help'])
# async def start_handler(message: types.Message):
#    user_id = message.from_user.id
#    user_name = message.from_user.first_name
#    user_full_name = message.from_user.full_name
#    logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")
#
#    await message.reply(f"Hi!! {user_full_name} this bot is about remind you to programm, its 1 question `{MSG}` and you try answer that using program languages if yo did of corse ")
#
#
# @dp.message_handler(lambda message: 'yes' in message.text.lower())
# async def answer_handler(message: types.Message):
#    user_id = message.from_user.id
#    user_full_name = message.from_user.full_name
#    logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")
#    user_name = message.from_user.first_name
#
#    await bot.send_message(user_id, MSG_True.format(user_name))
#    response_text = message.text.lower()  # Convert user's response to lowercase for case-insensitive comparison
#    if 'python' not in response_text:
#        await message.reply('thats also cool but try learn python')
#    else:
#        await message.reply(f"{MSG_language} ")
#
# @dp.message_handler(lambda message: 'no' in message.text.lower())
# async def answer_handler(message: types.Message):
#    user_id = message.from_user.id
#    user_full_name = message.from_user.full_name
#    logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")
#    user_name = message.from_user.first_name
#
#    await bot.send_message(user_id, MSG_Bad.format(user_name))
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
