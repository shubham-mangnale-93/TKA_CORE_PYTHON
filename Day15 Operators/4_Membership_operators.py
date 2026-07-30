'''
Membership Operators : It is used to check whether a value is present
in a sequence (list, tuple, string, set, dictionary) or not.
It returns True or False.

1) in      -> Returns True if value is present in the sequence.
2) not in  -> Returns True if value is NOT present in the sequence.
'''
# name = "pavankumar"
# print("u" in name)          # True

# numbers = [10, 20, 30, 40, 50]
# print(35 not in numbers)    # True

# name = "pavankumar"
# print("x" not in name)      # True


# Examples:

fruits = ["apple", "banana", "mango", "grapes"]

print("banana" in fruits)      # True
print("orange" in fruits)      # False

print("orange" not in fruits)  # True
print("apple" not in fruits)   # False

# With string:
name = "Rushikesh"
print("Ru" in name)      # True
print("z" in name)       # False

# With tuple:
numbers = (10, 20, 30, 40)
print(25 in numbers)     # False
print(30 in numbers)     # True

# With dictionary (checks keys by default):
student = {"name": "Amit", "age": 21}
print("name" in student)     # True
print("Amit" in student)     # False (value आहे, key नाही)