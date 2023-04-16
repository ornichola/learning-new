"""
Написать контекстный менеджер, который принимает имя. При входе в контекст - печатается приветствие по
переданному имени. В тело контекста должно вернуться переданное имя в верхнем регистре.
В теле контекста необходимо распечатать каждую букву (вернувшегося в верхнем регистре имени) 3 раза.
При выходе из контекста - печатается прощание по переданному имени.
Задание необходимо реализовать двумя способами: и с помощью класса и без использования класса.
"""


from contextlib import contextmanager

@contextmanager
def name_triple(name: str):
    print(f'Привет, {name}')
    yield name
    print(f'Пока, {name}')

with name_triple('Степан') as nt:
    for letter in nt:
        print(letter.upper() * 3)


class NameTriple:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f'Привет, {self.name}')
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Пока, {self.name}')


with NameTriple('Иван') as nt:
    for letter in nt:
        print(letter.upper() * 3)
