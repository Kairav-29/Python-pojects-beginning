class Train:

    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print (f"The name of the train is {self.name}")
        print (f"The seats available in the train are {self.seats}")

    def fareinfo(self):
        print (f'The price of the ticket is: Rs. {self.fare}')

    def bookticket(self):
        if (self.seats > 0):
            print (f'Your ticket is booked and the ticket no. is {self.seats}')
            self.seats = self.seats - 1
        else :
            print ("The train is full")

    def cancelticket(self,seatno):
        self.seatno = seatno
        with open ('Railway seats.txt','w') as f:
            f.write(str(self.seats))
        if str(self.seatno) in "Railway seats.txt":
            # seatno = int (input ('Please enter yout seat no.which has to be cancelled')) #We already have asked seatno by parameter no  need to write these line
            print ('Your ticket is not valid')

        else:
            with open ('Railway seats.txt','a') as f:
                self.seats = self.seats + 1
                f.write (str(self.seatno))
                
                    
intercity = Train('Intercity Express: 14015',90,2)
intercity.getStatus()
intercity.fareinfo()
intercity.bookticket()
intercity.bookticket()
intercity.cancelticket(1)
# intercity.bookticket()
intercity.getStatus()

