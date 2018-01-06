'''
It is a test block, let's try something.

>>> print(quick_math(3, 2, '+'))
5.0

>>> print(quick_math(1, 3, '-'))
-2.0

>>> print(quick_math(5, 10, '*'))
50.0

>>> print(quick_math(6, 4, '/'))
1.5

>>> print(quick_math(2, 6, '**'))
64.0

>>> print(quick_math(3, 2, 'unrecognizable'))
Cannot recognize operation
'''

def quick_math(a: float, b: float, oper: str) -> float:
    if oper == '+':
        return float(a + b)
    elif oper == '-':
        return float(a - b)
    elif oper == '*':
        return float(a * b)
    elif oper == '/':
        return float(a / b)
    elif oper == '**':
        return float(a ** b)
    else:
        return "Cannot recognize operation"

# this should be included for running tests from module
# and then script should be launched as:
# $ python3 modulename.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# or we can exclude last idiom and launch test using command:
# $ python3 -m doctest -v modulename.py
