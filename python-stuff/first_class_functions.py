"""
In computer science, a programming language is said to have first-class functions if it treats functions as
first-class citizens.
https://en.wikipedia.org/wiki/First-class_function

A first-class citizen (also type, object, entity, or value) is an entity which supports all the operations
generally available to other entities. These operations typically include being passed as an argument, returned from
a function, modified, and assigned to a variable.
https://en.wikipedia.org/wiki/First-class_citizen
"""


def square(x):
    return x * x


def cube(x):
    return x ** 3


def half(x):
    return x * 0.5


def my_map(func, args):
    args_mapped = []
    for arg in args:
        args_mapped.append(func(arg))
    return args_mapped


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print(my_map(half, lst))
print(my_map(square, lst))
print(my_map(cube, lst))


print()


def logger(msg):
    """Closure"""
    def log_msg():
        print('LOG:', msg)
    return log_msg


log_hi = logger('Greetings!')
log_hi()


print()


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


print_h1 = html_tag('h1')
print(print_h1)            # <function html_tag.<locals>.wrap_text at 0x7f5b312a7b70>
print_h1('Test Headline')  # !!! <h1>Test Headline</h1>
