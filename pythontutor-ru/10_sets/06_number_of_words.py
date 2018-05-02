"""
http://pythontutor.ru/lessons/sets/problems/number_of_words/

Дан текст: в первой строке записано число строк, далее идут сами строки.
Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
"""

n = int(input())
unique_words = set()

for i in range(n):
    words = input().split()
    for word in words:
        unique_words.add(word)

print(len(unique_words))
