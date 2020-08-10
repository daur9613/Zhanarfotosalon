#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Сам бот

import telebot
import config
from telebot import types

# Ассоциируем переменную bot с нашим токеном
bot = telebot.TeleBot(config.token)

# —— ОБРАБОТЧИКИ КОМАНД —--

@bot.message_handler(commands = ['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, 'Salem! Men Zhanar fotostudiasynyn botymin! Zakaz beru ushin tandanyz\n')


# —— РЕЖИМ ОЖИДАНИЯ СООБЩЕНИЙ ——
if __name__ == '__main__':
  print("start")
  bot.polling(none_stop=True)
