"""
Напишите декоратор, который будет кэшировать вызовы функции,
которая будет передана на вход. То есть декоратор должен
проверить нет ли в кэше (например, словаре) значения,
и если нет, то вычислить и запомнить результат, если есть,
то взять это значение. Дополните код ниже, дописав свой код
в секции “YOUR CODE HERE”.

def cache_deco(func):
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        @cache_deco
        def fib(k):
            if k <= 2:
                return 1
            return fib(k - 1) + fib(k - 2)
        print(fib(30))
    Выходные данные
        832040
"""

def cache_deco(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args] # возвращаем значение из кэша
        result = func(*args) # вычисляем значение
        cache[args] = result # сохраняем значение в кэш
        return result
    return wrapper

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)