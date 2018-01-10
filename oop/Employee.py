class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Niko', 'Learner')

emp_1.fullname = 'John Doe'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
