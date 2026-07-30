'''
# return statement in python:------>
# What is the return Statement in Python?
Answer:
The return statement in Python is used inside a function to send a value or result back to the caller of the function. 
It terminates the function's execution. If there's no return statement, the function returns None by default.

syntax:
python
def function_name(parameters):
    # Function body
    return value   # Sends 'value' back to the caller
    or
    return value1, value2, ...   # multiple values (tuple)

eg.
def square(num):
        return num**2
print(square(6))   #36

def calci(n1, n2):
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    return add, sub, mul, div

result = calci(10, 5)
print(result)   # (15, 5, 50, 2.0)   
'''
def percentage(obt,total):
    per = obt/total *100
    print("Hello")
    return per
    print ("Welcome")  # After return does not display program

print(percentage(340,500))
per = percentage(450,500)
print(per)
#-------------------------------------------------------------------------------------------

def calci(n1,n2):
    sum = n1+n2
    sub = n1-n2
    return sum,sub

print(calci(10,5))
result = calci(40,3)
print(result)


sum,sub = calci(30,5)
print(sum)
print(sub)
#-------------------------------------------------------------------------------------------






























