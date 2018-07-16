def copy_dict(d: dict) -> dict:
    copied_dict = dict()
    for k in d:
        if isinstance(d[k], dict):
            copied_dict[k] = copy_dict(d[k])
        else:
            copied_dict[k] = d[k]
    return copied_dict


print(copy_dict({'a': 1, 'b': 2, 'c': 3}))
print(copy_dict({'a': {'d': 0, 'b': 2}, 'b': 2, 'c': 3}))
