class calculator:

    def __init__(self,num):
        self.number = num  

    def square(self):
        print (f'The square of {self.number} is {self.number**2}')

    def cube(self):
        print (f'The square of {self.number} is {self.number**3}')

    def sqrt(self):
        print (f'The square of {self.number} is {self.number**0.5 }')
    
    @staticmethod
    def greet():
        print ("Hello")



num2 = calculator(2)
num2.greet()
num2.square()
num2.cube ()
num2.sqrt()
