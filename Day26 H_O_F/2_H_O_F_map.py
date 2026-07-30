'''
map:-
syntax:
    map(fun,iterable)
'''
numbers = [10,20,30,40,50]
print(list(map(lambda num: num+5,numbers)))
#-------------------------------------------------------------------------------------------------
# Square of all elements:-------->>
numbers = [10,20,30,40,50,60,70,80,90,100]
print(list(map(lambda num: num**2,numbers)))
#-------------------------------------------------------------------------------------------------

# Title of all elements in this list:-------->>
students = ["pravin sonwane", "rahul patil", "amit shinde", "sachin kadam", "mahesh kulkarni"]
print(list(map(lambda name: name.title(),students)))
#-------------------------------------------------------------------------------------------------

# Reverse of all elements in this list:-------->>
students = ["Pravin Sonwane", "Rahul Patil", "Amit Shinde", "Sachin Kadam", "Mahesh Kulkarni", "Snehal Deshmukh"]
print(list(map(lambda name: name[::-1],students)))
#-------------------------------------------------------------------------------------------------

#print dict of square of numbers:----->>
numbers = [1,2,3,4,5,6,7,8,9,10]
print(dict(map(lambda num:(num,num**2) ,numbers)))
#-------------------------------------------------------------------------------------------------
print("--"*60)
# print dict to rep total number of character --->> {"Pravin Sonwane : 11"}

students = ["Pravin Sonwane", "Rahul Patil", "Amit Shinde", "Sachin Kadam", "Mahesh Kulkarni", "Snehal Deshmukh"]
print(dict(map(lambda name: (name,len(name)) ,students))) 
# print total char with space <<-----

print("--"*60)
print(dict(map(lambda name: (name,len(name.replace(" ",""))) ,students))) 
# print total char without space <<-----
print("--"*60)

#-------------------------------------------------------------------------------------------------

# Method 1: Using a map + lambda function:----->>
marks = [20, 45, 78, 10, 90]
grace_marks = map(lambda mark: mark + 5, marks)
print(list(grace_marks))

# Method 2: Using a Normal Function:----->>
def add_grace(mark):
    return mark + 5

marks = [20, 45, 78, 10, 90]
result = map(add_grace, marks)
print(list(result))

#-------------------------------------------------------------------------------------------------

