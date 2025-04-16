"""

    Написать функцию parse_time, которая принимает строку
в качестве параметра, которая является временем формата
“ГГГГ ММ ДД ЧЧ ММ СС” и парсит эту строку в объект
datetime.datetime и сдвигает ее на один день вперед.


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import datetime

string_datetime = input()


def parse_time(s):
   # YOUR CODE HERE

print(parse_time(string_datetime))


Пример 1
    Входные данные
        2023 03 03 12 30 00
    Выходные данные
        4
"""

import datetime

string_datetime = input()


def parse_time(s):
    dt = datetime.datetime.strptime(s,"%Y %m %d %H %M %S") #ГГГГ ММ ДД ЧЧ ММ СС
    dt = dt + datetime.timedelta(days=1)
    return int(dt.strftime("%d"))

print(parse_time(string_datetime))

