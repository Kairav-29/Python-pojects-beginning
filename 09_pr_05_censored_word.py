y = ["donkey","paap","lalu"]
with open ('censored.txt') as f:
    a= f.read ()
    for word in y:
      a= a.replace(word,"####")
      with open ('censored.txt','w') as f:
          f.write(a)
    
