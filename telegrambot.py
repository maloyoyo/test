

import telebot
from pyowm.owm import OWM


bot = telebot.TeleBot("1016204377:AAE6cwbQ_1zeSyIBOZWRh3XJefQLwixClrM", parse_mode=None)
owm = OWM('2f2061299c8043a8af1ca3e29e876e7a')



@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place( message.text )
        weather = observation.weather
        temp = weather.temperature('celsius')["temp"]
    	#bot.reply_to(message, message.text)
        answer = ("В городе " + str( message.text) + " сейчас " + str(weather.detailed_status)) + "\n"
        answer += ("Температура " + str(temp)) + "\n\n"
        if temp < 10:
            answer +=("Очень холодно, стоит одеться потеплее!")
        elif temp < 20:
        	answer +=("Прохладненько, можно что-нибудь накинуть!")
        else:
        	answer +=("Вполне хорошая температура!")


        bot.send_message(message.chat.id, answer)

    except:
        bot.send_message(message.chat.id, 'Извините, произошла ошибка')
    print('Завершение')

bot.polling( none_stop = True)
