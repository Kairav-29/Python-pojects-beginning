u = input ("Please enter file name u want to match\n")
with open (u) as f:
    a = f.read()

v = input ("Please enter another file name u want to find identical\n")
with open (v) as f:
    b = f.read()

if a == b :
    print ('The files are identical')
else :
    print ('The files are not idential')