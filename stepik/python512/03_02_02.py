"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_02_02 Регулярные выражения в Python
"""

"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.

Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:
cat
catapult and cat
"cat"
!cat?
"""

import re
import sys


PATTERN = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(PATTERN, line):
        print(line)
