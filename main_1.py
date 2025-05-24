import telebot
    
from bot_logic import gen_pass

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['token'])
def send_welcome(message):
    bot.reply_to(message, "Иди нафиг!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password_generate'])
def send_bye(message):
    bot.reply_to(message, gen_pass(7))

@bot.message_handler(commands=['bir'])
def send_bye(message):
    bot.reply_to(message, "С днём рождения!")

@bot.message_handler(commands=['alisa'])
def send_bye(message):
    bot.reply_to(message, "Алиса самая лучшая!")

@bot.message_handler(commands=['artem'])
def send_bye(message):
    bot.reply_to(message, "Артём самый лучший!")

@bot.message_handler(commands=['youtube'])
def send_bye(message):
    bot.reply_to(message, "Мой ютуб канал: https://www.youtube.com/@atemvoropayk")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
