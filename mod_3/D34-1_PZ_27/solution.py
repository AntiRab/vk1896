"""
Реализовать метод calculate_period с декоратором classmethod
в классе “Pendulum”, в котором написаны два атрибута класса:

    g =10
    pi = 3.14

Этот метод должен вычислять период математического маятника по формуле:
T=2π√l/g
Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.
class Pendulum:
   g = 10
   pi = 3.14

   @classmethod
   def calculate_period(cls, length):
       # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

Пример 1
    Входные данные
        print(Pendulum.calculate_period(10))
    Выходные данные
        6.28

"""


class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length):
        return 2 * cls.pi * (length / cls.g)**0.5

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
