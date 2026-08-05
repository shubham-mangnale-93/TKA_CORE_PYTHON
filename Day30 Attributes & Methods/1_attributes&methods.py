# A) Instance Attributes:---->>
'''
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
'''
class Student:
    #attributes
    def __init__(self, nm, ag):    # constructor + parameters
        #instance attributes
        self.name = nm    # instance attribute
        self.age = ag     # instance attribute

s1 = Student("vaibhav patil", 26)
s2 = Student("rahul patil", 30)
# print(s1.name)
# print(s1.age)
print(s2.name)
#------------------------------------------------------------------------------------------
#create a employee class with at least 4 instance attributes

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name              # instance attribute 1
        self.emp_id = emp_id          # instance attribute 2
        self.salary = salary          # instance attribute 3
        self.department = department  # instance attribute 4

# creating objects
e1 = Employee("Shivam Patil", 201, 55000, "Finance")
e2 = Employee("Omkar Patil", 202, 48000, "Marketing")

# accessing attributes
print(e1.name)
print(e1.emp_id)
print(e1.salary)
print(e1.department)

print(e2.name)
print(e2.emp_id)
print(e2.salary)
print(e2.department)