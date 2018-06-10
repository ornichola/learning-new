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
