'''
http://pythontutor.ru/lessons/str/problems/first_and_last_occurences/
Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего появления.
Если буква f в данной строке не встречается, ничего не выводите.
'''

s = input()

first = 0
last = 0

first = s.find('f')
if first != -1:
    for i in range(len(s)):
        next = s.find('f', i)
        if next > last:
            last = next
    print(first)
    if last > first:
        print(last)

'''
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
'''
