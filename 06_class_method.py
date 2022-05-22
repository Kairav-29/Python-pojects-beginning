class Employee:
    company = 'Camel'
    salary = 100
    location = 'Delhi'

    # def changesalary(self,sal):          #These method change the class salary but its little lengthy way 
    #     self.__class__.salary = sal

    # def changesalary(self,sal):         # These method is an intance which does not change the class but change but change for the respective noun, 
    #     self.salary = sal

    @classmethod
    def changesalary(cls,sal): #these class method changes the employee class method directly 
        cls.salary = sal

e = Employee()
print (e.salary)
e.changesalary(455)
print (e.salary)
print (Employee.salary)
