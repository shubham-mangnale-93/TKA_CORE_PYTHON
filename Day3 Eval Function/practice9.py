# Task 8: Online Food Order Bill
# A food app wants to generate a bill.

# Details:
# Customer Name
# Food Item Price

# Rules:
# Delivery Charge = ₹40
# GST = 5% of Food Price
# Total Bill = Food Price + GST + Delivery Charge

# Task:
# Write a Python program to:
# Accept customer name and food item price.
# Calculate GST and total bill.
# Display the bill using string formatting.
#--------------------------------------------------------------------------------------------------
#data 
name = input("Enter Customer Name: ")
food_price = float(input("Food Item Price: "))

#logic
delivery_charge = 40
gst = food_price * 5/100
total_bill = food_price + delivery_charge + gst

#display
print ("\n----- Food Order Bill -----")
print (f"Customer Name: {name}")
print (f"Food Price: {food_price}")
print (f"Delivery Charges: {delivery_charge}")
print (f"Gst (5%): {gst}")
print (f"Total Bill: {total_bill}")