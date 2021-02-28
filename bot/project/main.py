import telebot, time

bot = telebot.TeleBot('')

monday = """1. Английский
2. Математика
3. Физкультура
4. Химия
5. Родная литература
6. Всеобщая история
7. Литература"""

tuesday = """1. Обществознание
2. География
3. Математика
4. Русский
5. Проект
6. Биология
7. Английский"""

wednesday = """1. Математика
2. Физкультура
3. ОБЖ
4. Литература
5. Физика
6. Химия
7. Экономика"""

thursday = """1. Литература
2. Математика
3. Биология
4. Русский
5. Всеобщая история
6. Астрономия
7. География"""

friday = """1. Физика
2. Английский
3. Обществознание
4. Физкультура
5. Математика
6. Информатика"""

saturday = """ЮХУУ ВЫХОДНОЙ!!!"""

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user.first_name
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Понедельник', 'Вторник')
    keyboard.row('Среда', 'Четверг')
    keyboard.row('Пятница', 'Суббота')
    bot.send_message(message.chat.id, f"Привет, {user}. Выбери день и я тебе выдам расписание:", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'понедельник':
        time.sleep(1)
        bot.send_message(message.chat.id, monday)
    elif message.text.lower() == 'вторник':
        time.sleep(1)
        bot.send_message(message.chat.id, tuesday)
    elif message.text.lower() == 'среда':
        time.sleep(1)
        bot.send_message(message.chat.id, wednesday)
    elif message.text.lower() == 'четверг':
        time.sleep(1)
        bot.send_message(message.chat.id, thursday)
    elif message.text.lower() == 'пятница':
        time.sleep(1)
        bot.send_message(message.chat.id, friday)
    elif message.text.lower() == 'суббота':
        time.sleep(1)
        bot.send_message(message.chat.id, saturday)

if __name__ == '__main__':
     bot.infinity_polling()
