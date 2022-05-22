#  If else code
# n1 = int (input("Enter the 1st number: "))
# n2 = int (input("Enter the 2st number: "))
# n3 = int (input("Enter the 3rd number: "))

# if (n1>n2):
#     f1=n1
# else:
#     f1=n2

# if (f1>n3):
#     print ("the greater no is,",f1)
# else:
#     print("the greater no is ,",n3)

#  Function type Code
def maxium(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3

num1 = int (input("Please enter the 1st number: "))
num2 = int (input("Please enter the 2nd number: "))
num3 = int (input("Please enter the 3rd number: "))

m = maxium ( num1,num2,num3)
print("The Greatest number is " + str (m))
    