# import telebot
# from telebot import types
# bot = telebot.TeleBot('6331851978:AAHp0uXeq6H_UPYsxBm1jEClNKoaPtDJtYs')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     murkup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('go to site')
#     murkup.row(btn1)
#     btn2 = types.KeyboardButton('edit text')
#     btn3 = types.KeyboardButton('delete')
#     murkup.add(btn2, btn3)
#     file = open('./ItProgerTgBot.png', 'rb')
#     # file = open('./ItProgerTgBot.mp4', 'rb')
#     # bot.send_photo(message.chat.id, file, reply_markup=murkup)
#     # bot.send_video(message.chat.id, file, reply_markup=murkup)
#     #          audio
#     #          file = open('./ItProgerTgBot.mp3', 'rb')
#     #
#     #          ......
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'go to site':
#         bot.send_message(message.chat.id,'website is open')
#     elif message.text == 'delete':
#         bot.send_message(message.chat.id,'delited')
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     murkup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('go to site', url='https://google.com')
#     murkup.row(btn1)
#     btn2 = types.InlineKeyboardButton('edit text', callback_data='edit')
#     btn3 = types.InlineKeyboardButton('delete', callback_data='delete')
#     murkup.add(btn2, btn3)
#     bot.reply_to(message,'good photo', reply_markup=murkup )
#
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id,callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('edided text',callback.message.chat.id,callback.message.message_id)
# bot.polling(none_stop=True)