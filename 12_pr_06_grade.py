a = int(input("PLease enter your marks"))
b = ("Your grade is ")
if (a>=90 and a<100):
    print(b + "Ex")
elif (a>=80 and a<90):
    print (b + "A")
elif (a>=70 and a<80):
    print (b + "B")
elif (a>=60 and a<70):
    print (b + "C")
elif (a>=50 and a<60):
    print (b + "D")
else:
    print (b+"F")

#second approach
a = int(input("PLease enter your marks"))
b = ("Your grade is ")
if a>=90:
    grade = "Ex"
elif a>=80:
    grade = "A"
elif a>=70:
    grade = "B"
elif a>=60:
    grade = "C"
elif a>=50:
    grade = "D"
else:
   grade = "F"

print ("your grade is "+grade)