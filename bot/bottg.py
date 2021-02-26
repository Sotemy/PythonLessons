#!/usr/bin/env python
import telebot, config

admin_id = '1208787761'
# loglist = open(filename, 'w')
start = {'hi'}
help = {'hahahaah'}


##################################################################################################################
# клавиатура админа
admin_keyboard = telebot.types.ReplyKeyboardMarkup(True)
admin_keyboard.row("Check logs", "Balance")
admin_keyboard.row("FAQ 🖍")

##################################################################################################################
# клава юзера
user_keyboard = telebot.types.ReplyKeyboardMarkup(True)
user_keyboard.row("Buy btc")
user_keyboard.row("sell btc")

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    if str(message.from_user.id) in admin_id:
	    bot.send_message(message.chat.id, 'bot started', reply_markup = admin_keyboard)
    else:
        user = message.from_user.id
        username = message.from_user.first_name
        print(f"{user} pressed start")
        bot.send_message(message.chat.id, f"Hello, {username}.", reply_markup = user_keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, help)

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if str(message.from_user.id) in admin_id:
	    bot.send_message(message.chat.id, 'Hello, admin', reply_markup = admin_keyboard)
    else:
        userid = message.from_user.id
        # logfile = open(/usr/bin/, 'w')
        # logfile.write(f"user {userid} tried to acces root")
        print(f"user {userid} tried to acces root")
        bot.send_message(message.chat.id, 'you are not admin', reply_markup = user_keyboard)

bot.polling()
