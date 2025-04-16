"""
Напишите декоратор, который будет принимать натуральное
число n – число повторений – и будет повторять вызов
декорированной функции n раз, а также возвращать значение
из последнего вызова. Дополните код ниже, дописав свой код
в секции “YOUR CODE HERE”.

def repeat_deco(n=1):
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        @repeat_deco(4)
        def hello():
            print("hello")
        hello()
    Выходные данные
        hello
        hello
        hello
        hello
Пример 2
    Входные данные
        @repeat_deco(n=3)
        def add(seq, val):
            seq.append(val)
            return seq
        print(add([], 1))
    Выходные данные
        [1, 1, 1]
"""
def repeat_deco(n=1):
    def decor(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decor

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
