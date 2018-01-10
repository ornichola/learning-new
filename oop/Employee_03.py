# https://youtu.be/rq8cL2XMM5M
# oop @classmethod and @staticmethod


class Employee:

    nums_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.nums_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Niko', 'Learner', 120000)
emp_2 = Employee('John', 'Smith', 100000)

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

emp_1.set_raise_amount(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Doe-90000'
emp_str_3 = 'Steve-Fisher-80000'

# Creating new instance using default constructor
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.fullname())

# Creating new instance using @classmethod constructor
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.fullname())

import datetime
my_date = datetime.date(2018, 7, 10)
print(Employee.is_workday(my_date))
