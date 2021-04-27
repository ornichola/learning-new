"""
[STEPIK]
Python: основы и применение https://stepik.org/512
02_04_01 Работа с файловой системой и файлами
"""

"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""

with open('02_04_01_input.txt', 'r') as f:
    lines = f.read().splitlines()

with open('02_04_01_output.txt', 'w') as f:
    f.write('\n'.join(reversed(lines)))