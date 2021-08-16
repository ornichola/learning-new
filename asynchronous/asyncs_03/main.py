def f_reader(f_name: str):
    for row in open(f_name, 'r'):
        row = row.replace('\n', '')
        yield row if row else None


for tpl in zip(f_reader('sample_01.txt'), f_reader('sample_02.txt')):
    print(tpl)
