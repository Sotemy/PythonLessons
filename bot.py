import telebot, sqlite3

bot = telebot.TeleBot("1234647714:AAEb63ROfKfO1iRn0kIVUfmmtGUZOkzvT_I")
admin = "747449797"

class Page(object):
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        
    
    def choicebtn():
        print("Stuff")

    def backbtn():
        print("backbtn")

class Keyboard(object):
    def __init__(self, name):
        self.name = name
    

class ChoiceKey(Keyboard):
    def choicebutton(message):
        name = "cube"
        count = 1
        price = 1
        bot.send_message(message.chat.id, f'''stuff: {name} --- count:{str(count)} --- price:{str(price)}''')



@bot.message_handler(commands=["start"])
def StartPage(message):
    id = str(message.from_user.id)
    username = str(message.chat.username)
    user = Page(id, '0')
    bot.send_message(id, f'''Привет, {username} ({id}). Выбери какую нибудь кнопку''')
    bot.send_message(admin, f"{user.id} был зарегестрирован сегодня")
    choice = ChoiceKey.choicebutton(message)
    choice
    backbtn = Page.backbtn()
    backbtn

bot.polling()