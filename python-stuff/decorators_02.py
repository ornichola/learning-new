import time
import logging
from functools import wraps  # https://youtu.be/FsAPt_9Bf3U?t=24m16s


def time_me(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_before = time.time()
        func(*args, **kwargs)
        t_after = time.time()
        print('{func_name} runs {time:.2f} seconds'.format(func_name=func.__name__, time=(t_after - t_before)))
    return wrapper


@time_me
def something():
    for i in range(1000000):
        print(i)


something()


print()


def log_me(func):
    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return func(*args, **kwargs)

    return wrapper


@log_me
def display(name, age):
    print('I am {}, {} years old'.format(name, age))


display('Boris', 40)


print()


@log_me
@time_me
def display(name, age):
    time.sleep(5)
    print('I am {}, {} years old'.format(name, age))


display('Johh', 30)
