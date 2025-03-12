 """
Необходимо написать программу, которая будет принимать на вход строку,
разбивать строку на слова по пробелу. Далее нужно из всех слов убрать
следующие пунктуационные знаки:
!,.?;:#$%^&*(),
а также привести слова к нижнему регистру. В итоге нужно вывести
в алфавитном порядке слова, которые состоят как минимум из 5 символов,
а также имеют как минимум 4 уникальных символа, и которые встретились
в исходном тексте более 2х раз.
Пример 1
    Входные данные
         It is a herbaceous perennial which produces flowers in the typical aroid structure: a densely crowded inflorescence called a spadix is subtended by one large bract called a spathe (occasionally two spathes are produced, with the upper spathe smaller). The spadix is generally cream or ivory when young, and turns green with age; the spathe is generally white or white with green nerves distally from the margin, turning green with age. Leaves are basal, glossy and somewhat deeply veined, ovate and acuminate. The petioles are long and the leaves arch gracefully. The plant produces offsets at the base and in time becomes a dense clump. Spathiphyllum wallisii is one of approximately 40 species in a genus of tropical evergreens. It was discovered in the late 19th century growing wild in Colombia. A number of cultivars, many of hybrid origin, are commercially available, such as the larger hybrids "Mauna Loa", named after the Hawaiian volcano, and the even larger “Sensation", which are both popular indoor plants. "Domino" is a finely variegated variety of intermediate size. Its wide natural range includes parts of Mexico, the Caribbean Islands, and northern South America.
    Выходные данные
        green
        spathe
Пример 2
    Входные данные
        Strings implement all of the common sequence operations, along with the additional methods described below. Strings also support two styles of string formatting, one providing a large degree of flexibility and customization (see str.format(), Format String Syntax and Custom String Formatting) and the other based on C printf style formatting that handles a narrower range of types and is slightly harder to use correctly, but is often faster for the cases it can handle (printf-style String Formatting). The Text Processing Services section of the standard library covers a number of other modules that provide various text related utilities (including regular expression support in the re module).
    Выходные данные
        formatting
        string

"""
text = input().lower()
sub = "!,.?;:#$%^&*()"
# Убираем символы и приводим к нижнему регистру
cleaned_text = "".join(symbol for symbol in text if symbol not in sub)
# Разбиваем строку на слова
text_word = cleaned_text.split()
# Подсчитываем количество каждого слова
words_count = {}
for word in text_word:
    words_count[word] = words_count.get(word, 0) + 1
# Фильтруем слова по условиям:
# Слово встречается более 2 раз
# Длина слова >= 5
# количество уникальных символов >= 4
filtered_words = []
for word, count in words_count.items():
    if count > 2 and len(word) >= 5 and len(set(word)) >= 4:
        filtered_words.append(word)
# Сортируем слова
filtered_words.sort()
# Выводим результат
for word in filtered_words:
    print(word)
