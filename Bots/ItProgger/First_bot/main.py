# import telebot
# import webbrowser
#
# bot = telebot.TeleBot('6331851978:AAHp0uXeq6H_UPYsxBm1jEClNKoaPtDJtYs')
#
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://itproger.com')
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f"hello {message.from_user.first_name} {message.from_user.last_name}")
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>help</b> <em><u>information</u></em>', parse_mode='html')
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f"hello {message.from_user.first_name} {message.from_user.last_name}")
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f"ID: {message.from_user.id}")
#
#
# bot.polling(none_stop=True)
#
