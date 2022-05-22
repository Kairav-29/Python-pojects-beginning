a= int(input("please enter 1st number: "))
b= int(input("please enter 2nd number: "))
c= int(input("please enter 3rd number: "))
d= int(input("please enter 4th number: "))

if (a>b):
    f1 = a
else:
    f1 = b

if (c>d):
    f2 = c
else:
    f2 = d 

if (f1 > f2):
    print (str(f1)+"is greater")
else:
    print (str(f2)+"is greater")
