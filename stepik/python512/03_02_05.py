"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_05 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa
Sample Output:

blabla is a tandem repetition
123123 is good too
"""

import re
import sys


PATTERN = r'\b(.+)\1\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(PATTERN, line):
        print(line)
