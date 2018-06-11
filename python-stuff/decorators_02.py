import time


def time_me(func):
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
