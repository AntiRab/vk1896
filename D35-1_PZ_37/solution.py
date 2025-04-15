"""

    Написать функцию shift_time, которая принимает
2 параметра: количество дней и количество секунд и
сдвигает дату и время 01.01.2023 12:30:00 на указанное
количество дней и секунд. В качестве выходного значения
нужно вывести кортеж: день и секунда от сдвинутого времени.


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
   # YOUR CODE HERE

print(shift_time(days, seconds))

Пример 1
    Входные данные
        1
        0
    Выходные данные
        (2, 0)
"""

import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    delta_d = datetime.timedelta(days=days, seconds=seconds)
    dt = datetime.datetime.strptime("01.01.2023 12:30:00",
                                    "%d.%m.%Y %H:%M:%S")
    dt = dt+delta_d
    return (int(datetime.datetime.strftime(dt,"%d")),
            int(datetime.datetime.strftime(dt,"%S")))

print(shift_time(days, seconds))

