"""
Дана функция, которая ничего не делает случайное количество времени. Необходимо написать декоратор,
который считает и выводит на экран время выполнения этой функции.
"""

import random
import time


def timeit(f):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        f(*args, **kwargs)
        print(f'Function "{f.__name__}" took: {time.time() - time_start}')
    return wrapper

@timeit
def random_sleep():
    time.sleep(random.randint(0, 10))

random_sleep()

# timed = timeit(random_sleep)
# timed()
