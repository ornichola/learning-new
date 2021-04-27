"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_03 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:

zabcz
zzxzz
"""

import re
import sys


PATTERN = r'z.{3}z'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(PATTERN, line):
        print(line)
