'''
Comparison Operators : It is used to compare two values or expressions
and return True or False based on the comparison.

1) ==  -> Equal to           : True if both values are equal
2) !=  -> Not equal to       : True if values are NOT equal
3) >   -> Greater than       : True if left value is greater
4) <   -> Less than          : True if left value is smaller
5) >=  -> Greater than equal : True if left is greater or equal
6) <=  -> Less than equal    : True if left is smaller or equal
'''
# Examples:

# a = 10
# b = 20

# print(a == b)   # False
# print(a != b)   # True
# print(a > b)    # False
# print(a < b)    # True
# print(a >= 10)  # True
# print(b <= 20)  # True

# # With strings (comparison based on alphabetical/ASCII order):
# name1 = "apple"
# name2 = "banana"
# print(name1 == name2)   # False
# print(name1 < name2)    # True (a comes before b)

# # With float:
# x = 10
# y = 10.0
# print(x == y)     # True (value same)


a = 10
b = 20

print(a > b)     # False  -> Greater than (a मोठं आहे का)
print(a < b)     # True   -> Less than (a लहान आहे का)
print(a >= 10)   # True   -> Greater than or equal to
print(a <= 5)    # False  -> Less than or equal to
print(a == 10)   # True   -> Equal to (value सारखी आहे का)
print(a != b)    # True   -> Not equal to (value वेगळी आहे का)