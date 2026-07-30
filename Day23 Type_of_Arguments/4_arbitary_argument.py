'''
# Positional Arbitary Argument:----------->
# Explain Positional Arbitary Argument? 
Answer: 
This allows you to pass a variable number of positional arguments to the function. 
The *args syntax collects extra arguments as a tuple. 

Eg.,
def fname(*args):
        print(args)
fname(11,66,8)   #(11,66,8)
'''

# def add (*args):
#     print(args)
# add (10,20)  
# add (10,20,30)  
# add (10,20,30,40,50)  # store this element as a tuple.
#--------------------------------------------------------------------------------------------------

# def add (*args):
#     sum = 0
#     for num in args:
#         sum = sum + num
#     print(sum)
# add (10,20)  
# add (10,20,30)  
# add (10,20,30,40,50)
#--------------------------------------------------------------------------------------------------

'''
# Arbitrary Keyword Arguments:------->
# Explain Arbitrary Keyword Arguments (**kwargs)?
Answer:
     This allows you to pass a variable number of keyword arguments. 
     The **kwargs syntax collects extra arguments as a dictionary.
eg.
def show_info(**kwargs):
    print(kwargs)

show_info(name="Vaibhav", age=25, profession="Python Developer")
# Output:
{'name': 'Vaibhav','age': 25,'profession': 'Python Developer Trainer'}
'''

# def percentage (**kwargs):
#     print(kwargs)
# percentage (t1=80,t2=70,t3=92)    # store this element as a dictionary.
#--------------------------------------------------------------------------

def percentage (**kwargs):
    obt = 0
    for mk in kwargs.values():
        obt = obt + mk 
    print("Obtain Marks: ",obt)
    total = len(kwargs)*100
    print("Total Marks: ",total)
    per = obt / total * 100
    print("Percentage: ",per)   
percentage (t1=80,t2=70,t3=92) 
print("-"*60)
percentage (marathi=80,english=70,hindi=92,math=88,science=82,history=66) 
print("-"*60)
#---------------------------------------------------------------------------------------

def sum_of_numbers(*args, **kwargs):
    if args:
        print(args)
    else:
        print(kwargs)

sum_of_numbers(10, 20, 30)
sum_of_numbers(n1=10, n2=20, n3=30)

def sum_of_numbers(*args, **kwargs):
    total = 0
    if args:
        for num in args:
            total = total + num
        print(total)
    else:
        for num in kwargs.values():
            total = total + num
        print(total)

sum_of_numbers(10, 20, 30)
sum_of_numbers(n1=10, n2=20, n3=30)

# def sum_of_numbers(*args, **kwargs):
#     if args:
#         print(sum(args))
#     else:
#         print(sum(kwargs.values()))

#---------------------------------------------------------------------------------------

 






