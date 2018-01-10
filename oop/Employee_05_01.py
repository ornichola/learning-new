# https://youtu.be/3ohzBxoFHAY
# oop __repr__ and __str__


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


emp_1 = Employee('Niko', 'Learner', 120000)
emp_2 = Employee('John', 'Smith', 100000)

print(emp_1)
print()
print(repr(emp_1))
print(str(emp_1))
print()
print(emp_1.__repr__())
print(emp_1.__str__())
