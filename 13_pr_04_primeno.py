b = int(input("Please enter your no: "))
prime = True
for i in range (2,b):
    if (b%i ==0):
        prime = False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")    