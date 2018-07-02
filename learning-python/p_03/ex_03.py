"""
Напишите цикл for, который выводит
элементы словаря в  порядке возрастания. (Подсказка: используйте метод
keys словаря и метод списка sort или новую встроенную функцию sorted.)
"""

d = {'c': 2, 'a': 0, 'b': 1, 'd': 3}

for k in sorted(d):
    print(k, d[k])

keys = list(d.keys())
keys.sort()
for k in keys:
    print(k, d[k])
