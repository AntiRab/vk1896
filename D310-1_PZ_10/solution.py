"""
Необходимо написать программу, которая будет считывать
со стандартного ввода строку. Нужно разбить строку на слова,
словом будем считать последовательность символов отличных
от пробелов (то есть знаки пунктуации будут входить в слова).
Далее нужно посчитать сколько каждое слово встречалось в тексте
и вывести наиболее часто слово и сколько оно встретилось.
Все слова нужно также приводить к нижнему регистру при подсчете.
Гарантируется, что в тексте самое частое слово – единственное.
Пример 1
    Входные данные
        Python is an easy to learn, powerful programming language.
        It has efficient high-level data structures and a simple
        but effective approach to object-oriented programming.
    Выходные данные
        to 2
"""

text_word = input().lower().split()
words_count = {}
# Подсчитываем количество каждого слова
for word in text_word:
    words_count[word] = words_count.get(word, 0) + 1

# Находим самое часто встречающее слово
max_word = max(words_count, key=words_count.get)
max_count = words_count[max_word]

print(max_word,max_count)