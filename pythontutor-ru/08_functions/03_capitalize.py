"""
http://pythontutor.ru/lessons/functions/problems/capitalize/
Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же,
меняя первую букву на большую.
Например, print(capitalize('word')) должно печатать слово Word.

На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв.
Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы.
При этом используйте вашу функцию capitalize().

Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(),
которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.
"""


def capitalize(word):
    ascii_code = ord(word[0]) - 32
    word_capitalized = chr(ascii_code) + word[1:]
    return word_capitalized


words = input().split()

for word in words:
    print(capitalize(word), end=' ')
