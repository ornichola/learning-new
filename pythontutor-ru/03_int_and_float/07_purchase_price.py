'''
http://pythontutor.ru/lessons/int_and_float/problems/purchase_price/
Пирожок в столовой стоит a рублей и b копеек.
Определите, сколько рублей и копеек нужно заплатить за n пирожков.
Программа получает на вход три числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.
'''

a = int(input())
b = int(input())
n = int(input())

price = a * 100 + b

print(price * n // 100, price * n % 100)
