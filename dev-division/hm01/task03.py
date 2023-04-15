"""
Найдите два ключа с самыми большими значениями в словаре.
"""

def task_03(dictionary: dict):
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    if len(dictionary) < 2:
        raise ValueError(f'В словаре {dictionary} меньше двух ключей')
    d = dict()
    biggest = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:2]
    d[biggest[0][0]], d[biggest[1][0]] = biggest[0][1], biggest[1][1]
    return d

    # https://stackoverflow.com/questions/39496096/understanding-dictionary-get-in-python
    # return sorted(dictionary, key=dictionary.get)[-2:]


print(task_03({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}))
