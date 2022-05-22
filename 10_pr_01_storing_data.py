class programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product= product

    def getinfo(self):
        print (f"The name of the {self.name} of {self.company} programmer is {self.name} and the product is{self.product}")
    

        #### wrong code written below
        # a = (f"{self.getinfo()}")
        # with open('Microsoft programmer.txt','a') as f:
        #     f.write(a)
        
    
harry = programmer("harry",'skype')

rajni = programmer('rajni','github')

kairav = programmer('kairav','msoffice')


a= harry.getinfo()
b= rajni.getinfo()
c= kairav.getinfo()



  




        