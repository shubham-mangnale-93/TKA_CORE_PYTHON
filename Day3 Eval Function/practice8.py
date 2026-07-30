# Task 6: Fuel Cost Calculator
# A person wants to calculate total fuel cost.

# Details:
# Person Name
# Fuel Quantity (in liters)

# Rules:
# Cost per liter = â‚¹105
# Total Cost = Quantity Ã— Cost per liter

# Task:
# Write a Python program to:
# Accept name and fuel quantity
# Calculate total fuel cost
# Display details using string formatting
# ------------------------------------------------------------------------------------------------------
#data
name = input("Enter Person Name: ")
fuel_quantity = float(input("Enter Fuel Quantity (in liters): "))

#logic
cost_per_liter = 105
# Calculate total cost
total_cost = fuel_quantity * cost_per_liter

#display
print ("\n----- Fuel Cost Details -----")
print (f"Person Name: {name}")
print (f"Fuel Quantity: {fuel_quantity} liters")
print (f"Cost Per Liter: ₹{cost_per_liter}")
print (f"Total Fuel Cost: ₹{total_cost}")

