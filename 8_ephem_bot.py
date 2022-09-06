"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import date

logging.basicConfig(filename='bot.log', level=logging.INFO)

#PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start\nЕсли ты введешь команду /planet и добавишь название планеты на английском языке, то я расскажу кое-что интересное')

def planet_constellation(update, context):
    logging.info('Вызвана команда /planet')
    planet=list(map(str,update.message.text.split()))[1]
    logging.info(planet)
    body = getattr(ephem, planet)(date.today())
    constellation = ephem.constellation(body)
    update.message.reply_text(f'{planet} сегодня в созвездии {constellation}')

def talk_to_me(update, context):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text[::-1])  # по просьбе Максима

def main():
    mybot = Updater(settings.API_KEY, use_context = True) # request_kwargs = PROXY
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

