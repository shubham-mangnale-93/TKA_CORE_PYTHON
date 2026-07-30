# Task 10: Water Bill Generator
# A municipal corporation wants to calculate the water bill.

# Details:
# Consumer Name
# Water Usage (in liters)

# Rules:
# Charge per liter = ₹2
# Total Bill = Water Usage × Charge per liter

# Task:
# Write a Python program to:
# Accept consumer name and water usage.
# Calculate the total water bill.
# Display the output using string formatting.
#---------------------------------------------------------------------------------------------------
#data
name = input("Enter Consumer Name: ")
water_usages = int(input("Enter Water Usage (in liters): "))

#logic
Charge_per_liter = 2
Total_Bill = water_usages * Charge_per_liter

#display
print ("\n----- Water Bill -----")
print(f"Consumer Name    : {name}")
print(f"Water Usage      : {water_usages} liters")
print(f"Charge Per Liter : ₹{Charge_per_liter}")
print(f"Total Bill       : ₹{Total_Bill}")