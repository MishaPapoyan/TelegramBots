import telebot
from telebot import types

bot = telebot.TeleBot('6331851978:AAHJidKJI4WJVkDdPMcvR0IJA-Ap638YNfo')

# about football
messi = open('./images/messi.jpg', 'rb')
ronaldinho = open('./images/ronaldinho.jpg', 'rb')
neymar = open('./images/neymar.jpg', 'rb')

aguero = open('./images/aguero.jpg', 'rb')
tevez = open('./images/tevez.jpg', 'rb')
deBruyne = open('./images/deBruyne.jpg', 'rb')


suares = open('./images/suares.jpeg', 'rb')
gerrard = open('./images/gerrard.jpg', 'rb')
torres = open('./images/Torres.jpg', 'rb')
# ------------------------------------------------------

# about cars
bmw = open('./images/bmwM5.jpg', 'rb')
audi = open('./images/audi.jpg', 'rb')
porche = open('./images/porche.jpg', 'rb')

# functions

def show_interests(message):
    markup = types.InlineKeyboardMarkup()
    # adding buttons
    btn_football = types.InlineKeyboardButton('Football', callback_data='show_teams')
    btn_cars = types.InlineKeyboardButton('Cars', callback_data='show_cars')

    markup.add(btn_football,btn_cars)

    bot.send_message(message, "Choose your interest:", reply_markup=markup)

def show_teams(message):
    markup = types.InlineKeyboardMarkup()
    # adding buttons
    btn_team1 = types.InlineKeyboardButton('Barcelona', callback_data='show_Barcelona_games')
    btn_team2 = types.InlineKeyboardButton('Manchester City', callback_data='show_City_games')
    btn_team3 = types.InlineKeyboardButton('Liverpool', callback_data='show_liverpool_Footballers')

    markup.add(btn_team1, btn_team2, btn_team3)
    bot.send_message(message, "Choose your favorite team:", reply_markup=markup)





def show_cars(message):
    markup = types.InlineKeyboardMarkup()
    # adding buttons
    btn_car1 = types.InlineKeyboardButton('BMW', callback_data='show_bmw')
    btn_car2 = types.InlineKeyboardButton('AUDI', callback_data='show_audi')
    btn_car3 = types.InlineKeyboardButton('PORCHE', callback_data='show_porche')

    markup.add(btn_car1, btn_car2, btn_car3)
    bot.send_message(message, "Choose your favorite car:", reply_markup=markup)



def show_Barcelona_Footballers(message):
    markup = types.InlineKeyboardMarkup()
    # adding buttons
    # fotballer1 = types.InlineKeyboardButton('Messi', callback_data='show_messi_photo')
    fotballer1 = types.InlineKeyboardButton('Messi', callback_data='show_messi_photo')
    fotballer2 = types.InlineKeyboardButton('Ronaldinho', callback_data='show_ronaldinho_photo')
    fotballer3 = types.InlineKeyboardButton('Neymar', callback_data='show_neymar_photo')

    markup.add(fotballer1, fotballer2, fotballer3)
    bot.send_message(message, " which match do yo think are the best", reply_markup=markup)


def show_City_Footballers(message):
    markup = types.InlineKeyboardMarkup()
    # adding buttons
    fotballer1 = types.InlineKeyboardButton('Aguero', callback_data='show_aguero_photo')
    fotballer2 = types.InlineKeyboardButton('Teves', callback_data='show_teves_photo')
    fotballer3 = types.InlineKeyboardButton('De Bruyne', callback_data='show_deBruyne_photo')

    markup.add(fotballer1, fotballer2, fotballer3)
    bot.send_message(message, " which match do yo think are the best", reply_markup=markup)


def show_ronaldinho_photo(message):
    bot.send_message(message, 'you choise ronaldinho')
    bot.send_photo(message, ronaldinho)

def show_messi_photo(message):
    bot.send_message(message, 'you choise messi')
    bot.send_photo(message, messi)
def show_neymar_photo(message):
    bot.send_message(message, 'you choise neymar')
    bot.send_photo(message, neymar)


def show_aguero_photo(message):
    bot.send_message(message, 'you choise Aguero')
    bot.send_photo(message, aguero)

def show_tevez_photo(message):
    bot.send_message(message, 'you choise Tevez')
    bot.send_photo(message, tevez)

def show_deBruye_photo(message):
    bot.send_message(message, 'you choise De Bruyne')
    bot.send_photo(message, deBruyne)


def show_gerrard_photo(message):
    bot.send_message(message, 'you choise gerrard')
    bot.send_photo(message, gerrard)

def show_torres_photo(message):
    bot.send_message(message, 'you choise Torres')
    bot.send_photo(message, torres)

def show_suares_photo(message):
    bot.send_message(message, 'you choise Suares')
    bot.send_photo(message, suares)

def show_bmw(message):
    bot.send_message(message, 'you choise BMW')
    bot.send_photo(message, bmw)

def show_audi(message):
    bot.send_message(message, 'you choise AUDI')
    bot.send_photo(message, audi)

def show_porche(message):
    bot.send_message(message, 'you choise PORCHE')
    bot.send_photo(message, porche)
def show_Liverpool_Footballers(message):
    markup = types.InlineKeyboardMarkup()
    # adding buttons
    fotballer1 = types.InlineKeyboardButton('Gerrard', callback_data='show_gerrard_photo')
    fotballer2 = types.InlineKeyboardButton('Torres', callback_data='show_torres_photo')
    fotballer3 = types.InlineKeyboardButton('Suares', callback_data='show_suares_photo')

    markup.add(fotballer1, fotballer2, fotballer3)
    bot.send_message(message, " which match do yo think are the best", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    message = call.message.chat.id
    if call.data == 'show_teams':
        bot.send_message(message, "You chose Football.")
        show_teams(message)
    elif call.data == 'show_cars':
        bot.send_message(message, "You chose Cars.")
        show_cars(message)
    elif call.data == 'show_bmw':
        show_bmw(message)
    elif call.data == 'show_audi':
        show_audi(message)
    elif call.data == 'show_porche':
        show_porche(message)
    elif call.data == 'show_programmers':
        bot.send_message(message, "You chose Programming.")
        # show_programmers(message)
    elif call.data == 'show_Barcelona_games':
        show_Barcelona_Footballers(message)
    elif call.data == 'show_City_games':
        show_City_Footballers(message)
    elif call.data == 'show_liverpool_Footballers':
        show_Liverpool_Footballers(message)
    elif call.data == 'show_messi_photo':
        show_messi_photo(message)
    elif call.data == 'show_ronaldinho_photo':
        show_ronaldinho_photo(message)
    elif call.data == 'show_neymar_photo':
        show_neymar_photo(message)
    elif call.data == 'show_aguero_photo':
        show_aguero_photo(message)
    elif call.data == 'show_teves_photo':
        show_tevez_photo(message)
    elif call.data == 'show_deBruyne_photo':
        show_deBruye_photo(message)
    elif call.data == 'show_gerrard_photo':
        show_gerrard_photo(message)
    elif call.data == 'show_torres_photo':
        show_torres_photo(message)
    elif call.data == 'show_suares_photo':
        show_suares_photo(message)


@bot.message_handler(commands=['start'])
def startMessage(message):
    show_interests(message.chat.id)

bot.polling(none_stop=True)