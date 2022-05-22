# Use open finction to read the content of aa file!
# f = open ('sample.txt', 'r')


f = open('sample.txt','r')


f = open ('sample.txt') #by default the mode is r
# data = f.read()
data = f.read(5) # reads First five character from the file

print (data)
f.close