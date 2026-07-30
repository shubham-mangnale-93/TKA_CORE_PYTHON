# 2) if else :---------------------->
'''
if else:"The if-else statement is used to execute one block of code,
         if the condition is true and another block if the condition is false."
syntax:
      if condition:
          #if block
          #code 1
      else:
          #else block
          # code 2    
'''

# print("Start.....")
# num = eval(input("Enter Num: "))
# if num >= 50:
#     print(f"{num} is GT Or Equal To 50")
# else:
#     print(f"{num} is LT 50")
# print("Stop.....")
#-----------------------------------------------------------------------------------------------

# print("Start.....")
# num = eval(input("Enter Num: "))
# if num % 2 == 0:
#     print(f"{num} is Even Number")
# else:
#     print(f"{num} is Odd Number")
# print("Stop.....")
#-----------------------------------------------------------------------------------------------

# numbers = [1,2,3,4,5,6,7,8,9,10]
# # "WAP to print list of even numbers and list of odd numbers:
# odd_numbers = []
# even_numbers = []

# for num in numbers:
#     if num % 2 != 0:
#         odd_numbers.append(num)
#     else:
#         even_numbers.append(num)

# print(even_numbers)
# print(odd_numbers)
#-----------------------------------------------------------------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,10]
# WAP to find the sum of even numbers and sum of odd numbers from a given list.
even_sum = 0
odd_sum = 0
for num in numbers:
    if num%2==0:
        even_sum = even_sum+num
        # print(num)
    else:
        odd_sum = odd_sum+num
        # print(num)
print(even_sum)
print(odd_sum)