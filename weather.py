#погода

from colorama import init
from colorama import Fore, Back, Style

from pyowm.owm import OWM

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('2f2061299c8043a8af1ca3e29e876e7a')

place = input('Введите страну/город: ')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
weather = observation.weather
temp = weather.temperature('celsius')["temp"]

#w.temperature('celsius')
init()
print("В городе " + str(place) + " сейчас " + str(weather.detailed_status))
print(Fore.GREEN)
print("Температура " + str(temp))
print(Fore.CYAN)
if temp < 10:
    print("Очень холодно, стоит одеться потеплее!")
elif temp < 20:
	print("Сейчас прохладненько, можно что-нибудь накинуть!")
else:
	print("Вполне хорошая температура!")

print(weather)
