from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# чтоб телега работала
# PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
#   'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


'''
def greet_planet(bot, update):
    import ephem
    import datetime
    date = datetime.date.today()
    print('Взвана планета /planet')
    planets = update.message.text.split()[1]
    # print(planets)
    if planets == 'Venus':
        planets1 = ephem.Venus(date)
    planets1 = ephem.constellation(planets1)
    print(planets1)
'''


def main():
        #mybot = Updater("773873236:AAHl7STB8NGZopRZxXz6LyIIrLOMIS6a7uo", request_kwargs=PROXY)
    mybot = Updater("773873236:AAHl7STB8NGZopRZxXz6LyIIrLOMIS6a7uo")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #dp.add_handler(CommandHandler('planet', greet_planet))
    mybot.start_polling()
    mybot.idle()


main()
