'''
# higher-order function:----->
A higher-order function in Python is a function 
that either takes one or more functions as arguments, returns a function as its result, or does both.
'''
#---------------------------------------------------------------------------------------------
# iterable means - sequence - collection of elements .
#---------------------------------------------------------------------------------------------


'''
filter(fun, iterable) ---> filter_obj

The filter() function takes a "fun" (a condition function) and applies it 
to every element of the given "iterable" (list, tuple, etc.). Only the 
elements for which "fun" returns True are kept, and the result is 
returned as a "filter object" (a lazy iterable).
'''
#---------------------------------------------------------------------------------------------

numbers = [1,2,-3,4,-5,6,7,-8,9,-10]
def ispositive(num):
    if num>0:
        return True
    else:
        return False

print(filter(ispositive,numbers))  #<filter object at 0x00000235AD421690>
print(list(filter(ispositive,numbers)))

#--------------------------------------------------------------------------------------------


numbers= [10,20,30,40,50,60,70,80,90]
def isgt(num):
    if num>50:
        return True
    else:
        return False

print(tuple(filter(isgt,numbers)))

#--------------------------------------------------------------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda num: num%2==0 ,numbers)))
#--------------------------------------------------------------------------------------------

students = ["kunal","Ishwar","kishor","pavan","kavita"]
print(list(filter(lambda name : name[0]=="k",students)))
#--------------------------------------------------------------------------------------------

numbers = [10,20,3,6,9,12,15,30,45,90,5,20]
#wap to filter elements --->divisible by 3 and 5
print(list(filter(lambda num: num%3==0 and num%5==0 , numbers)))
#--------------------------------------------------------------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda num: num%2!=0, numbers)))
#--------------------------------------------------------------------------------------------

print("--"*60)
# program, named function (def) using:----->
numbers = [1,2,3,4,5,6,7,8,9,10]
def iseven(num):
    if num%2==0:
        return True
    else:
        return False
def isodd(num):
    if num%2!=0:
        return True
    else:
        return False
even_list = list(filter(iseven, numbers))
odd_list = list(filter(isodd, numbers))

print("Even list:", even_list)
print("Odd list:", odd_list)
#--------------------------------------------------------------------------------------------

print("--"*60)
#program, nested def (using one function into another function):---->

numbers = [1,2,3,4,5,6,7,8,9,10]

def split_even_odd(nums):
    def iseven(num):
        if num%2==0:
            return True
        else:
            return False
    def isodd(num):
        if num%2!=0:
            return True
        else:
            return False
    even_list = tuple(filter(iseven,nums))    
    odd_list = tuple(filter(isodd,nums))  
    return even_list,odd_list

even_list,odd_list = split_even_odd(numbers)      
print("Even list:", even_list)
print("Odd list:", odd_list)
#--------------------------------------------------------------------------------------------

print("--"*60)
# using lambda function + filter :---->
numbers = [1,2,3,4,5,6,7,8,9,10]

even_list = set(filter(lambda num: num%2==0, numbers))
odd_list = tuple(filter(lambda num: num%2!=0, numbers))

print("Even list: ",even_list)
print("Odd list: ",odd_list)

print("Type of even_list:", type(even_list))
print("Type of odd_list:", type(odd_list))

#--------------------------------------------------------------------------------------------









