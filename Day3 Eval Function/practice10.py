# Task 9: Room Rent Calculation
# A hotel wants to calculate room rent.

# Details:
# Guest Name
# Number of Days

# Rules:
# Rent per day = ₹1800
# Total Rent = Number of Days × Rent per day

# Task:
# Write a Python program to:
# Accept guest name and number of days.
# Calculate the total room rent.
# Display the bill using string formatting.
#------------------------------------------------------------------------------------------------------
#data
name = input ("Enter Guest Name: ")
days = int(input("Enter Number Of Days: "))

#logic
Rent_per_day = 1800
Total_Rent = days * Rent_per_day

#display
print ("\n----- Room Rent Bill -----")
print(f"Guest Name   : {name}")
print(f"Days Stayed  : {days}")
print(f"Rent Per Day : ₹{Rent_per_day}")
print(f"Total Rent   : ₹{Total_Rent}")