'''
*Flow Control Statements:----->
      "Flow Control Statements are statements that control the order of execution of a program. 
       They help the program make decisions, repeat a block of code,
       or change the normal flow of execution based on a condition."

*What is a Conditional Statement?
       "A Conditional Statement is used to make decisions based on a condition."
'''

# 1) if :---------------------->
'''
if: The if statement is used to execute a block of code only when the given condition is true.
syntax:
      if condition:
          #body|block
          #code
          
'''

# print ("start")
# num = int(input("Enter Number: "))
# if num>50:
#     print(f"{num} is GT 50")
# print("The End")    
# -----------------------------------------------------------------------------------------------

# print("TKA")
# password = input("Enter Your Password: ")
# if password == 12345:
#     print("Welcome TO DashBoard Page")      
# print("Thank You")    
# -----------------------------------------------------------------------------------------------

# numbers = [10,20,30,40,50,60,70,80,90,100]
# for num in numbers:
#     if num>50:
#         print(num)
# -----------------------------------------------------------------------------------------------
     

# numbers = [1,2,3,4,5,6,7,8,9,10]
# wap to iterate only even numbers from given list:
# for num in numbers:
#      if num%2==0:
#          print(num)  
# -----------------------------------------------------------------------------------------------

# numbers = [1,2,-3,4,5,-6,7,8,9,-10]
# wap to iterate only negative numbers from given list:
# for num in numbers:
    # if num < 0:
        # print(num)
# -----------------------------------------------------------------------------------------------

# numbers = [11,12,13,14,15,16,17,18,19,20]
# wap to iterate only sum of all odd numbers from given list:
# sum = 0
# for num in numbers:
#     if num%2 !=0:
        # print(num)
#         sum = sum + num
# print(sum)
# -----------------------------------------------------------------------------------------------

# students = ["vijay", "kunal", "vaibhav", "varun", "suraj", "vishal"]
# Print only students whose name starts with 'v'
# for student in students:
#     if student.startswith("v"):
#         print(student)

# for student in students:
#     if student[0] == "v":
#         print(student)        
# -----------------------------------------------------------------------------------------------

students = ["vijay", "kunal", "Vaibhav", "varun", "suraj", "Vishal"]
# WAP to iterate students whose name starts with 'v' or 'V'
# for student in students:
#     if student.lower().startswith("v"):
#         print(student)

# for student in students:
#     if student[0].lower()=="v":
#         print(student)

for student in students:
    if student[0] in "vV":
        print(student)
# -----------------------------------------------------------------------------------------------
