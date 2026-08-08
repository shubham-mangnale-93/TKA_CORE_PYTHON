'''
# PRODUCT MANAGEMENT SYSTEM:----------->>
'''
products = {
    101: {
        "pname": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "stock": 10
    },
    102: {
        "pname": "Mouse",
        "category": "Electronics",
        "price": 800,
        "stock": 25
    },
    103: {
        "pname": "Keyboard",
        "category": "Electronics",
        "price": 1500,
        "stock": 15
    },
    104: {
        "pname": "Headphones",
        "category": "Electronics",
        "price": 2500,
        "stock": 20
    }
}

#----------------------------------------------------------------------------------------------
# Add Product:
def add():
    pid = int(input("Enter Product ID: "))

    if pid in products:
        print("Product already exists")
        return

    pname = input("Enter Product Name : ")
    category = input("Entery Category : ")
    price = int(input("Enter Price : "))
    stock = int(input("Enter Stock : "))

    products[pid] = {
        "pname": pname,
        "category": category,
        "price": price,
        "stock": stock
    }
    
    print("Product added successfully!")
#----------------------------------------------------------------------------------
#Update Stock:
def update_stock():
    pid = int(input("Enter product ID:"))

    if pid in products:
        stock = int(input("Enter New Stock : "))
        products[pid]["stock"] = stock
        print("Stock Updated Successfully!")
    else:
        print("Product Not Found!")
#----------------------------------------------------------------------------------
# Update_Price:
def update_price():
    pid = int(input("Enter Product ID: "))

    if pid in products:
        price = int(input("Enter New Price : "))
        products[pid]["price"] = price
        print("Price Updated Successfully!")
    else:
        print("Product Not Found!")
#----------------------------------------------------------------------------------
# Search Product:
def search_product():
    pid = int(input("Enter Product ID: "))

    if pid in products:
        print("\n========== PRODUCT DETAILS ==========")

        print("Product ID:",pid)
        print("Product Name:",products[pid]["pname"])
        print("Category:",products[pid]["category"])
        print("price:",products[pid]["price"])
        print("Stock:",products[pid]["stocks"])
    else:
        print("Product Not Found!")

#----------------------------------------------------------------------------------
# Display Product:

def display():
    print("\n========== ALL PRODUCTS ==========")
    for pid,details in products.items():
        print("Product ID :", pid)
        print("Product Name :", details["pname"]) 
        print("Category :", details["category"]) 
        print("Price :", details["price"]) 
        print("Stock :", details["stock"])

        print("---------------------------------")
#----------------------------------------------------------------------------------
# Menu:
def menu():
    while True:
        print(''' 
        ========== PRODUCT MANAGEMENT SYSTEM ========== 

        1. Add Product
        2. Update Stock
        3. Update Price
        4. Search Product
        5. Display Products
        6. Exist
        ===============================================                             
        ''')

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            add()

        elif choice == 2:
            update_stock

        elif choice == 3:
            update_price

        elif choice == 4:
            search_product

        elif choice == 5:
            display()

        elif choice == 6:
            print("Thank YOU!")
            break 

        else:
            print("Invalid Choice")
#----------------------------------------------------------------------------------
# Calling Menu:
menu()
#----------------------------------------------------------------------------------


