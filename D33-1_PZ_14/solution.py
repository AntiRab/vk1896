"""
В Python есть встроенная функция map()
(https://docs.python.org/3/library/functions.html#map),
она принимает первым аргументом функцию, а вторым произвольную
последовательность. Возвращает она итератор – иными словами объект,
по которому можно проходиться циклом for. При этом каждый элемент,
который будет возвращаться этим итератором будет получен из элементов
исходной последовательности с помощью применения функции, переданной
первым аргументом в map(). Иными словами map(func, seq) применяет
функцию func ко всем элементам seq, причем делает это не разом,
а по мере того как мы итерируемся по новой последовательности.
Например, код:

seq = range(1, 4)
new_seq = map(lambda x: x * 2, seq)
for i in new_seq:
   print(i)

выведет нам числа от 2, 4, 6, так как мы к числам 1, 2, 3
применили функцию, которая умножает их на 2. В сценарии
использования map() лямбда функции позволяют нам записать
нужно преобразование в одну строку. Например, мы можем решить
задачу “Поданные на вход строки преобразовать к верхнему регистру,
если первым строки является символ ‘!’, иначе привести к нижнему.
В первом случае также убрать лидирующий ‘!’” буквально в 2 строки,
если считать, что исходные строки лежат в переменной seq:

for i in map(lambda x: x[1:].upper() if x[0] == "!" else x.lower(), seq):
   print(i)
В этом примере мы воспользовались тернарным оператором внутри
лямбда функции, чтобы компактно записать наш код.

Теперь само задание: напишите код, который также будет использовать
функцию map() и лямбда функцию. На вход будут подаваться три аргумента
для range: начало, конец и шаг числовой последовательности. Нужно вывести
для каждого элемента range квадрат числа, если число нечетное, иначе
вывести противоположное

Пример 1
    Входные данные
        1 10 1
    Выходные данные
        1
        -2
        9
         -4
        25
        -6
        49
        -8
        81
Пример 2
    Входные данные
        1 10 2
    Выходные данные
        1
        9
        25
        49
        81

"""
rang = input().split()

result = list(map(lambda x: x**2 if x % 2 != 0 else -x,
                  range(int(rang[0]), int(rang[1]), int(rang[2]))))
for i in result:
   print(i)
