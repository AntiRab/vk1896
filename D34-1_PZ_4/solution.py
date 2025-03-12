"""
Необходимо будет написать программу, которая будет считывать
со стандартного ввода строку и выводить на стандартный вывод
является ли строка “правильной”. Строка считается правильной,
если в ней есть латинская буква “a” или “o”, но нет букв “i” и “e”.
Строка содержит только латинские буквы в нижнем регистре.
Пример 1
    Входные данные
        letter
    Выходные данные
        False
Пример 2
    Входные данные
        pilot
    Выходные данные
        False
"""

line = input()
rul11 = True if 'a' in line else False
rul12 = True if 'у' in line else False

rul21 = True if "i" not in line else False
rul22 = True if 'e' not in line else False

res =  (rul11 or rul12) and (rul21 and rul22)
print(res)