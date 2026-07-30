#TUPLE:------>
'''
"It is comma sep value within ()."
#syntax:
    var = (v1,v2,v3,....)

'''
numbers = (10,20,30,40,50)
print(type(numbers))  #<class 'tuple'>

'''
tuple:---> It is ordered, immutable, heterogeneous collection of elements, duplicates are allowed.

'''

num = (1,2,3,4,5)
print(num)  #(1, 2, 3, 4, 5) ordered

# num[2] = 5
# print(num)  #TypeError: 'tuple' object does not support item assignment.---Immutable---
# not change/changeable.


x = (10,20.5,"om","true",False,[11,22,33],{1,2,3,4,5})
print(x)  #(10, 20.5, 'om', 'true', False, [11, 22, 33], {1, 2, 3, 4, 5}).
# heterogeneous collection of elements.

t1 = (10,20,20,30,30,30,40,50,30,40)
print (t1)  #(10, 20, 20, 30, 30, 30, 40, 50, 30, 40)
# duplicates are allowed.






