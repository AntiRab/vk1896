"""

В классе Dictionary реализуйте методы __call__ и __init__:

В __init__(self, dictionary) объявите словарь в качестве атрибута
В методе call реализуйте поиск в словаре по ключу

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

class Dictionary:
   def __init__(self, dictionary):
       # YOUR CODE HERE

   def __call__(self, key):
       # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)


Пример 1
    Входные данные
        dictionary = Dictionary({1:2, 2:1, 3:3})
        print(dictionary(1))
    Выходные данные
        2
"""

class Dictionary:
   def __init__(self, dictionary):
       self.dictionary = dictionary

   def __call__(self, key):
       return self.dictionary[key]


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
