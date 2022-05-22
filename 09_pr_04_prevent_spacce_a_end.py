#  Function type code
# def s(n):
#     return (n*(n+1))/2

# n = int(input("Enter the no for sum of n natural numbers: "))
# v= s(n)
# print (v)

# Recursive Function code method
def sum_recursive(n):
    if n == 0 :
        return 0
    return (sum_recursive(n-1)+ n )


ns = int(input ("Enter the required sum of natural numbers:  "))
m = sum_recursive(ns)
print (f'The sum of first {ns} natural number is {m}')

