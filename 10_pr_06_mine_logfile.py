

with open ('log.txt') as f:
    t = f.read().lower()
    if 'python' in t:
        print ('Yes python is present')
    else:
        print ('Python is not present')

# second way
with open ('log.txt') as f:
    t = f.read()
    if 'python' in t.lower():
        print ('Yes python is present')
    else:
        print ('Pyton is not present')