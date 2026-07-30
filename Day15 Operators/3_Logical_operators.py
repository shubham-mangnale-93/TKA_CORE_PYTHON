'''
Logical operators : It is used to combine two or more condition and return
True or False based on the result.

1) and  -> Both conditions must be True. If any one is False, result is False.
2) or   -> Any one condition True is enough. Result is False only if all are False.
3) not  -> Reverses the result. True becomes False, False becomes True.
'''
"""
# Examples:

a = 10
b = 20

print(a>5 and b>15)   # True and True  -> True
print(a>15 and b>15)  # False and True -> False

print(a>15 or b>15)   # False or True  -> True
print(a>15 or b>25)   # False or False -> False

print(not(a>5))       # not(True) -> False
print(not(a>15))      # not(False) -> True

"""

# marks = eval(input("Enter Your Marks: "))
# print(marks>90)

# no_t_mock = int(input("Topic Count: "))
# no_f_mock = int(input("Full syllabus Count: "))
# print(no_t_mock>10)
# print(no_f_mock >5)
# print("final result: ")
# print(no_t_mock>10 and no_f_mock >5)

# att = eval(input("Att: "))
# mock_count = int(input("Count: "))
# print(att > 95)
# print(mock_count>30)
# print(att > 95 or mock_count>30)