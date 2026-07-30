# Task 4: Salary Slip Generator (basic)
# A company wants to generate a basic salary slip.

# Details:
# Employee Name Basic Salary

# Rules:
# HRA=  20% of Basic Salary
# DA = 10% of Basic Salary
# Gross Salary =Basic + HRA + DA

# Task:
# Write a Python program to:
# Accept employee name and basic salary
# Calculate HRA, DA, and gross salary
# Display salary slip using string formatting
#-------------------------------------------------------------------------------------------------------

name = input("Enter Employee name: ")
basic = float(input("Enter Basic Salary: "))

hra = basic * 20 /100
da = basic * 10 /100

gross = basic + hra + da

print (f"Employee Name: {name},\nBasic salary: {basic},\nHRA (20%): {hra},\nDA (10%): {da}, \nGross Salary: {gross}")