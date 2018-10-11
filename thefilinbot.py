import random
import requests
import telebot
from telebot import apihelper


PROXY = {"https": "socks5://sabarban:musora666pidorasy@staff.adminez.org:9000/"}
TOKEN = "646987513:AAFB-XnaJuijfhlwcD7fW_d0UqvkEd7RpHc"
HELP_STRING = """Филин умееет подтверждать.\
               Если его попросить что-то подтвердить, то он должен это подтвердить.\
               Или не подтвердить.\
               На слово Филин - отзывается."""


confirmation = ["подтверди", "Подтверди", "скажи да"]
answer = ["Зуб даю!", "Подтверждаю!", "Сто пудов!", "Нет гарантии 100%", "За тебя не могу дать гарантию!", "УГУ"]


apihelper.proxy = PROXY
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, HELP_STRING)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bullshit = False
    for con in confirmation:
        if con in message.text:
            bot.send_message(message.chat.id, random.choice(answer))
            bullshit = False
            break
        else:
            bullshit = True
    
    if bullshit == True:
        bot.send_message(message.chat.id, "УГУ")


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    file_info = bot.get_file(message.sticker.file_id)
    file = requests.get("https://api.telegram.org/file/bot{0}/{1}".format(TOKEN, file_info.file_path), proxies=PROXY)
    bot.send_photo(message.chat.id, file.content)
    bot.send_message(message.chat.id, message.sticker.emoji)


bot.polling()
