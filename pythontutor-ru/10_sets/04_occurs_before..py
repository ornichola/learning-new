"""
http://pythontutor.ru/lessons/sets/problems/occurs_before/
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO, если не встречалось.
"""

lst = [int(i) for i in input().split()]
st = set(lst)
appearances = [0 for _ in range(len(lst))]

while st:
    el = st.pop()
    appeared = False
    for i in lst:
        if i == el and not appeared:
            appearances[lst.index(i)] = 'NO'
            appeared = True
            lst[lst.index(i)] = None
            continue
        elif i == el and appeared:
            appearances[lst.index(i)] = 'YES'
            lst[lst.index(i)] = None
            continue
        else:
            pass

for i in appearances:
    print(i)

"""
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
"""
