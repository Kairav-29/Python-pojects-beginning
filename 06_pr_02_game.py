# def game():
#     return 46


# score = game()
# with open ('hiscore.txt') as f:
#     hiscore = int(f.read())

# if hiscore<score :
#     with open ('hiscore.txt','w') as f:
#         f.write (str(score))

# with open ('hiscore.txt') as f:
#     a = f.read ()
# print (a)

# Including Blank also code
def game():
    return 11

score = game()
with open ('hiscore.txt') as f:
    hiscorest = f.read()

if hiscorest == "" :
    with open ('hiscore.txt','w') as f:
        f.write (str(score))

elif int(hiscorest)<score:
    with open ('hiscore.txt','w') as f:
        f.write (str(score))

with open ('hiscore.txt') as f:
    a = f.read ()
print (a)
