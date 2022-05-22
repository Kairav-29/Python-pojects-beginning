class Person:
    country = 'India'

    def takeBreath(self):
        print ('I am Breathing...')

class Employee(Person):
    company = 'Honda'

    def getsalary(self):
        print (f'Salary is {self.salary}')

    def takeBreath(self):
        print (f'I am Employee so i am luckily breathing..')

class Programmer (Employee):
    company = 'Fiverr'

    def getsalary(self):
        print (f'No salary to programmers')

    def takeBreath(self):
        print ('I am a Programmer so i am breathing ++..')

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()

# If we just dont add take breath attribute to any employee and programmer the command will take it from takebreath attribute of Person.