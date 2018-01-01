data = [ 1, 2, 3, 4, 5, 6, 8 ]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)

print(evens)

evens = [num for num in data if not num % 2]

print(evens)


data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

print(words)

words = [num for num in data if isinstance(num, str)]

print(words)


data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

print(title)

title = [word.title() for word in data ]

print(title)
