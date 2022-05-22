with open ('donkey.txt') as f:
    a= f.read ()

    with open ('donkey.txt','w') as f:
        f.write(a.replace ('####','donkey'))
    
