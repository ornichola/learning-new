def func(arg):
    print(arg)


func('string')                  # string
func(1)                         # 1
func(['a', 'b', 'c', 'd'])      # ['a', 'b', 'c', 'd']
func({'a': 1, 'b': 2, 'c': 3})  # {'b': 2, 'c': 3, 'a': 1}
# func()                          # TypeError: func() missing 1 required positional argument: 'arg'