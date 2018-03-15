'''
http://pythontutor.ru/lessons/for_loop/problems/how_many_zeroes/
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
Подсчитайте количество нулей среди введенных чисел и выведите это количество.
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
'''

n = int(input())
zeroes = 0
for _ in range(n):
    inp = int(input())
    if inp == 0:
        zeroes += 1
print(zeroes)
