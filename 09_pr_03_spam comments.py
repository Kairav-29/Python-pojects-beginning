
#cant be used as these can be only used if it has comed upto that words not other words
# b = input(" please enter from email")

# a = ["make a lot of money","buy now","subscribe this","click this"]

# if (b in a):
#     print ("scam")
# else:
#     print ("clear")


#Right one 

text = input ("Enter the text: ")

if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if (spam):
    print ("This text is spam")
else:
    print ("This is not spam")