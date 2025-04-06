"""
Написать функцию get_indexes которая принимает два списка и
возвращает список индексов, в которых элемент из первого
списка меньше элемента из второго списка по данному индексу.
Желательно проходиться сразу по двум массивам одновременно
(вспомните функцию zip). Для нахождения индексов можно
использовать enumerate вместе с zip.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""

from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(i for i, (n1, n2) in enumerate(zip(nums1,nums2))if n1 < n2)

# print(get_indexes([1,5,9,5],[7,9,3,6,8]))

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)