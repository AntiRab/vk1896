"""

    Написать функцию rotate_list, которая принимает список
целых чисел и целое число, которое будет задавать, сколько
крутить список. Под кручением списка подразумевается забор
элемента из конца списка и вставка его в начало списка.
Желательно, чтобы это было реализовано через двустороннюю
очередь.


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        print(rotate_list([1,2,3,4], 1))
    Выходные данные
        [4, 1, 2, 3]
"""

from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    nums_new = deque(nums)
    for _ in range(n):
       nums_new.appendleft(nums_new.pop())
    return list(nums_new)
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
