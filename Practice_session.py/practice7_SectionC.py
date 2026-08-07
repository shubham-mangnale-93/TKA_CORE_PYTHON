'''
Product Dictionary Tasks
Use this dictionary for Tasks 31-40:
'''
products = {
 "P101": {"name": "Laptop", "price": 55000, "stock": 8},
 "P102": {"name": "Mouse", "price": 700, "stock": 25},
 "P103": {"name": "Keyboard", "price": 1200, "stock": 15},
 "P104": {"name": "Monitor", "price": 14000, "stock": 5},
 "P105": {"name": "Headphones", "price": 2500, "stock": 0}
}

# 31. Print the name and price of every product.
for product_id, details in products.items():
    print(details["name"],"-",details["price"])
print("--"*40)

# 32. Print products having stock less than 10.
for product_id, details in products.items():
     if details["stock"]<10:
          print(details["name"],"-",details["stock"])
print("--"*40)

# 33. Print products that are out of stock.
for product_id, details in products.items():
     if details["stock"]==0:
          print(product_id,"-",details["name"],"-","out of stock this product")
print("--"*40)

# 34. Calculate the total value of each product using price x stock.
for product_id, details in products.items():
     total_value = details["price"]*details["stock"]
     print(product_id,"-",details["name"],"-","Total value:",total_value)
      
print("--"*40)

# 35. Find the most expensive product.
highest_price = 0
expensive_product_id = None
expensive_product_name = None

for product_id, details in products.items():
    if details["price"] > highest_price:
        highest_price = details["price"]
        expensive_product_id = product_id
        expensive_product_name = details["name"]
print(expensive_product_id, "-", expensive_product_name, "-", highest_price)
print("--"*40)
          
# 36. Find the cheapest product.
cheapest_price = 100000
cheapest_product_id = None
cheapest_product_name = None

for product_id, details in products.items():
    if details["price"] < cheapest_price:
        cheapest_price = details["price"]
        cheapest_product_id = product_id
        cheapest_product_name = details["name"]
print(cheapest_product_id, "-", cheapest_product_name, "-", cheapest_price)
print("--"*40)

# 37. Create a list containing the names of all available products.
available_products = []
for product_id, details in products.items():
    if details["stock"]>0:
        available_products.append(details["name"])
print("37.Available Products",available_products)         
print("--"*40)

# 38. Create a dictionary containing product name as key and stock as value.
name_stock = {}
for product_id, details in products.items():
    name_stock[details["name"]] = details["stock"]
print(name_stock)
print("--"*40)

# 39. Update the stock of product P104 to 12.
products["P104"] ["stock"] = 12
print("39.Update the stock of product P104 to 12:",products["P104"])
#------------------------------------------------
# for product_id, details in products.items():
#     if product_id == "P104":
#         details["stock"] = 12
# print(products["P104"])
print("--"*40)

# 40. Apply a 5% discount to all products costing more than 10,000
for product_id, details in products.items():
    if details["price"]>10000:
        details["price"] = details["price"]*5/100
print("40.Apply a 5% discount to all products costing more than 10,000:",products)
print("--"*40)      
