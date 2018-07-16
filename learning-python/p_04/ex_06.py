def add_dict(a: dict, b:dict) -> dict:
    summed = {}
    for k in a.keys():
        summed[k] = a[k]
    for k in b.keys():
        summed[k] = b[k]
    return summed


print(add_dict(
    {'a': 0, 'b': 1, 'c': 2},
    {1: 'd', 2: [0, 1]}
))
