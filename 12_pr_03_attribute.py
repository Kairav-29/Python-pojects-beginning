class a:
    a=1 # its an class attribute 
    
kairav = a()
kairav.a = 100 # its an instance which only changes the attribute for the kairav only

a.a=2 #these is how we can change the class attribute

print (a.a)
print (kairav.a)