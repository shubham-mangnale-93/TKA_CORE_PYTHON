class Student:
    def __init__(self):
        print("hello i am init")

    def m1(self):
        print("welcome")
s1= Student()
# s1.m1()

#----------------------------------------------------------------------------------------------------

class Student:
    def __init__(self):
        print("init")
s1 = Student()
s1 = Student()                                    
s1 = Student()                                    
s1 = Student()                                    
s1 = Student()                                    
#----------------------------------------------------------------------------------------------------

class Student:
    def __init__(self):
        print(f'id of self is {id(self)}')

s1 = Student()
print(f'id of s1 is {id(s1)}')

print("-"*100)
s2 = Student()
print(f'id of s2 is {id(s2)}')
#----------------------------------------------------------------------------------------------------
print("-"*100)

class BankAccount:

    # Constructor is called automatically when an object is created.
    # 'self' refers to the current object.
    def __init__(self):

        # Print the memory address of the current object.
        print(f"ID of self is: {id(self)}")


# Create first object
account1 = BankAccount()

# Print the memory address of account1.
# It will be the same as self.
print(f"ID of account1 is: {id(account1)}")

print("-" * 50)

# Create second object
account2 = BankAccount()

# Print the memory address of account2.
# It will be the same as self.
print(f"ID of account2 is: {id(account2)}")
print("-" * 50)

#----------------------------------------------------------------------------------------------------


class Employee:
    def __new__(cls):
        print("new method")
        obj = super().__new__(cls)
        return obj
    
    def __init__(self):
        print("init method")
s1 = Employee()        

#----------------------------------------------------------------------------------------------------

