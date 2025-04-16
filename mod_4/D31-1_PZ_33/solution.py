"""
    Написать функцию write_and_read, которая будет записывать
в файл текст как параметр функции и читать текст из этого
файла и передавать на выход функции.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import os

text = input()

def write_and_read(text):
   # YOUR CODE HERE

print(write_and_read(text))


Пример 1
    Входные данные
        hello world
    Выходные данные
        hello world

"""
import os

text = input()

def write_and_read(text):
    if text != "":
        with open("example.txt", mode="w",encoding="utf-8") as f:
            f.write(text)
    with open("example.txt", mode="r", encoding="utf-8") as f:
        text = f.read()
        return text

print(write_and_read(text))
