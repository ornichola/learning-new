def outer():
    msg = 'Greetings!'

    def inner():
        print(msg)
    return inner()


a = outer()  # Greetings!
print(a)     # None


def outer():
    msg = 'Greetings!'

    def inner():
        print(msg)
    return inner


a = outer()  #
print(a)     # <function outer.<locals>.inner at 0x7f05d0211840>
a()          # Greetings!


print()


def outer(msg):
    message = msg

    def inner():
        print(message)

    return inner


hi_func = outer('Hi!')
greet_func = outer('Hello!')

hi_func()
greet_func()
