class Employee:
    company = 'Visa'
    ecode=120

class Freelancer:
    company = 'Fiverr'
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class Programmer (Employee, Freelancer):
    name = 'Rohit'

p = Programmer()
p.upgradelevel()
p.upgradelevel()
print (p.level)
print (p.company) # will run for first the Employee and then check for freelancer /if its written freelancer then will print fiverr first 