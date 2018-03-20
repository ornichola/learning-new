'''
http://pythontutor.ru/lessons/str/problems/delete_every_third_char/
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
'''

s = input()
s_new = ''

for i in range(len(s)):
    if not i % 3 == 0:
        s_new += s[i]

print(s_new)
