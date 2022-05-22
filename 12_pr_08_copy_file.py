with open ('this.txt') as f:
    t = f.read()

with open ("Copy.txt","w") as f:
    f.write (t)