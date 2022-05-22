def remove_and_Strip (string,word):
    newStr = string.replace(word," ")
    return newStr.strip()

this = "     Harry is a good    "
n = remove_and_Strip (this,"Harry")
print (n)