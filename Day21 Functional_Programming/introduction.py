# 1] Functional Programming:-------->
'''
# Function :----> function is a reusable block of code.
# function definition
# syntax:---->
        def frame:
            #block
            #code

# calling

# What is functional programming?
: Functional programming in Python is a programming paradigm that treats functions as the main building blocks to solve problems. 
It emphasizes:
Writing independent functions that don't rely on or modify external state (pure functions).
Using immutable data, meaning data cannot be changed after it is created.
Applying higher-order functions like map, filter, and reduce to process data.

# what is function?
: A function is a reusable block of code that performs a specific task. 
Instead of repeating code, you can define a function once and call it whenever needed. 
Functions can take inputs (arguments), perform operations, and return outputs.
'''
# wap to cal factorial of num:

# def factorial():
#     num = int(input("Enter Number: "))
#     fact = 1
#     for num in range(1,num+1):
#         fact = fact*num
#     print(f"factorial of {num} is {fact}")   
# factorial()


# wap to check is armstrong or not:

# num = int(input("Num: "))
# snum = str(num)
# n = len(snum)
# sum = 0
# for i in snum:
#     sum = sum + int(i)**n
# if num == sum:
#     print("armstrong")
# else:
#     print("Not")



# def isarmstrong():
#     num = int(input("Num: "))
#     snum = str(num)
#     n = len(snum)
#     sum = 0
#     for i in snum:
#         sum = sum + int(i)**n
#     if num == sum:
#         print("armstrong")
#     else:
#         print("Not") 
# isarmstrong()        

#--------------------------------------------------------------------------------------------
'''
#parameter and arguments
#function ----> operation ---> data

def funame(parameter):     #variable
    #body | block
    #operation ---> data

funame(arguments)

def funame(p1, p2, p3):    #parameter
    #operations

funame(v1, v2, v3)         #arguments    
'''

#create a fun TO cal num of two number

# def sum(n1, n2):    #parameters
#     result = n1 + n2
#     print(result)

# sum(10, 4)   #arguments


#create a function to print email add.
# def create_email(fn, ln, cn):   #parameter
#     email = f'{fn}_{ln[0]}@{cn}.com'
#     print(email)

# create_email("vaibhav", "patil", "tka")   #arg.

#---------------------------------------------------------------------------------------------

#create a function to check number is perfect or not:---->

#create a function to check number is perfect or not

def check_perfect(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total = total + i
    
    if total == number:
        return True
    else:
        return False

# Function call करून check करणे
num = int(input("Enter a number: "))

if check_perfect(num):
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")

















