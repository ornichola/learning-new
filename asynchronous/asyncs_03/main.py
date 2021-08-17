"""
Два текстовых файла
Вывести на экран их содержимое в соответствующих строках в виде кортежей
Если в каком-то файле не хватает строк - выводить None

"""

from itertools import zip_longest


def f_reader(f_name: str):
    for row in open(f_name, 'r'):
        row = row.replace('\n', '')
        yield row if row else None


for tpl in zip_longest(f_reader('sample_01.txt'), f_reader('sample_02.txt')):
    print(tpl)
