import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('6331851978:AAHJidKJI4WJVkDdPMcvR0IJA-Ap638YNfo')
API = "https://restcountries.com/v2/all"
countryName = None
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hello write country  and know information ')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'getCountriesPopulation':
        getCountriesPopulation(call.message)
    elif call.data == 'getCountriesCapital':
        getCountriesCapital(call.message)
    elif call.data == 'getCountriesCallingCodes':
        getCountriesCallingCodes(call.message)
    elif call.data == 'getCountriesCurrencies':
        getCountriesCurrencies(call.message)
    elif call.data == 'getCountriesLanguages':
        getCountriesLanguages(call.message)
    elif call.data == 'getCountriesAllInformation':
        getCountriesAllInformation(call.message)




def getCountriesAllInformation(message):
    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)
    info = data[0]
    capitalOfCountry = info['capital']
    populationOfCountry = info['population']
    callingCodeOfCountry = '+' + info['callingCodes'][0]
    currenciesOfCountry  = info['currencies'][0]['name']
    currenciesSynbolOfCountry  = info['currencies'][0]['symbol']
    lenguageNameOfCountry = info['languages'][0]['name']
    lenguageOfCountry = info['languages'][0]['nativeName']
    if countryName != 'Australia':
        borders = info['borders']
        country_borders = ' '
        for i in borders:
            country_borders += i + ' '
    else:
        country_borders = f"The {countryName} doesn't have borders of any countries"

    flagPNG = info['flags']['png']
    topLevelDomain = info['topLevelDomain'][0]

    bot.send_message(message.chat.id,   f'The capital of {countryName} is <i><u><em><b> {capitalOfCountry}</b></em></u></i> \n'
                                            f'the population of {countryName} is <i><u><em><b>{populationOfCountry}</b></em></u></i> \n'
                                            f'the calling code of {countryName} is <i><u><em><b>{callingCodeOfCountry}</b></em></u></i> \n'
                                            f'currency of {countryName} is <i><u><em><b>{currenciesOfCountry}</b></em></u></i> \n'
                                            f'currency symbol of {countryName} is <i><u><em><b>{currenciesSynbolOfCountry}</b></em></u></i> \n'
                                            f'name of {countryName} is <i><u><em><b>{lenguageNameOfCountry}</b></em></u></i> \n'
                                            f'lenguage of {countryName} is <i><u><em><b>{lenguageOfCountry}</b></em></u></i> \n'
                                            f'borders of {countryName} is <i><u><em><b>{country_borders}</b></em></u></i> \n '
                                            f'top Level Domain of {countryName} is <i><u><em><b>{topLevelDomain}</b></em></u></i> \n '
                                            f'flag in PNG format of {countryName} is <i><u><em><b>{flagPNG}</b></em></u></i> \n', parse_mode='html')


def getCountriesLanguages(message):
    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)
    lenguage = data[0]
    lenguage_code = lenguage['languages'][0]['nativeName']
    bot.send_message(message.chat.id, f'The capital of {countryName} is {lenguage_code}')


def getCountriesCurrencies(message):
    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)
    currencies = data[0].get("currencies", [])
    currency_code = currencies[0].get("code", "N/A")

    bot.send_message(message.chat.id, f'The capital of {countryName} is {currency_code}')
def getCountriesCallingCodes(message):
    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)
    calling_codes = data[0].get("callingCodes", ["N/A"])
    calling_codes ='+' + calling_codes[0]
    bot.send_message(message.chat.id, f'The capital of {countryName} is {calling_codes}')

def getCountriesCapital(message):
    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)
    capital = data[0].get("capital", "N/A")
    bot.send_message(message.chat.id, f'The capital of {countryName} is {capital}')


@bot.message_handler()
def getCountry(message):
    global countryName
    countryName = message.text

    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)

    if "status" in data and data["status"] == 404:
        bot.send_message(message.chat.id,f"Country '{countryName}' doesn't exist, please input a valid country name.")
    else:
        countryName = data[0]['name']
        btns(message)





def getCountriesPopulation(message):
    res = requests.get(f'https://restcountries.com/v2/name/{countryName}')
    data = json.loads(res.text)
    population = data[0].get("population", "N/A")
    bot.send_message(message.chat.id, f'Population in {countryName} is {population}')


def btns(message):
    markup = types.InlineKeyboardMarkup()
    capital = types.InlineKeyboardButton('Capital', callback_data='getCountriesCapital')
    population = types.InlineKeyboardButton('population', callback_data='getCountriesPopulation')
    callingCodes = types.InlineKeyboardButton('callingCodes', callback_data='getCountriesCallingCodes')
    currencies = types.InlineKeyboardButton('currencies', callback_data='getCountriesCurrencies')
    lenguage = types.InlineKeyboardButton('languages', callback_data='getCountriesLanguages')
    allInformation = types.InlineKeyboardButton('all information', callback_data='getCountriesAllInformation')
    markup.add(capital, population, callingCodes, currencies, lenguage, allInformation)
    bot.send_message(message.chat.id, f" which you would like to know about {countryName}", reply_markup=markup)


bot.polling(none_stop=True)
