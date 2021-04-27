"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_01 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat
"""

import re
import sys


PATTERN = r'cat.*cat'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(PATTERN, line.rstrip()):
        print(line)
