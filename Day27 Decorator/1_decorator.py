'''
Decorator:---->>

def deco(fun):       # fun takes as a argument and return fun
        def inner():
            pass
        return inner
'''

#-------------------------------------------------------------------------------------------------
# def extra(fun):
#     def inner():
#         fun()
#         print("Hello")
#     return inner

# @extra
# def printer():
#     print("Hello")
#     print("Hello")

# printer()
#-------------------------------------------------------------------------------------------------

#Write a Python program using a decorator that squares the result of add, subtract, multiply, and divide functions :-->>
# def square(fun):
#     def inner():
#         result = fun()     # calls the original add()
#         sq = result**2     # squares the result
#         return sq
#     return inner    

# @square
# def add():
#     num1 = int(input("Enter Num1: "))
#     num2 = int(input("Enter Num2: "))
#     sum = num1 + num2
#     return sum
# # print(add())

# @square
# def sub():
#     num1 = int(input("Enter Num1: "))
#     num2 = int(input("Enter Num2: "))
#     s = num1 - num2
#     return s

# @square
# def mul():
#     num1 = int(input("Enter Num1: "))
#     num2 = int(input("Enter Num2: "))
#     m = num1 * num2
#     return m

# @square
# def div():
#     num1 = int(input("Enter Num1: "))
#     num2 = int(input("Enter Num2: "))
#     d = num1 / num2
#     return d

# print(add())
# print(sub())
#-------------------------------------------------------------------------------------------------

# # Python Program to Convert Full Name to Title Case Using a Decorator:--->>

# def title_case(fun):          # decorator function, takes another function as input
#     def inner():              # wrapper function
#         result = fun()        # call original function
#         r = result.title()    # convert result to Title Case
#         return r              # return modified result
#     return inner              # return wrapper function


# @title_case                   # apply decorator -> full_name = title_case(full_name)
# def full_name():
#     first_name = input("Enter First Name: ")    # take first name input
#     middle_name = input("Enter Middle Name: ")  # take middle name input
#     last_name = input("Enter Last Name: ")      # take last name input

#     fname = f'{first_name} {middle_name} {last_name}'   # combine all names
#     return fname                                        # return combined name


# print(full_name())    # call decorated function and print result
#----------------------
# # Dry run:---->>
# # Method 1:
# inner = title_case(full_name)
# print(inner())    # output: Shubham Sanjay Mangnale

# # Method 2:
# full_name = title_case(full_name)
# print(full_name())  # output: Shubham Sanjay Mangnale

#-------------------------------------------------------------------------------------------------

# Python Program to Implement a Decorator with Parameters and Arguments (Full Name to Title Case):---->>
# parameter and argument ke help se:---->>
def title_case(fun):
    def inner(fn,mn,ln):          # fn, mn, ln = PARAMETERS
        result = fun(fn,mn,ln)    # fn, mn, ln = ARGUMENTS
        r = result.title()
        return r
    return inner 
@title_case
def full_name(name,mname,lname):          # name, mname, lname = PARAMETERS
    fname =  f"{name} {mname} {lname}"
    return fname

# inner = title_case(full_name)            # manually wrap full_name with decorator
# print(inner("ganesh", "ramesh", "patil"))   # pass required arguments <("ganesh", "ramesh", "patil")>

print(full_name("ganesh", "ramesh", "patil")) 

#-------------------------------------------------------------------------------------------------

# Python Program to Implement Login Authentication using a Decorator:----->>>

def login(fun):                              # decorator function, takes another function as input
    def inner():                             # wrapper function that checks login first
        username = input("Username: ")       # take username input
        password = input("Password: ")       # take password input
        if username == 'vaibhav' and password == "123":   # check credentials
            fun()                            # if correct, call the original function
        else:
            print("incorrect username or password")       # if wrong, show error message
    return inner                             # return the wrapper function


@login                                        # apply login decorator -> attendance = login(attendance)
def attendance():
    print("welcome to Attendance page")       # runs only if login is successful


@login                                        # apply login decorator -> testreport = login(testreport)
def testreport():
    print("welcome to testreport page")       # runs only if login is successful


@login                                        # apply login decorator -> livebatches = login(livebatches)
def livebatches():
    print("welcome to livebatches page")      # runs only if login is successful


attendance()                                  # call decorated function -> asks for login first

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# ==========================================
# Dictionary Data
# ==========================================

products_mrp = {
    "p1": 20000,
    "p2": 60000,
    "p3": 40000,
    "p4": 10000
}

# ==========================================
# Decorator Function
# Adds extra functionality before and after
# calling the original function.
# ==========================================

def offer(fun):

    def wrapper():

        print("========== OFFER STARTED ==========\n")

        # Call the original function
        result = fun()

        print("\n========== OFFER COMPLETED ==========")

        # Return the result received from
        # the original function
        return result

    # Return the wrapper function
    return wrapper


# ==========================================
# Apply Decorator
# ==========================================

@offer
def show_discount():

    print("Original Product Prices")
    print(products_mrp)

    # Get only price values
    prices = list(products_mrp.values())

    # Apply 10% discount using map() and lambda
    discounted_prices = list(
        map(
            lambda price: price - (price * 0.10),
            prices
        )
    )

    # Return discounted price list
    return discounted_prices


# ==========================================
# Function Call
# ==========================================

final_prices = show_discount()

print("\nDiscounted Prices")
print(final_prices)



























































