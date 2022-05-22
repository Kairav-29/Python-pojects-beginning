class Employee():
    salary = 100
    increment = 500

    @property
    def totalsalary (self):
        return self.salary + self.increment

    @totalsalary.setter
    def totalsalary (self, val):
        self.increment = val - self.salary

e = Employee()
e.totalsalary = 750
print (e.salary)
print (e.increment)