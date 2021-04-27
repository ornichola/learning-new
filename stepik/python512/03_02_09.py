"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_09 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'(\w)\1+', r'\1', line))
