'''
User Story
Bank ke paas customers ka transaction data hai.
Har customer ka account number unique hai.

Bank ko ye kaam karna hai:
1. Har customer ka total balance calculate karna hai.
2. Suspicious transactions identify karni hain.
3. Duplicate transaction IDs remove karne hain.
4. Minimum balance maintain nahi karne wale customers find karne hain.
5. Har customer ka last 3 transactions reverse order me print karna hai.
'''
bank_customers = {
    1001: {
        "name": "Amit",
        "account_type": "Savings",
        "branch": ("Pune", "FC Road"),
        "transactions": [5000, -1000, -500, 2000, -7000, 3000],
        "transaction_ids": {"TXN101", "TXN102", "TXN103", "TXN102"}
    },
    1002: {
        "name": "Ravi",
        "account_type": "Current",
        "branch": ("Mumbai", "Andheri"),
        "transactions": [10000, -2000, -1500, -12000, 5000],
        "transaction_ids": {"TXN201", "TXN202", "TXN203", "TXN204"}
    },
    1003: {
        "name": "Sneha",
        "account_type": "Savings",
        "branch": ("Pune", "Kothrud"),
        "transactions": [3000, -500, -700, 1000, -200],
        "transaction_ids": {"TXN301", "TXN302", "TXN301", "TXN303"}
    }
}

# print (len(bank_customers))
# print (type(bank_customers))


# savings_count = 0
# current_count = 0

# for cust_id, details in bank_customers.items():
#     if details["account_type"] == "Savings":
#         savings_count = savings_count + 1
#     elif details["account_type"] == "Current":
#         current_count = current_count + 1

# print("Total Savings Accounts:", savings_count)
# print("Total Current Accounts:", current_count)
#-----------------------------------------------------------------------------------

# finaloutput = set()
# for key,val in bank_customers.items():
#     # print(key)
#     # print(val)
#     # print(val["account_type"])
#     # finaloutput.add(val["account_type"])
#     acctype = val["account_type"]
#     finaloutput.add(acctype)
# print(finaloutput)
#-----------------------------------------------------------------------------------

#1. Har customer ka total balance calculate karna hai :---->
# for cust_id, details in bank_customers.items():
#     # print(details)
#     total=0
#     for txn in details["transactions"]:
#         total= total+txn
#     print(f"{cust_id} - {details['name']}: Total Balance = {total}")
#-----------------------------------------------------------------------------------

# finaltype = set()

# for custid, dataofcust in bank_customers.items():
#     transactionsvalues = dataofcust["transactions"]
#     total = 0
#     for txn in transactionsvalues:
#         total = total + txn 
#     print(f"name >> {dataofcust['name']} ke transaction {transactionsvalues} total >> {total}")
    

#-----------------------------------------------------------------------------------

#2. Suspicious transactions identify karni hain :---->
# threshold = -5000
# for cust_id, details in bank_customers.items():
#     for txn in details["transactions"]:
#         if txn < threshold:
#             print(f"Suspicious Transaction Found -> Customer: {details['name']} (ID: {cust_id}), Amount: {txn}")
#-----------------------------------------------------------------------------------
# susp_amount = 3000
# allsuptransactions = list()

# for custId, custData in bank_customers.items():
#     transactionvalues = custData["transactions"]
#     for transvalue in transactionvalues:
#         if transvalue > susp_amount:
#             allsuptransactions.append(transvalue)
# print(allsuptransactions)
#-----------------------------------------------------------------------------------

#3.Duplicate transaction IDs remove karne hain:----->

# for custId, custData in bank_customers.items():
#     transaction_ids = custData["transaction_ids"]
#     unique_ids = set(transaction_ids)
#     print(f"{custData['name']} ke unique transaction IDs >> {unique_ids}")
#-----------------------------------------------------------------------------------
# for custId, custData in bank_customers.items():
#     transaction_ids = custData["transaction_ids"]
#     print(transaction_ids)
#-----------------------------------------------------------------------------------

#4.Minimum balance maintain nahi karne wale customers find karne hain.
# min_balance = 1000

# for custId, custData in bank_customers.items():
#     total = sum(custData["transactions"])
#     if total < min_balance:
#         print(f"{custData['name']} (ID: {custId}) minimum balance maintain nahi kar raha, Balance = {total}")
#-----------------------------------------------------------------------------------

# minbalance = 300

# for custId, custData in bank_customers.items():
#     transactionvalues = custData["transactions"]
#     custname = custData["name"]
#     totalbalacceneOfcust = sum(transactionvalues)
#     if totalbalacceneOfcust < minbalance:
#         print(custname)
#         print(f"customer name >> {custname} and his balance is >> {totalbalacceneOfcust}")
#-----------------------------------------------------------------------------------

#5.Har customer ka last 3 transactions reverse order me print karna hai.:----->

# for custId, custData in bank_customers.items():
#     transactionvalues = custData["transactions"]
#     print("-> Last 3 Transactions (Reverse Order): ",transactionvalues[-1:-4:-1])
#-----------------------------------------------------------------------------------

# for custId, custData in bank_customers.items():
#     transactionvalues = custData["transactions"]      
#     custname = custData["name"]                        

#     last_three_reversed = transactionvalues[-1:-4:-1]  # last 3 transactions, reverse order  

#     print(f"Customer: {custname} (ID: {custId}) -> Last 3 Transactions (Reverse Order): {last_three_reversed}")    
#-----------------------------------------------------------------------------------
'''
Task #1: Print all customer names.
Task #2: Print all Savings account customers.
Task #3: Print balance of each customer.
Task #4: Print customers whose balance is below minimum balance.
Task #5: Print suspicious transactions above ₹5000 withdrawal.
Task #6: Print last 3 transactions of every customer in reverse order.
Task #7: Print transaction IDs of every customer.
Task #8: Print Pune branch customers.
Task #9: Print risk category of every customer.
Task #10: Print final bank summary.


dict = account wise customer data
list = transactions
set = unique transaction IDs
tuple = fixed branch information
range = index-based transaction processing
if = banking conditions
for = process all customers and transactions
'''
# Task #1: Print all customer names.:---->
print("Task #1: All Customer Names".center(60,"="))
for customer in bank_customers.values():
    # print(customer)
    print(customer["name"])

# Task #2: Print all Savings account customers.
print("Task #2: All Saving Account Customers".center(60,"="))
for customer in bank_customers.values():
    if customer["account_type"] == "Savings":
        print(customer["name"])

# Task #3: Print balance of each customer.
print("Task #3: Balance of Each Customers".center(60,"="))
balances = {}
for customer in bank_customers.values():
    balance = customer["transactions"]
    total = 0
    for amount in balance:
        total+=amount
    balances[customer["name"]] = total    
    # print(total)
    print(customer["name"], ":",total)    

# Task #4: Print customers whose balance is below minimum balance.:---->
print("Task #4: Customer Below Minimum Balance".center(60,"="))
min_balance = 1000
for customer in bank_customers.values():
    balance = sum(customer["transactions"])                 
    # print(balance)
    if balance<1000:
        print(customer["name"],":", balance)

# Task #5: Print suspicious transactions above ₹5000 withdrawal.:---->
print("Task #5: Suspicious Transactions above ₹5000 withdrawal".center(90,"="))
for customer in bank_customers.values():
    for txn in customer["transactions"]:
        if txn < -5000:
            print(customer["name"],":", txn)

# Task #6: Print last 3 transactions of every customer in reverse order.:---->
print("Task #6: last 3 Transactions of Every Customer in Reverse Order".center(90,"="))
for customer in bank_customers.values():
    print(customer["name"],customer["transactions"][-1:-4:-1])

# Task #7: Print transaction IDs of every customer.:---->
print("Task #7: Transaction IDs of Every Customer".center(90,"="))
for customer in bank_customers.values():
    print(customer["name"],customer["transaction_ids"])

# Task #8: Print Pune branch customers.:---->
print("Task #8: Print Pune Branch Customers".center(60,"="))
for customer in bank_customers.values():
    if customer["branch"] [0] == "Pune":
        print(customer["name"], customer["branch"])

# Task #9: Print risk category of every customer.:----->
print("Task #9: Print Risk Category of Every Customers".center(60,"="))
MIN_BALANCE = 1000
for customer in bank_customers.values():
    balance = sum (customer["transactions"])

    if balance < 0:
        print(customer["name"],":", "High Risk")
    elif balance < MIN_BALANCE:
        print(customer["name"],":", "Medium Risk")
    else:
        print(customer["name"],":", "Low Risk")

# Task #10: Print final bank summary.:---->
print("Task #10: Print Final Bank Summary".center(60,"="))
total_customer = len(bank_customers)
savings  = 0 
current = 0
total_balance = 0 

for customer in bank_customers.values():
    if customer ["account_type"] == "Savings":
        savings += 1
    else:
        current += 1

    total_balance += sum(customer["transactions"])        
print("Total Customers: ",total_customer)
print("Savings Accounts: ",savings)
print("Current Accounts: ",current)
print("Total Bank Balance: ",total_balance)

    




































































