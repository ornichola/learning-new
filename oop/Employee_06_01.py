# https://youtu.be/jCzT9XFZ5bw
# oop Employee.py without property methods


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Niko', 'Learner')

# Without sentence below output of $ python3 Employee.py will be:
# Niko
# Niko.Learner@company.com
# Niko Learner
emp_1.first = 'Jim'
# but with this sentence output will be:
# Jim
# Niko.Learner@company.com
# Jim Learner

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
