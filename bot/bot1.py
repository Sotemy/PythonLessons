
import telebot


token = "1687395672:AAENEK9qTvtdMKWq31GetvXYYbLIDQJyLGM"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def start_massage(massage):
    bot.send_message(massage.chat.id, massage.text)
if __name__ == '__main__':
     bot.infinity_polling()