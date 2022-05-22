# a = int(input("Please input your 1st marks: "))
# b = int(input("Please input your 2nd marks: "))
# c = int(input("Please input your 3rd marks: "))

# z = ((a+b+c)*100/300)

# if (a>33 and b>33 and c>33 and z>40):
#     print ("Pass")
# else:
#     print("Fail")


# second approach
a = int(input("Please input your 1st marks: "))
b = int(input("Please input your 2nd marks: "))
c = int(input("Please input your 3rd marks: "))

if (a<33 or b<33 or c <33):
    print ("You are fail because you have less than 33% in one of the subject")
elif (a+b+c)/3 < 40:
    print ("You are fail due to total percentage less than 40")
else:
    print ("Cograts! you passed the exam")