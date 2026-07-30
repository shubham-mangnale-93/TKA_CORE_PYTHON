'''
Identity Operators : It is used to check whether two variables
point to the same object in memory or not (not just equal value,
but same memory location / identity).
It returns True or False.

1) is      -> Returns True if both variables refer to the same object.
2) is not  -> Returns True if both variables do NOT refer to the same object.
'''
# num1 = 100
# num2 = 100
# print(num1 == num2)   # True
# print(num1 is num2)   # True (small integers cached in memory)


# l1 = [10,20,30]
# l2 = [10,20,30]
# print(l1==l2)          # True  (values same)
# print(l1 is l2)         # False (different objects in memory)

# n1=10
# n2=10.0
# print(n1==n2)           # True  (value same, int vs float)
# print(n1 is n2)          # False (different types/objects)

# Examples:

a = 10
b = 10
print(a is b)          # True  (small integers are cached in memory)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)          # True  (values are same)
print(x is y)          # False (different objects in memory)

z = x
print(x is z)          # True  (z points to same object as x)

name1 = "hello"
name2 = "hello"
print(name1 is name2)  # True (strings can be interned/cached)

name3 = "hello world!"
name4 = "hello world!"
print(name3 is name4)  # False (usually, for longer/complex strings)

print(x is not y)      # True  (different objects)
print(x is not z)      # False (same object)