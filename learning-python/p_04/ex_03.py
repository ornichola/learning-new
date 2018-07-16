def adder(*args):
    if isinstance(args[0], int) or isinstance(args[0], float):
        summ = 0
    else:
        summ = args[0][:0]
    print('summ', summ)
    sum(args)
    for arg in args:
        summ += arg
    return summ


print(adder('hello', ' world', '!'))
print(adder('hello world!'))
print(adder([0], [1], [2], ['a', 'b', 'c']))
print(adder(1, 2, 3, 4))
print(adder(3.25, 7.45, 2))
print(adder(1.02))
