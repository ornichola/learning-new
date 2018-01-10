# https://youtu.be/jCzT9XFZ5bw
# oop Employee.py with replaced by @property method variables


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@company.com'

    # removing instance variable emil and
    # replacing it with email() method with
    # decorated by @property will allow us
    # access email as attribute

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Niko', 'Learner')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
