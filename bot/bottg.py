#!/usr/bin/env python
import telebot

bot = telebot.TeleBot('')
admin = ''

shop_name = "<i><b>HAHHAHAHAHA</b></i>"

stuff = ['start', 'PINK STARBURST', 'WHITE DEATH', 'BLACK DIAMOND']
price = ['start', ' - 5€', ' - 6€', ' - 5€']
town = ['start', 'Aalen', 'Bad Mergentheim', 'Baden-Baden', 'Bruchsal', 'Esslingen', 'Freiburg im Breisgau', 'Freudenstadt', 'Friedrichshafen', 'Göppingen', 'Hechingen', 'Heidelberg', 'Heilbronn', 'Karlsruhe', 'Konstanz', 'Ludwigsburg', 'Mannheim', 'Offenburg', 'Pforzheim', 'Ravensburg', 'Reutlingen', 'Schwäbisch Gmünd', 'Schwäbisch Hall', 'Stuttgart', 'Tübingen', 'Ulm']

def town_choose(message):
    markup = telebot.types.InlineKeyboardMarkup()
    for i in range(0,24):
        i = i + 1
        markup.add(telebot.types.InlineKeyboardButton(text=town[i], callback_data=i))
    bot.send_message(message.chat.id, text="Wahle sein Stadt:", reply_markup=markup)

def stuff_choose(message):
    markup = telebot.types.InlineKeyboardMarkup()
    for sp in range(0,3):
        sp = sp + 1
        markup.add(telebot.types.InlineKeyboardButton(text=stuff[sp] + price[sp], callback_data=sp*10))
    bot.send_message(message.chat.id, text="Wahle Stuff:", reply_markup=markup)   

def help(message):
    bot.send_message(message.chat.id, "f[f[[f[f")

@bot.message_handler(commands=['start'])
def start_message(message):
    username = message.from_user.first_name
    user_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    user_keyboard.row('Kaufen', 'Reichweite')
    user_keyboard.row('Stadt wahlen', 'Stuffback')
    bot.send_message(message.chat.id, f'{shop_name}\n\n Hallo {username}. Ich werde Ihnen helfen, Marihuana zum NIEDRIGSTEN PREIS in der Stadt zu kaufen\n Wenn Sie etwas nicht verstehen, schreiben Sie /help', parse_mode='HTML', reply_markup=user_keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'kaufen':
        town_choose(message)
    elif message.text.lower() == 'reichweite':
        stuff_choose(message)
    elif message.text.lower() == 'stadt wahlen':
        town_choose(message)
    elif message.text.lower() == 'stuffback':
        help(message)

@bot.message_handler(commands=['balance'])
def check_balance(message):
    if str(message.from_user.id) in admin:
        print("log")
    else:
        print("asdasdasdasd")

bot.polling()
# \n Hallo {username}. Ich werde Ihnen helfen, Marihuana zum NIEDRIGSTEN PREIS in der Stadt zu kaufen\n Wenn Sie etwas nicht verstehen, schreiben Sie /help'