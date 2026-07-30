'''
# Positional Arguments:---->
These arguments are passed to the function based on their position in the function call. 
The order in which the arguments are passed must match the order of the parameters in the function definition, 
and number of argument is equal to the number of parameter.
Eg,
def add(a, b):
    return a + b

result = add(5, 3)   # '5' is passed to 'a', '3' is passed to 'b'
print(result)   # Output: 8
syntax: 
    def function_name(p1, p2, ..., pN):
         # function body
           pass
    function_name(value1, value2, ..., valueN)
# positional :----> no.of parameter = no. of arguments
'''
# num  = 0              #1,(),(1,2),{},{1,2},[],[1,2,3]
# if num:
#     print("hello")
# else:
#     print("welcome")
#-----------------------------------------------------------------------------------

def full_name(fn,mn,ln):
    fname = f"{fn} {mn} {ln}"
    print(fname)
full_name("Pranav","Ramdas","Patil")    


def greet(name, age):
    print(name, age)

greet("Rahul", 25)   # order matters


 