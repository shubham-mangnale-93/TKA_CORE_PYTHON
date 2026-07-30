#Q1- WAP TO PRINT FROM 1 TO 100 USING A FOR LOOP :
##range(start, stop)
# for num in range(1,101):
#     print(num)

#Q2- Print numbers from 10 to 1 using a for loop.
#range(start, stop, step)
# for num in range (100,0,-1):
#     print(num)

#Q3- Print all even numbers from 1 to 20 using a for loop.
# for num in range (2,21,2):
#     print(num)   

#Q4- Print all odd numbers from 1 to 20 using a for loop.
for num in range (1,21,2):
    print(num)

#Q5- Print all numbers from 1 to 50 that are divisible by 5.
for num in range (5,51,5):
    print(num)

#Q6- Take a number from the user and print numbers from 1 to that number using a for loop.
num = int(input("Enter a number: "))
for num in range(1,num+1):
    print(num)

for num in range (num,0,-1):
    print(num)   #6,5,4,3,2,
    
#Q7- Take a number from the user and print its multiplication table (1 to 10) using a for loop.
num = int(input("Enter a number: "))
for i in range (1,11):
    print(num,"x",i,"=",num*i)
   
#Q8- 