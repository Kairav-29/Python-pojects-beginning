# Wrong code (written by own a trial)
# def multiplication(n):
#     for i in range(1,11):
#       z= (f'{n} x {i} = {n*i}')

# for n in range (2,21):

#    a = multiplication(n)
#    with open(f'{n}.txt','a') as f:
#     f.write (str(a))
#   # print (a)

# Right Code
for i in range (2,21):
  with open (f"tables/Multiplicstion_of_{i}.txt",'w') as f:
    for j in range (1,11):
      f.write (f'{i} x {j} = {i*j}')
      if j!= 10:
        f.write ('\n')
  # break # if 2 table is printed it will break the program



