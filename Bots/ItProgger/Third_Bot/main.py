# import telebot
# from telebot import types
# import sqlite3
#
#
# bot = telebot.TeleBot('6331851978:AAHp0uXeq6H_UPYsxBm1jEClNKoaPtDJtYs')
# name = None
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('itprogger.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_incriment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Hi) now you registred ')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name (message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'choose password ')
#     bot.register_next_step_handler(message, user_pass)
#
#
# def user_pass (message):
#     password = message.text.strip()
#     conn = sqlite3.connect('itprogger.sql')
#     cur = conn.cursor()
#
#     cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Hi) now you registred ')
#     bot.register_next_step_handler(message, user_name)
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("user", callback_data='users'))
#     bot.send_message(message.chat.id, 'You registred', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     password = call.message.text.strip()
#     conn = sqlite3.connect('itprogger.sql')
#     cur = conn.cursor()
#
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#     info = ''
#     for el in users:
#         info += f"name {el[1]} password{el[2]}\n"
#     cur.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info)
#
#
#
#
#
#
#
# bot.polling(none_stop=True)