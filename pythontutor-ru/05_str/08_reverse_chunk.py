'''
http://pythontutor.ru/lessons/str/problems/reverse_chunk/
Дана строка, в которой буква h встречается как минимум два раза.
Разверните последовательность символов,
заключенную между первым и последним появлением буквы h, в противоположном порядке.
'''

s = input()
first = s.find('h')
last = s.rfind('h')

print(s[:first] + s[last:first:-1] + s[last:])
