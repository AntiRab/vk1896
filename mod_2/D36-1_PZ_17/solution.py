"""
В этом задании нужно будет написать свою реализацию filter()
(https://docs.python.org/3/library/functions.html#filter),
то есть генераторную функцию, которая принимает функцию и
последовательность и фильтрует последовательность в зависимости
от вердикта переданной функции. Воспользуйтесь своей реализацией,
чтобы применить лямбда функцию, поданную на вход, к поданной
на вход последовательности. Вам нужно написать свой код в секции
“YOUR CODE HERE”, остальной код можно оставить как есть:
def filter(func, seq):
   # YOUR CODE HERE

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)

Пример 1
    Входные данные
        lambda x: x > 0
        (1, 2, 0, 3, -1, -2, 5)
    Выходные данные
        1
        2
        3
        5
"""

def filter(func, seq):
   # Проходим по каждому элементу
   for item in seq:
      # Применяем функцию к элементу
      if func(item):
          yield item

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)
