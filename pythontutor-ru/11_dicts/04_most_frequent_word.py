"""
Дан текст: в первой строке задано число строк, далее идут сами строки.
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""

words = {}
for _ in range(int(input())):
    words_split = input().split()
    for word in words_split:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

max_key = None
max_value = 1
for word in words:
    if words[word] > max_value:
        max_value = words[word]
        max_key = word

if max_value > 1:
    max_occurrences = {}
    for word in words:
        if words[word] == max_value:
            max_occurrences[word] = max_value
    d = max_occurrences
else:
    d = words

print(sorted(d.keys())[0])

"""
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
"""
