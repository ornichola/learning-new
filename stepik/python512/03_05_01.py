"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_05_01 API
"""

"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт 
об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring

У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
"""

import json
import requests


def get_number_info(num: str) -> dict:
    res = requests.get(url=f'http://numbersapi.com/{num}/math?json=true')
    return json.loads(res.text)


def is_interesting(num: str) -> bool:
    return get_number_info(num).get('found')


with open('03_05_01_dataset.txt') as f:
    numbers = f.read().splitlines()
    for number in numbers:
        print('Interesting' if is_interesting(number) else 'Boring')
