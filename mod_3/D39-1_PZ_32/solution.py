"""
Реализуйте следующую иерархию классов:

    В классе Rectangle с атрибутами a и b, который являются
сторонами прямоугольника реализуйте метод calculate_area,
который вычисляет площадь прямоуольника по формуле S =ab:
    В классе-наследнике от Rectangle- Square реализуйте
метод __init__, в котором принимается только один
параметр - сторона. Желательно, чтобы вы это реализовали
через super.
    В классе-примеси CalculatePerimeterMixin, наследнике
Rectangle, реализуйте метод calculate_perimeter, который
вычисляет периметр по формуле P =2(a + b)
    В классе наследнике SquareWithMixin от двух классов
(CalculatePerimeterMixin, Square) реализуйте
3 магических метода:
        __eq__, который сравнивает фигуры по сторонам
        __gt__, который сравнивает фигуры по площади
        __add__, который складывает площади двух фигур


Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

class Rectangle:
   def __init__(self, a, b):
       self.a = a
       self.b = b

   def calculate_area(self):
       # YOUR CODE HERE


class Square(Rectangle):
   def __init__(self, a):
       # YOUR CODE HERE


class CalculatePerimeterMixin(Rectangle):
   def calculate_perimeter(self):
       # YOUR CODE HERE


class SquareWithMixin(CalculatePerimeterMixin, Square):
   def __eq__(self, other):
       # YOUR CODE HERE

   def __gt__(self, other):
       # YOUR CODE HERE

   def __add__(self, other):
       # YOUR CODE HERE


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
Пример 1
    Входные данные
        square_with_mixin1 = SquareWithMixin(3)
        square_with_mixin2 = SquareWithMixin(2)
        print(square_with_mixin1.calculate_area())
        print(square_with_mixin1.calculate_perimeter())
        print(square_with_mixin1 == square_with_mixin1)
        print(square_with_mixin1 == square_with_mixin2)
        print(square_with_mixin1 > square_with_mixin2)
        print(square_with_mixin1 > square_with_mixin1)
        print(square_with_mixin1 + square_with_mixin1)
    Выходные данные
        9
        12
        True
        False
        True
        False
        18
"""


class Rectangle:
   def __init__(self, a, b):
       self.a = a
       self.b = b

   def calculate_area(self):
       return self.a * self.b


class Square(Rectangle):
   def __init__(self, a):
       self.a, self.b = a, a


class CalculatePerimeterMixin(Rectangle):
   def calculate_perimeter(self):
       return 2 * (self.a + self.b)


class SquareWithMixin(CalculatePerimeterMixin, Square):
   def __eq__(self, other):
       return self.a == other.a

   def __gt__(self, other):
       return self.calculate_area() > other.calculate_area()

   def __add__(self, other):
       return self.calculate_area() + other.calculate_area()


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
