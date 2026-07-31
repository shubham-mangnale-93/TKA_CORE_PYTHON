shopping_customers = {
    2001: {
        "name": "Rahul",
        "membership": "Gold",
        "location": ("Pune", "Maharashtra"),
        "orders": [2500, 1200, 4500, 800, 6000],
        "products": {"Laptop Bag", "Mouse", "Keyboard", "Mouse"},
        "payment_modes": ["UPI", "Card", "UPI", "Cash", "Card"],
        "delivery_status": ["Delivered", "Delivered", "Pending", "Delivered", "Pending"]
    },

    2002: {
        "name": "Priya",
        "membership": "Silver",
        "location": ("Mumbai", "Maharashtra"),
        "orders": [1500, 3500, 700, 2200],
        "products": {"Shoes", "Watch", "Handbag", "Shoes"},
        "payment_modes": ["Card", "UPI", "Cash", "UPI"],
        "delivery_status": ["Delivered", "Cancelled", "Delivered", "Pending"]
    },

    2003: {
        "name": "Neha",
        "membership": "Gold",
        "location": ("Nashik", "Maharashtra"),
        "orders": [5000, 7500, 1800, 9000, 1200],
        "products": {"Mobile", "Earphones", "Power Bank", "Mobile"},
        "payment_modes": ["UPI", "Card", "Card", "UPI", "Cash"],
        "delivery_status": ["Delivered", "Delivered", "Delivered", "Pending", "Cancelled"]
    },

    2004: {
        "name": "Arjun",
        "membership": "Regular",
        "location": ("Pune", "Maharashtra"),
        "orders": [600, 950, 1300, 400],
        "products": {"T-Shirt", "Jeans", "Shoes", "T-Shirt"},
        "payment_modes": ["Cash", "Cash", "UPI", "Card"],
        "delivery_status": ["Delivered", "Delivered", "Pending", "Delivered"]
    }
}
'''

## Tasks

### Task #1: Print all customer names

Print the customer ID and customer name of every customer.

### Task #2: Print Gold membership customers

Find and print all customers whose membership type is `"Gold"`.

### Task #3: Calculate total order amount

Calculate and print the total amount spent by every customer.

Example:

```text
Rahul: ₹15000
Priya: ₹7900
```

### Task #4: Find high-value customers

Print customers whose total order amount is greater than ₹15,000.

### Task #5: Find expensive orders

Print all individual orders whose amount is greater than ₹5,000.

Also print the customer name with the order amount.

### Task #6: Print the last three orders in reverse order

For every customer:

1. Select the last three orders.
2. Reverse their order.
3. Print the result.

### Task #7: Print unique products

Print the unique products purchased by every customer.

Also print the total number of unique products.

### Task #8: Find Pune customers

Print all customers whose city is `"Pune"`.

Use the city value stored inside the `location` tuple.

### Task #9: Assign customer category

Assign a customer category based on their total order amount:

* Total above ₹20,000 → `"Premium Customer"`
* Total from ₹10,000 to ₹20,000 → `"Regular Customer"`
* Total below ₹10,000 → `"Low-Value Customer"`

Print the name, total amount, and customer category.

### Task #10: Print final shopping summary

Print the following information:

* Total number of customers
* Total sales amount
* Total number of Gold customers
* Total number of Pune customers
* Total number of pending deliveries
* Total number of cancelled deliveries
* Customer with the highest spending
* Customer with the lowest spending

## Concepts Used

```text
dictionary = customer-wise shopping data
list       = orders, payment modes and delivery statuses
set        = unique product names
tuple      = fixed city and state information
range      = index-based order and delivery processing
if         = membership, spending and delivery conditions
for        = process all customers and their order details
```
'''
#=============================================================================================================
## Task #1: Print all customer names
print("Task 1: All Customer Names")
for customer_id, customer in shopping_customers.items():
    print(customer_id, "-", customer["name"])


### Task #2: Print Gold membership customers
print("\nTask 2: Gold Membership Customers")
for customer_id, customer in shopping_customers.items():
    if customer["membership"] == "Gold":
        print(customer_id, "-", customer["name"])  


## Task #3: Calculate total order amount
print("\nTask 3: Total Order Amount")
for customer_id, customer in shopping_customers.items():
    total_amount = sum(customer["orders"])
    print(customer["name"], "- ₹", total_amount)


## Task #4: Find high-value customers
#A high-value customer has spent more than ₹15,000.
print("\nTask 4: High-Value Customers")
for customer_id, customer in shopping_customers.items():
    total_amount = sum(customer["orders"])

    if total_amount > 15000:
        print(customer["name"], "- ₹", total_amount)              


## Task #5: Find expensive orders
#Print individual orders above ₹5,000.

print("\nTask 5: Orders Above ₹5,000")
for customer_id, customer in shopping_customers.items():
    for order_amount in customer["orders"]:
        if order_amount > 5000:
            print(customer["name"], "- ₹", order_amount)


## Task #6: Print last three orders in reverse order
print("\nTask 6: Last Three Orders in Reverse Order")
for customer_id, customer in shopping_customers.items():
    last_three_orders = customer["orders"][-3:]
    reverse_orders = last_three_orders[::-1]
    # print(last_three_orders)
    print(customer["name"], "-", reverse_orders)            


### Using `range()`
print("\nTask 6 Using Range")

for customer_id, customer in shopping_customers.items():
    orders = customer["orders"]

    print(customer["name"], end=": ")

    start_index = len(orders) - 1
    stop_index = max(len(orders) - 4, -1)

    for index in range(start_index, stop_index, -1):
        print(orders[index], end=" ")

    print()


## Task #7: Print unique products
print("\nTask 7: Unique Products")
for customer_id, customer in shopping_customers.items():
    products = customer["products"]

    print(customer["name"])
    print("Products:", products)
    print("Total Unique Products:", len(products))
    print()    


## Task #8: Find Pune customers
print("\nTask 8: Pune Customers")
for customer_id, customer in shopping_customers.items():
    city = customer["location"][0]

    if city == "Pune":
        print(customer_id, "-", customer["name"])


## Task #9: Assign customer category
'''Assign a customer category based on their total order amount:
* Total above ₹20,000 → `"Premium Customer"`
* Total from ₹10,000 to ₹20,000 → `"Regular Customer"`
* Total below ₹10,000 → `"Low-Value Customer"`
'''
print("\nTask 9: Customer Risk Category")
for customer_id, customer in shopping_customers.items():
    total_amount = sum(customer["orders"])

    if total_amount > 20000:
        category = "Premium Customer"

    elif total_amount >= 10000:
        category = "Regular Customer"

    else:
        category = "Low-Value Customer"

    print(
        customer["name"],
        "- Total: ₹",
        total_amount,
        "- Category:",
        category
    )


'''    
### Task #10: Print final shopping summary

Print the following information:
* Total number of customers
* Total sales amount
* Total number of Gold customers
* Total number of Pune customers
* Total number of pending deliveries
* Total number of cancelled deliveries
* Customer with the highest spending
* Customer with the lowest spending
'''
print("\n10. Final Shopping Summary")

total_sales = 0
gold_count = 0
pune_count = 0
pending_count = 0
cancelled_count = 0

customer_totals = {}

for customer_id, customer in shopping_customers.items():

    customer_total = sum(customer["orders"])
    customer_totals[customer["name"]] = customer_total

    total_sales += customer_total

    if customer["membership"] == "Gold":
        gold_count += 1

    if customer["location"][0] == "Pune":
        pune_count += 1

    for status in customer["delivery_status"]:
        if status == "Pending":
            pending_count += 1

        elif status == "Cancelled":
            cancelled_count += 1


highest_customer = max(customer_totals, key=customer_totals.get)
lowest_customer = min(customer_totals, key=customer_totals.get)

print("Total Customers:", len(shopping_customers))
print("Total Sales: ₹", total_sales)
print("Gold Customers:", gold_count)
print("Pune Customers:", pune_count)
print("Pending Deliveries:", pending_count)
print("Cancelled Deliveries:", cancelled_count)

print(
    "Highest Spending Customer:",
    highest_customer,
    "- ₹",
    customer_totals[highest_customer]
)

print(
    "Lowest Spending Customer:",
    lowest_customer,
    "- ₹",
    customer_totals[lowest_customer]
)



















