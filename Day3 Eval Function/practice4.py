#Task 2
# WAP TO CAL THE TOTAL COST OF TRAVELING A CERTAIN DISTANCE BY BIKE?

#DATA
distance = float (input("Enter distance (km) : "))
mileage = float (input("Enter bike mileage (km/l) : "))
petrol_price = float (input("Enter petrol price : "))

#logic
petrol = distance / mileage
total_cost = petrol * petrol_price

# print (total_cost)
print(f"Petrol Required: {petrol} litres, \nTotal Cost: Rs. {total_cost}")