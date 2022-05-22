# class sample:
#     sample = 'harry'

# print (sample.sample)
# kairav = sample()
# kairav.sample = "kairav" #its an instance 

# sample.sample = "LOl"

# print (sample.sample)
# print (kairav.sample)

class sample:

    def __init__(slf,name): #we can change the self parameter to any but for common understanding we use self
        slf.name = name

obj = sample('Harry')

print (obj.name)

