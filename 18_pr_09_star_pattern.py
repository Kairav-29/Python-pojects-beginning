# Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))
ch = input("Please Enter any Character  : ")

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('%c' %ch, end = '  ')
        else:
            print(' ', end = '  ')
    print()
