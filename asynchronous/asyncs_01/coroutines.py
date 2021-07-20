def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'ready to accept message'
    message = yield x
    print('Subgen received', message)


@coroutine
def avg():
    count = 0
    summ = 0
    avg = None
    while True:
        try:
            x = yield avg
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            avg = round(summ / count, 2)


class SomeException(BaseException):
    ...


def subgen():
    while True:
        try:
            message = yield 
        except StopIteration:
            print('stopped')
            break
        else:
            print('....', message)
    return 'Returned from subgen'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except SomeException as e:
    #         g.throw(e)
    result = yield from g
