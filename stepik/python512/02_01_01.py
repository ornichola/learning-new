"""
[STEPIK]
Python: основы и применение https://stepik.org/512
02_01_01 Ошибки и исключения
"""

"""
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, 
ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
    
Подсказка: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


# invalid pretty solution due to grader logic
# try:
#     foo()
# except BaseException as e:
#     print(e.__class__.__name__)

# valid version of  pretty solution
# errors = (ZeroDivisionError, ArithmeticError, AssertionError)
# try:
#     foo()
# except errors as e:
#     print(e.__class__.mro()[ e.__class__ not in errors ].__name__)
