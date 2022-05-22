with  open ('another.txt','w') as f:
    a = f.write ('these is how i can write the python')
    print (a)

with open('another.txt','r') as f:
    b = f.read()
    print (b)