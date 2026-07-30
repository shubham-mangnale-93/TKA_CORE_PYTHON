'''
Lambda Function ??
------------------
lambda function in Python is a small, anonymous function 
that can have any number of arguments but can only execute a single expression.

single line
simple operations
lambda

syntax :
    lambda parameter : exp
'''

# def square(num):
#     sq=num**2
#     return sq
# print(square(4))

print((lambda num : num**2 )(7))

#---------------------------------------------------------------------------------------
# def add(n1,n2):
#     s = n1+n2
#     return s
# print(add(10,4))

print((lambda n1,n2 : n1+n2)(4,6))
#---------------------------------------------------------------------------------------

fullname = lambda fn,mn,ln : f'{fn} {mn} {ln}'
print(fullname("pavan","rajeshkumar","yadav"))
#---------------------------------------------------------------------------------------

calci1 = lambda n1,n2 : (n1+n2, n1-n2, n1*n2)
calci2= lambda n1,n2 : [n1+n2, n1-n2, n1*n2]
print(calci1(10,6))     # (16, 4, 60) stored as a tuple
print(calci2(10,6))     # [16, 4, 60] stored as s list

#---------------------------------------------------------------------------------------












