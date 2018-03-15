'''
http://pythontutor.ru/lessons/for_loop/problems/sum_of_cubes/
По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.
'''

n = int(input())
s = 0
for i in range(1, n+1):
    s += i ** 3
print(s)
