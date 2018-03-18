'''
http://pythontutor.ru/lessons/str/problems/second_occurence/
Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
Если буква f в данной строке встречается только один раз, выведите число -1,
а если не встречается ни разу, выведите число -2.
'''

s = input()

if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    print(s.find('f', s.find('f') + 1))

'''
if s.find('f') == -1:
    print ('-2')
else:
    print(s.find('f', s.find(''f') + 1))
'''
