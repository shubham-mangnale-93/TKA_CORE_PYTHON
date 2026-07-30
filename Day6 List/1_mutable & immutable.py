#Immutable :→ Once created,t it cannot be changed direcly. A new object is created instead.

institute = "the keeran academy"
ac = institute.replace("ee","i")
print(institute) #the keeran academy
print(ac) #the kiran academy
#---------------------------------------------------------------------------------------------------------

#Mutable :→ Once created, it can be changed directly. No new object is created.

numbers = [10,20,30,44,50,60]
print (id(numbers)) #2491935405248
numbers [3] = 40
print( numbers) #[10, 20, 30, 40, 50, 60]
print (id(numbers))  #3019243238592

