import math
import time


REPS = 1000


def timer(func, *args, reps=REPS, **kwargs):
    start = time.time()
    for i in range(reps):
        func(i)
    elapsed = time.time() - start
    return elapsed


def pow01(x):
    return math.sqrt(x)


def pow02(x):
    return x ** .5


def pow03(x):
    return pow(x, .5)


print(timer(pow01))
print(timer(pow02))
print(timer(pow03))
