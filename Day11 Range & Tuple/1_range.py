# RANGE--->
# range is used to generate a sequence of whole numbers (integers)

# RANGE SYNTAX:
# var = range(start_value, end_value, step_value)
# start_value ---> start 
# end_value ----> stop before end value
# step_value ----> diff 
# forward ----> +value
# reverse ----> -value 
#--------------------------------------------------------------------------------------------------

r1 = (1,6,1)
print(type(r1))
print(r1)

for num in r1:
    print(num)


#WAP TO ITERATE ALL NUMBER FROM 20 TO 10:
for num in range(20,9,-1):
    print(num)

#WAP TO PRINT ALL EVEN NUMBERS FROM 1 TO 10:
for num in range(2,11,2):
    print (num)   


#WAP TO PRINT ALL ODD NUMBERS FROM 22 TO 44:
for num in range(23,44,1):
    print (num)  

#WAP TO PRINT ALL EVEN NUMBERS FROM 100 T0 50:
for num in range(100,49,-2):
    print (num)      

for num in range(21):
    print(num)
   
#WAP to print total count of elements in given list:
numbers = [10,20,30,40,50,60,70]   
# count = len(numbers)
# print("Total count of elements:", count)

count = 0
for num in numbers:
    count = count + 1
print("Total no of element in list are :",count)

#WAP TO PRINT TOTAL SUM OF ALL NUMBERS 1-100:
sum = 0
for num in range(1,101):
    sum = sum + num
print("Total sum of all numbers 1-100:",  sum)    

#WAP TO CAL TOTAL COUNT OF ALL EVEN NUMBERS FROM 1 TO 100:
count = 0
for num in range(2,101,2):
    # print(num)
    count = count + 1
    # print(num)
print ("total count of all even number is",count)


#start = int(input("Enter Start Value"))
# stop = int(input("Enter Stop Value: "))
# for num in range(start, stop+1, 1):
#     print(num)
num1 = int(input("Enter start Number: "))
num2 = int(input("Enter End Number: "))
for num in range(num1,num2+1):
    print(num)