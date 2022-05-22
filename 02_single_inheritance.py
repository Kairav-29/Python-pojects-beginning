class Employee:
    company = 'Google'

    def showdetails (self):
        print ("This is an Employee")

class Programmer(Employee):
    language = 'Python'
    company = 'Youtube'

    def getlanguage (self):
        print (f'The language is {self.language}')

    def showdetails (self):
        print ('This is an programmer')

e = Employee()
e.showdetails()
p = Programmer ()
p.showdetails()
print (p.company)