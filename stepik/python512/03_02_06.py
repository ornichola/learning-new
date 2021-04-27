"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_06 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

Sample Input:
I need to understand the human mind
humanity

Sample Output:
I need to understand the computer mind
computerity
"""

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub('human', 'computer', line))
