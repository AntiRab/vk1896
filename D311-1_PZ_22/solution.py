"""
Представьте, что у вас есть словарь с ключами и их частотами
(то есть насколько часто встречался каждый ключ)
в качестве значений. Напишите функцию make_most_common_keys,
которая принимает словарь частот и выводит отсортированный
(например через функцию sorted) по убыванию частот
(то есть значений ключей) список ключей.
from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
C  # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)


Пример 1
    Входные данные
        d =  {5:3, 3:5, 0:2, 4:6, 7:10}
        print(make_most_common_keys(d))

Выходные данные
    [7, 4, 3, 5, 0]

Пример 2
    Входные данные
        d = {0:1, 1:2, 2:3, 3:4, 4:5}
        print(make_most_common_keys(d))

    Выходные данные
        [4, 3, 2, 1, 0]
"""

from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    return sorted(d.keys(), key=lambda k: d[k], reverse=True)


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)