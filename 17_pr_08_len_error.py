class vector:
    def __init__(self,vec):
        self.vec = vec
    

    def __str__(self):
        str1 = ''
        index = 0 
        for i in self.vec:
            str1 += f'{i}a{index} +'
            index +=1
        return str1[:-1]   #these is called string slicing 

    def __add__(self,vec2):
        newlist = []
        if len (self.vec) == len (vec2.vec):
            for  i  in range (len(self.vec)):
               newlist.append (self.vec[i] + vec2.vec[i])
            return vector(newlist)
        else :
            print ('Please enter valid vector of same dimension')

    def __mul__(self,vec2):
        sum = 0
        if len (self.vec) == len (vec2.vec):
            for  i  in range (len(self.vec)):
                sum += self.vec[i] + vec2.vec[i]
            return sum 
        else :
            print ('Please enter valid vector of same dimension')

    def __len__(self):
        return len(self.vec)


v1 = vector ([1,4,5])
v2 = vector ([1,6,5])
print (v1+v2)
print (v1 * v2)