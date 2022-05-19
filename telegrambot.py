import telebot

bot = telebot.TeleBot("5391513178:AAFh6kdi8MZzv5wu0UmaqnHOdteV9MIYmlc")
@bot.message_handler(commands=["help", "start"])

def enviar(message):
    bot.reply_to(message, "Hola, Como estas?")

@bot.message_handler(func=lambda message:True)

def mensaje(message):
    bot.reply_to(message, message.text)

bot.polling()