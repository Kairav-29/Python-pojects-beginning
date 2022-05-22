#A Different Approach
# import random

# def rightguess (comp,you):
#     guesses = 0
#     while (you != comp):
#         if you != comp:
    
#             if comp > you:
#                 print ('higher number please.')
#                 guesses += 1

#             elif comp < you:
#                 print ('Lower number please.')
#                 guesses += 1
            
#             break


#         else :
#             print ('You guessed it right')

# print ('Computer Guesses the no')
# comp = random.randint(1,10)

# you = int(input ('Please Guess the no: '))
# a = rightguess(comp,you)


import random
randnumber = random.randint (1,100)
print (randnumber)
userguess = None
guesses = 0
while (userguess != randnumber):
    userguess = int (input('Enter your guess: '))
    if (userguess == randnumber):
        print ('You guessed it right!')

    elif (userguess > randnumber):
        print ('Lower number please')
        guesses += 1

    elif (userguess < randnumber):
        print ('higher number please')
        guesses += 1

print (f'Guesses you have made: {guesses+1}')

with open ('hiscoret.txt','r') as f:
    hiscore = int (f.read())

if (hiscore == ''):
    with open('hiscoret.txt','w') as f:
        f.write(guesses)

if (guesses < hiscore):
    print ('You have just broken the high score!')
    with open ('hiscoret.txt','w') as f:
        f.write(str(guesses))