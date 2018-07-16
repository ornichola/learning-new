def adder01(good=0, bad=1, ugly=2):
    return


adder01(1)
adder01(2, 3)
adder01(2, 3, 5)
# adder(2, 3, 5, 9)  # TypeError: adder() takes from 0 to 3 positional arguments but 4 were given
adder01(good=0, bad=1, ugly=2)
adder01(good=1, bad=2, ugly=3)
adder01(bad=2, good=1, ugly=3)
adder01(ugly=1, good=2)
adder01(ugly='good', good='ugly')


def adder02(**kwargs):
    keys = list(kwargs.keys())
    if isinstance(kwargs[keys[0]], int) or isinstance(kwargs[keys[0]], float):
        summ = 0
    else:
        summ = kwargs[keys[0]][:0]
    for key in kwargs:
        summ += kwargs[key]
    return summ


print(adder02(one=1, two=2, three=3))
print(adder02(first='a', second='b', third='c'))
