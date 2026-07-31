# TASK 1:---->
# Write a Python program to:
# 1. Accept marks of 5 students from the user
# 2. Store the marks in a list
# 3. Display all the marks
# 4. Calculate and display the total marks
# 5. Calculate and display the average marks

# # step 1:--------->
# marks = []

# # step 2:--------->
# for i in range(1,6):
#     # m = int(input("Enter five students of marks:" + str(i) + ":")) 
#     m = int(input(f"Enter marks for student {i}: "))
#     marks.append(m)
# print("All students Marks:",marks)

# # step 3:--------->
# total_marks = sum(marks)
# average = total_marks/len(marks)

# # step 3:--------->
# print("Total Marks:",total_marks)
# print("Average Marks:",average)
#---------------------------------------------------------------------------------------------

# # Task 2:---->
# Write a Python program to:
# 1. Accept the price of 6 products from the user
# 2. Store the prices in a list
# 3. Display all the product prices
# 4. Calculate and display the total bill amount
# 5. Calculate 18% GST on the total bill
# 6. Display the final bill amount (total + GST)

# prices = []

# for i in range(1,7):
#     p = eval(input(f"Enter The Price of Product {i}: "))
#     prices.append(p)
# print("All product prices:",prices)

# total_bill = sum(prices)
# gst = total_bill*18/100
# final_bill = total_bill + gst

# print("Total Bill Amount: ",total_bill)
# print("18% GST on the total bill:",gst)
# print("The Final Bill Amount:",final_bill)

# price=list()
# sum=0
# for i in range(1,7):
#     p=eval(input(f'enter price of product {i} ='))
#     price.append(p)
#     sum=sum+p
#     gst=sum*18/100
#     total_bill=sum+gst
# print(price)   
#---------------------------------------------------------------------------------------------

# Task 3:---->
"""
Write a Python program to:
1. Accept the salaries of 5 employees from the user
2. Store the salaries in a list
3. Display all the salaries
4. Calculate and display the total salaries
5. Calculate and display the average salary
6. Calculate and display the bonus (10% of each salary) for every employee
"""
# salaries = list()
# sum = 0
# for i in range(1,6):
#     s = eval(input(f'Enter the salary of emp {i} ='))
#     salaries.append(s)
#     sum = sum + s
#     avg = sum/len(salaries)

# print ("all salaries:",salaries) 
# print ("total salaries:",sum) 
# print ("average salary:",avg) 

# print("\nBonus for each employee:")

# i = 1

# for sal in salaries:
#     bonus = sal * 10 / 100
#     print(f"Employee {i} bonus: {bonus}")
#     i = i + 1

# salaries = []
# bonuses = []
# sum = 0

# for i in range(1, 6):
#     s = float(input(f"Enter the salary of emp {i} = "))
#     salaries.append(s)
#     sum = sum + s
    
#     bonus = s * 10 / 100
#     bonuses.append(bonus)
#     print(f"Employee {i} bonus: {bonus}")

# avg = sum / len(salaries)

# print("\nAll salaries:", salaries)
# print("Total salaries:", sum)
# print("Average salary:", avg)
# print("All bonuses:", bonuses)
#---------------------------------------------------------------------------------------------

# Task 4:---->
'''
Write a Python program to:
1. Accept the price of 8 products from the user
2. Store the prices in a list
3. Increase every product price by ₹100
4. Display the updated price list
'''
# prices = []
# for i in range(1, 9):
#     p = float(input(f"Enter price of product {i}: "))
#     prices.append(p)
# print("\nOriginal price list:", prices)

 
# for i in range(len(prices)):
#     prices[i] = prices[i] + 100
# print("Updated price list:", prices)


prices = []
for i in range(1, 9):
    p = float(input(f"Enter price of product {i}: "))
    prices.append(p)
print("\nOriginal price list: ",prices)

 
updated_prices = []
for p in prices:
    new_price = p + 100
    updated_prices.append(new_price)
print("Updated price list:", updated_prices)
