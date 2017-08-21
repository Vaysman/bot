# -*- coding: utf-8 -*-
import telebot

token = '436750663:AAHobagg4S1NiG4iWJx1B5diAys2E78a_oE'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)