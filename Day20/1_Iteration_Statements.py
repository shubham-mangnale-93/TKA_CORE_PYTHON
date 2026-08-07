# 1] For Loop:------------->
'''
A for loop is a looping statement. 
It is used to execute a block of code repeatedly for each item in a sequence,
like/such as a string, list, tuple, set, or dictionary.
'''
# for i in range(5):
#     print("SHIV")
#-------------------------------------------------------------------------------------------

# product = {}
# for i in range(3):
#     pname = input("Enter Pname: ")
#     mrp = eval(input("Enter MRP: "))
#     product[pname] = mrp
# print(product)
#-------------------------------------------------------------------------------------------


# 2] While Loop:------------->
'''
A while loop is a looping statement in Python.
It executes a block of code repeatedly as long as the given condition is True.
When the condition becomes False, the loop stops.
syntax:
i
while cond:
     # body while loop
     # update
'''

num = 1
while num<5:
    print("Hello User")
    num = num + 1
#-------------------------------------------------------------------------------------------

# attendance = []
# add = "yes"
# while add=="yes":
#     name = input("Enter Name: ")
#     attendance.append(name)
#     add = input("Do You Want to Add Another Student (yes/no): ")
# print(attendance)  
#-------------------------------------------------------------------------------------------

users = {"vaibhav":"1234","tushar":"345","pranav":"321"}

username = " "
password = " "
while username not in users or password != users[username]:
    username = input("Username: ")
    password = input("Password: ")
print(f"Hello {username}, Welcome to Dashboard")    
#-------------------------------------------------------------------------------

# ATM_PIN_PROGRAM:-->> USING while else in if else ---->>>

PIN = 123456
c = 0
while c!=3:
    c = c+1
    pin = int(input("Enter a PIN: "))
    if pin==PIN:
        print("Correct PIN")
        break
    else:
        print("Incorrect PIN")
else:
    print("Card Blocked")
#-------------------------------------------------------------------------------
