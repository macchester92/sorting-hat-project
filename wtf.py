class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1


    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

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



emp_1 = Employee('Viktor', 'Radchenko', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname = 'Ahahaha Bugagaga'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
