# я решил немного усложнить себе задачу, надеюсь это ок :)

from datetime import datetime # подключаем модуль datetime для определения даты
import os # необходима функция os.environ.get() для определения имени пользователя

""" используем функцию datetime.now() для определения текущей даты
используем функцию datetime.date() для отсечения времени от даты"""
day = datetime.date(datetime.now())
name = os.environ.get( "USERNAME" )

print (f'Good day {name}! {day} is a perfect day to learn some python.')

# additional bonus task
str1 = 'Good day {}! {} is a perfect day to learn some python.'
print(str1.format(name, day))

print ('Good day {1}! {0} is a perfect day to learn some python.'.format(day, name))

# этот вариант не работает, так как переменные day и name - это классы
# print ('Good day %s! %s is a perfect day to learn some python.' (name, day))