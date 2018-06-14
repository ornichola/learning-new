from functools import lru_cache
"""
https://docs.python.org/3/library/functools.html#functools.lru_cache
Сохраняет результаты maxsize последних вызовов.
Это может сэкономить время при дорогих вычислениях, если функция периодически вызывается с теми же аргументами.
"""

@lru_cache(maxsize=None)
def fib(n):

    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(100)])
print(fib.cache_info())


print('-' * 79)


from functools import partial
"""
https://docs.python.org/3/library/functools.html#functools.partial
Used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting 
in a new object with a simplified signature.
"""

base_two = partial(int, base=2)
base_two.__doc__ = 'Convert base 2 string to an int'
print(base_two('10010'))


print('-' * 79)


from functools import partialmethod
"""
https://docs.python.org/3/library/functools.html#functools.partialmethod
Return a new partialmethod descriptor which behaves like partial except that it is designed to be used as
a method definition rather than being directly callable.
Descriptor - any object which defines the methods __get__(), __set__(), or __delete__().
"""

class Cell(object):


    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)  # False
c.set_alive()
print(c.alive)  # True


print('-' * 79)


from functools import singledispatch
"""
Transform a function into a single-dispatch generic function.
Generic function is a function composed of multiple functions implementing the same operation for different types. A function defined for polymorphism.
Single dispatch - a form of generic function dispatch where the implementation is chosen based on the type of a single argument.
"""


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


fun('Hi!', verbose=True)
fun(1337, verbose=True)
fun([0, 1, 2], verbose=True)
