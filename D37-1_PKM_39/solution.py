"""
    Написать функцию most_common_months, которая принимает
в качестве параметра список строк, которые являются датами
формата “ГГГГ-ММ-ДДTЧЧ-ММ-СС” и некоторое целое число n,
и выводит топ n самых частых месяцев этих дат. Желательно,
чтобы это было реализовано через Counter из модуля collections.


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
   # YOUR CODE HERE


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
        print(most_common_months(dates, 2))
    Выходные данные
        [1, 2]
"""

import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    month_list = list()
    for date in dates:
        month_list.append(datetime.datetime.
                          strptime(date,"%Y-%m-%dT%H:%M:%S").month)
    rang = Counter(month_list)
    rang = sorted(rang.items(), key=lambda item: item[1], reverse=True)
    return [x[0] for x in rang[:n]]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
