'''
http://pythontutor.ru/lessons/str/problems/num_words/
Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
Используйте для решения задачи метод count.
'''

s = input()
print(s.count(' ') + 1)
