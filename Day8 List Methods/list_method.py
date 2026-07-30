#mutable

#append--add data -- at end of the list.
numbers = [11,22,33,44,]

numbers.append(55)
print(numbers)
numbers.append("pankaj")
print(numbers)
#------------------------------------------------------------------------------------

#insert ---- index value

numbers = [10,20,30,50,60,70]
numbers.insert(3,40)
numbers.insert(0,5)
print(numbers)

numbers = [10,20,30,40,60,70,80]
numbers.insert(-3,50)
print(numbers)
#------------------------------------------------------------------------------------

#How to update data indexing and slicing :

#indexing:
numbers = [10,20,30,44,50,60]
#var [index] = [value]
numbers[3]=40
print(numbers)
numbers[1]=25
print(numbers)

#slicing:
numbers = [10,20,33,44,55,60,70]
#var [SI:EI:SV] = [values]
# numbers [2:5:1] = [30]
# print(numbers)

# numbers [2:5:1] = [30,40]
# print(numbers)
numbers [2:5:1] = [30,40,50]
print(numbers)
#------------------------------------------------------------------------
courses = ["Java Programming","DS","DA","WD"]
#var [index] = [value]
courses [0] = "JA"
print(courses)

courses_name = ["Java Programming","AWS","DS","DA","WD"]
courses_name [-3:] = ["Data science","Data analyst","Web development"]
print(courses_name)
#------------------------------------------------------------------------

#Delete -----> remove, pop, clear, del,...

#remove
numbers= [10,20,30,40,55,50,60]
numbers.remove(55)
print(numbers)

numbers = [10,20,30,40,50,20,60]
numbers.remove(20)
print(numbers) # first accurancy delete
#-------------------------------------------------------------

#pop
numbers = [10,20,30,40,50,20,60]
numbers.pop(-2)
print(numbers) # by using index number delete

numbers.pop() #-----> Last digit number delete
print(numbers)  
#---------------------------------------------------------------

p = ["raj","kunal","ajay","umesh"]
f = ["akansha","pranali","monali","rajesh"]

# name = f.pop(-1)
# p.append(name)
# print(f)
# print(p)

p.append(f.pop(-1))
print(f)
print(p)
#----------------------------------------------------------------

#clear
name = ["ram","kunal","ajay","umesh"]
name.clear()
print(name)
#-----------------------------------------------------------------

#remove
name = ["ram","kunal","ajay","umesh"]
name.remove("ram")
print(name)
#-----------------------------------------------------------------

#del 
# del----> indexing
num = [10,20,30,44,40,50,60]
del num[3]
print(num)

# del----> slicing
num = [10,20,30,1,2,3,4,40,50,60,70]
del num[3:7]
print (num)

#---------------------------------------------------------------------------



