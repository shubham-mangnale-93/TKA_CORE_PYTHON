# Task 11: Courier Charges Calculator
# A courier company wants to calculate courier charges.

# Details:
# Sender Name
# Parcel Weight (in kg)

# Rules:
# Charge per kg = ₹60
# Total Charge = Parcel Weight × Charge per kg

# Task:
# Write a Python program to:
# Accept sender name and parcel weight.
# Calculate the total courier charge.
# Display the bill using string formatting.
#-----------------------------------------------------------------------------------------------------
#logic
sender_name = input("Enter Sender Name: ")
parcel_weight = float(input("Enter Parcel Weight (in kg): "))

#logic
charge_per_kg = 60
total_charge = parcel_weight * charge_per_kg

#display
print("\n----- Courier Bill -----")
print(f"Sender Name: {sender_name}")
print(f"Parcel Weight: {parcel_weight} kg")
print(f"Charge Per Kg: ₹{charge_per_kg}")
print(f"Total Charge: ₹{total_charge}")