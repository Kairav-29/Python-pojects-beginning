class animals:
    animaltype = 'Mammal'

class pets(animals):
    colour = 'white'

class dog(pets):
    @staticmethod
    def bark():
        print ('Bow bow!')

d = dog()
d.bark()