import telebot
from telebot import types
from youtube import YT_DownloadVideo
import re

bot = telebot.TeleBot('6841920142:AAH8l0ARalMF-JAxtKozPqxLwudUjAPbRQ0')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Youtube")
    item2 = types.KeyboardButton("Vk")
    item3 = types.KeyboardButton("Яндекс дзен")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, "Привет! Я умею скачивать видео, выбери с какого ресурса ты хочешь скачать видео",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Youtube" or message.text == 'Vk':
        bot.send_message(message.chat.id, "Отлично! Отправь ссылку на видео")
    elif message.text == "Яндекс дзен":
        bot.send_message(message.chat.id, "Возможность скачивания видео с этого ресурса еще в разработке")


@bot.message_handler(content_types=['text'])
def get_link(message):
    if re.match(r"http(s)?:\/\/(www.)?youtube\.com\/", message.text):
        bot.send_message(message.chat.id, "урааа!!!")
        try:
            ytfilename = f'{message.from_user.id}.mp4'
            status = YT_DownloadVideo(message.text, ytfilename)
            if status == 0:
                bot.send_message(message.chat.id, "Ссылка недействительна")
            elif status == -1:
                bot.send_message(message.chat.id, 'Файл слишком большой')

            bot.send_video(message.chat.id, open(fr"C:\Users\honor\upsTGbot\youtubefiles\{ytfilename}", mode='rb'))

        except:
            bot.send_message(message.chat.id, "Ошибка. Невозможно скачать видео по этой ссылке")
    else:
        bot.send_message(message.chat.id, "Ошибка. Невозможно скачать видео по этой ссылке")


bot.infinity_polling()
