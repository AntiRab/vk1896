"""
В этом задании нужно будет написать свою реализацию map(),
который мы обсуждали в прошлом ДЗ. То есть нужно написать
генераторную функцию, которая первым аргументом будет принимать
функцию, а вторым некую последовательность. Полученный генератор
должен генерировать значения из переданной последовательности,
пропущенные через переданную первым аргументом функцию.

Воспользуйтесь своей реализацией, чтобы применить лямбда функцию,
поданную на вход, к поданной на вход последовательности. Вам нужно
написать свой код в секции “YOUR CODE HERE”, остальной код можно
оставить как есть:

Пример 1
    Входные данные
        lambda x: x ** 2
        range(-10, 11, 2)
    Выходные данные
        100
        64
        36
        16
        4
        0
        4
        16
        36
        64
        100
"""
def map(func, seq):
   # Проходим по каждому элементу
   for item in seq:
      # Применяем функцию к элементу
      yield func(item)

func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
   print(x)