#WAP TO print iterate all numbers from list:
numbers = [1,2,3,4,5,6]
for num in numbers:
    print(num)

#WAP TO print square of all numbers:
numbers = [1,2,3,4,5,6]
for num in numbers:
    # print(num*num)
    # square = num*num
    square = num**2
    #print(square)
    print(f"Square of {num} is {square}")
    # print("square of number",num,"is",square)


#WAP TO print list of cube of all numbers:
numbers = [1,2,3,4,5,6]
cube = []
for num in numbers:
    cb = num**3
    cube.append (cb)
    # print(cube)
print(cube)


#WAP TO print Set of square of all numbers:
numbers = [1,2,3,4,5,6]
square = set()
for num in numbers:
    sq = num**2
    square.add (sq)
print(square)    

#---------------------------------------------------------------------------------------------
x = set()
print(type(x))

y = {}
print(type(y))
#---------------------------------------------------------------------------------------------

#WAP TO cal sum of all numbers from list:
numbers = [1,2,3,4,5,6]
sum = 0
for num in numbers:
    sum = sum + num
    print(sum)
print("Sum of all numbers is",sum)    

#---------------------------------------------------------------------------------------------

# addition of all salaries:
employee = [("raj", 20000), ("pranav", 40000), ("pranav", 50000)]
# total_salary = 0
# for name, salary in employee:
#     total_salary = total_salary + salary
# print(total_salary)    

total_sal = 0
for emp in employee:
    salary = emp [1]
    # print(salary)
    total_sal = total_sal + salary
    # print(total_sal)    

print("addition of all salaries is",total_sal)    
#---------------------------------------------------------------------------------------------


