"""
http://pythontutor.ru/lessons/lists/problems/even_indices/
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""

l = input().split()
for i in range(len(l)):
    if i % 2 == 0:
        print(l[i])

# for i in range(0, len(l), 2):
#     print(l[i])
