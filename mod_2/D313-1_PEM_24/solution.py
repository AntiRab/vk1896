"""
Необходимо написать генераторную функцию solution,
которая будет фильтровать данные из последовательности
data функцией func_filter, к полученным данным применять
функцию func_map и возвращать в качестве значения каждый
второй элемент полученной последовательности. Нужно
пользоваться здесь концепцией генератора, то есть
обрабатывать не все данные разом, а только те, что
необходимы для возвращения следующего значения. Дополните
также код своей реализацией кэшируещего декоратора из ДЗ 4:


def cache_deco(func):
   # YOUR CODE HERE

def solution(func_map, func_filter, data):
   # YOUR CODE HERE

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)


Пример 1
    Входные данные
        def calc():
            count = 0
            @cache_deco
            def calc_(x):
                nonlocal count
                count += 1
                print("Call:", count)
                return x
            return calc_
        for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
            print(i)
    Выходные данные
        Call: 1
        1
        Call: 2
        3
        3
Пример 2
    Входные данные
        def calc():
            count = 0
            def calc_(x):
                nonlocal count
                count += 1
                print("Call:", count)
                return x
            return calc_
        for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
            print(i)
    Выходные данные
        Call: 1
        1
        Call: 2
        Call: 3
        3
        Call: 4
        Call: 5
        3
        Call: 6
    """

def cache_deco(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args) # сохраняем в кэш
        return cache[args]
    return wrapper


def solution(func_map, func_filter, data):
    count = 0
    for item in data:
        if func_filter(item): # применяем фильтр
            mapped = func_map(item) # применяем функцию
            if count % 2 == 0: # берем через одного
                yield mapped
            count += 1


code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)