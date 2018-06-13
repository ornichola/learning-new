def deco_01(f):
    def wrapper():
        print('BEFORE')
        return f()
    return wrapper


@deco_01
def say():
    print('Hi!')


say()


print()


def deco_02(f):
    def wrapper(name):
        print('BEFORE')
        f(name)
        print('AFTER')
    return wrapper


@deco_02
def say(name):
    print('Hi,', name)


say('Niko')


print()


def deco_03(f):
    def wrapper(*args, **kwargs):
        print('BEFORE')
        f(*args, **kwargs)
    return wrapper


@deco_03
def say(name, last_name):
    print('Hi,', name, last_name)


say('Niko', 'O')


print()


class DecoratorClass(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)


@DecoratorClass
def display():
    print('display function ran')


display()
