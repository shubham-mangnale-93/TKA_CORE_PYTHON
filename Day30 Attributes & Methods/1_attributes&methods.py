# A) Instance Attributes:------->>>>>>
# Attributes are variables that store the data or properties of a class or an object.
# :Types of Attributes:------->>>>>
# 1) Instance Attributes → Belong to an object.
# 2) Class Attributes → Belong to the class and are shared by all objects.
'''
1) Instance Attributes:--->>
   Instance attributes are variables that belong to an object (instance). 
   They are defined using the self keyword and each object has its own copy of these attributes.
Syntax:--->>   
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

#------------------------------------------------------------------------------------------

class Book:
    #attributes--> variable --->store value
    def __init__(self, tit, pr):
        self.title = tit
        self.price = pr

b1 = Book("Python Programming", 899)
b2 = Book("Java Programming", 799)
print(b1.title)
#-------------------------------------------------------------------------------------------
''' 
# 2) Class Attributes:--------->>
'''
class Student:
    # class attributes
    course = "Python"
    institute = "TKA"
    trainer = "vaibhav"

    def __init__(self, nm, ag, tr):
        # instance attributes
        self.name = nm
        self.age = ag

s1 = Student("kunal", 23, "Vaibhav")
s2 = Student("vijay", 24, "Vaibhav")
print(s1.institute)
print(s2.institute)
print(Student.institute)
#-------------------------------------------------------------------------------------------

class Employee:
    # ---------- class attributes ----------
    # common values shared by all employees
    company_name = "Kiran Academy"
    owner_name = "kiran sir"
    location = "Karve nagar"
    pf = 12
    hra = 10
    da = 5

    def __init__(self, id, nm, dep, sal):
        # ---------- instance attributes ----------
        # unique values for each individual employee
        self.emp_id = id
        self.name = nm
        self.department = dep
        self.salary = sal

# ---------- creating objects ----------
e1 = Employee(101, "jay", "HR", 20000)
e2 = Employee(102, "ajay", "operation", 25000)

# ---------- 1. accessing instance attribute ----------
print("---- Instance attribute access ----")
print(e1.name)                 # jay

# ---------- 2. accessing class attribute (both ways) ----------
print("\n---- Class attribute access ----")
print(e1.company_name)         # via object -> Kiran Academy
print(Employee.company_name)   # via class  -> Kiran Academy

# ---------- 3. overwriting instance attribute (affects only that one object) ----------
print("\n---- Instance attribute overwrite ----")
e1.name = "pranav"
print(e1.name)                 # pranav   (changed)
print(e2.name)                 # ajay     (untouched)

# ---------- 4. modifying class attribute (affects all objects) ----------
print("\n---- Class attribute modification (via class name) ----")
Employee.location = "Nagpur"
print(e1.location)             # Nagpur
print(e2.location)             # Nagpur
#-------------------------------------------------------------------------------------------

class MobileShop:
    # ---------- class attributes ----------
    shop_name = "Sai Mobile World"
    owner_name = "Rajesh Sharma"
    location = "Camp Area, Pune"

    def __init__(self, brand, model, price, quantity):
        # ---------- instance attributes ----------
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

# ---------- creating objects ----------
mobile1 = MobileShop("Samsung", "Galaxy M14", 12000, 10)
mobile2 = MobileShop("Apple", "iPhone 13", 55000, 5)

# ---------- accessing instance attributes ----------
print(mobile1.brand)
print(mobile1.model)
print(mobile1.price)
print(mobile1.quantity)

print(mobile2.brand)
print(mobile2.model)

# ---------- accessing class attributes (both ways) ----------
print(mobile1.shop_name)
print(MobileShop.shop_name)
 
# ---------- updating instance attribute (affects only that one object) ----------
mobile1.price = 11500
print(mobile1.price)      # 11500 (updated)
print(mobile2.price)      # 55000 (unchanged)
 
 
# ---------- updating class attribute (affects all objects) ----------
MobileShop.location = "Kothrud, Pune"
print(mobile1.location)   # Kothrud, Pune
print(mobile2.location)   # Kothrud, Pune
#-------------------------------------------------------------------------------------------

class Mobile_shop:
    Shop_name = "SS"
    location = "Sangli"
    gst = 18

    def __init__(self,brand,model,price,ram,storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
        self.storage = storage

m1 = Mobile_shop("Samsung","Galaxy S24",75000,8,256)
m2 = Mobile_shop("Apple","iPhone16",90000,8,256)

print(Mobile_shop.Shop_name)
print(m1.brand)
#-------------------------------------------------------------------------------------------









