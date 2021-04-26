"""
[STEPIK]
Python: основы и применение https://stepik.org/512
02_04_02 Работа с файловой системой и файлами
"""

"""
Вам дана в архиве файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, 
в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
"""


import os


with open('02_04_02_dirs_with_py.txt', 'w') as f:
    dirs_with_py_files = set()
    for dir_path, _, filenames in os.walk('main'):
        for f_name in filenames:
            if f_name.endswith('.py'):
                dirs_with_py_files.add(dir_path)
    f.write('\n'.join(sorted(dirs_with_py_files)))
