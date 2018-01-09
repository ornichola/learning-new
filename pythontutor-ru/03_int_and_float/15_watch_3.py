'''
http://pythontutor.ru/lessons/int_and_float/problems/watch_3/
С начала суток часовая стрелка повернулась на угол в α градусов.
Определите сколько полных часов, минут и секунд прошло с начала суток, то есть решите задачу, обратную задаче «Часы - 1».
Запишите ответ в три переменные и выведите их на экран.
'''

alpha = float(input())
H = alpha // 30
M = (alpha - H * 30) // 0.5
S = (alpha - H * 30 - M * 0.5) * 120

print(int(H), int(M), int(S))

#print(int(angle // 30), int(angle % 30 * 2), int(angle % 0.5 * 120))
