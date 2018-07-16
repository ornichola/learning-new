import math


L = [2, 4, 16, 25]

print('\nFOR LOOP')
for el in L:
    print(math.sqrt(el))

print('\nMAP')
for el in map(math.sqrt, L):
    print(el)

print('\nLIST COMPREHENSION')
for el in [math.sqrt(el) for el in L]:
    print(el)
