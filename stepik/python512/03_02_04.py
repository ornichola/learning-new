"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_04 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
Sample Input:

\w denotes word character
No slashes here
Sample Output:

\w denotes word character
"""

import re
import sys


PATTERN = r'\\'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(PATTERN, line):
        print(line)
