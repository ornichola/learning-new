"""
http://pythontutor.ru/lessons/lists/problems/even_elements/
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""

l = input().split()
for i in l:
    if int(i) % 2 == 0:
        print(i)
