'''
http://pythontutor.ru/lessons/str/problems/replace_in_chunk/
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
'''

s = input()

before = s[:s.find('h') + 1]
after = s[s.rfind('h'):]
replaced = s[s.find('h') + 1:s.rfind('h')].replace('h', 'H')

print(before + replaced + after)
