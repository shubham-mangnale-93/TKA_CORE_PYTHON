# TASK 3: WAP TO CAL : MOVIE TICKET BILLING SYSTEM, A CINEMA HALL WANTS TO CALCULATE TOTAL TICKET COST.
# DETAILS : 
# Customer Name
# Number of tickets

#rules :
# Cost per ticket 250
# total cost = tickets * cost per ticket

#task :
# accept customer name and ticket count 
# calculate total cost 
# display details using f string
#-------------------------------------------------------------------------------------------------------
#data
name = input("Enter Customer Name: ")
tickets = int (input("Enter Number of Tickets: "))

#logic
cost_per_ticket = 250
total_cost = tickets * cost_per_ticket

#display
print(f"\nCustomer Name: {name},\nNumber of Tickets: {tickets},\nCost Per Ticket: {cost_per_ticket},\nTotal Cost: {total_cost}")


