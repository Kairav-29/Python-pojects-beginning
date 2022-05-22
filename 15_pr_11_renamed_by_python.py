import os  # os module immported to delete file from the computer

oldname = "sample2.txt"
newname = 'renamed_by_python.txt'

with open('sample2.txt') as f:
    content = f.read()

with open ('renamed_by_python.txt',"w") as f:
    f.write (content)

os.remove(oldname)
