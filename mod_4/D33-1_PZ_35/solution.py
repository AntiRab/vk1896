"""

    Написать функцию fill_specializations, которая принимает
список кортежей из специальности и имени и возвращает словарь,
где в качестве ключей специальности, а в качестве значений -
списки имен. Желательно, чтобы это было реализовано через
словарь со значением по умолчанию.


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
   # YOUR CODE HERE


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        specs=[('Sales', 'John Doe'), ('Sales', 'Martin Smith'),
        ('Accounting', 'Jane Doe'), ('Marketing', 'Elizabeth Smith'),
        ('Marketing', 'Adam Doe')]
        print(fill_specializations(specs))
    Выходные данные
        {'Sales': ['John Doe', 'Martin Smith'],
        'Accounting': ['Jane Doe'],
        'Marketing': ['Elizabeth Smith', 'Adam Doe']}
"""
from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
   z = defaultdict(list)
   for key, name in specializations:
       z[key].append(name)
   return dict(z)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
