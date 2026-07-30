# Task 5: Area & Cost of Painting
# A house owner wants to calculate painting cost.

# Details:
# Owner Name
# Length of wall
# Breadth of wall

# Rules:
# Area = Length x Breadth
# Painting cost per sq unit = 15
# Total Cost = Area * Cost per unit

# Task:
# Write a Python program to:
# Accept details
# Calculate area and total cost
# Display output using string formatting
#--------------------------------------------------------------------------------------------------------
#data
name = input("Enter Owner Name: ")
length = float(input("Enter Length of Wall: "))
breadth = float(input("Enter Length of Wall: "))

#logic
area = length * breadth
cost_per_unit = 15
total_cost = area * cost_per_unit

#display
print("Owner Name: ",name)
print("Area of Wall: ",area)
print("Total painting cost: ",total_cost)
