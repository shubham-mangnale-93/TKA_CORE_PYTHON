'''
#scope /space

#global scope
x = 100
y = 200
def fun():
    #local scope
    a = 11
    b = 12

fun()

#global variable ---> x and y
#local variable --> a and b
'''
# global scope
x = 100
y = 200

def fun():
    # local scope
    a = 11
    b = 12
    y = 300
    print(a, b)  # we can access local variable within local scope
    print(x, y)  # we can access global variable within local scope
    print(y)     # 300

fun()
print(y)
#------------------------------------------------------------------------------

#global scope
x = 100
y = 200   #global variable
def fun():
    #local scope
    a = 11
    b = 12
    print(a)
    print(x)
    global y
    y=y+10     #new local variable
    print(y)

fun()
print(y)
#------------------------------------------------------------------------------

#global scope
x = 100
y = 200   #global variable
def fun():
    #local scope
    global y,x

    a = 11
    b = 12
    print(a)
    print(x)
    # global y,x
    y=y+10     #new local variable
    print(y)

fun()
print(y)
print(x)
#------------------------------------------------------------------------------

x = 100
def fun(n1, n2):
    global x 
    sum1 = n1 + n2
    return sum1

print(x)
x = fun(10, 20)
print(x)




















