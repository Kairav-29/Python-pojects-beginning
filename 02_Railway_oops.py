class RailwayForm:
    formType = 'RailwayForm'
    def printData (self):
         print (f'Name is {self.name}')
         print (f'Name is {self.train}')

harrysApplication = RailwayForm ()
harrysApplication.name = 'Harry'
harrysApplication.train = 'Rajdhani Express'
harrysApplication.printData ()

         
