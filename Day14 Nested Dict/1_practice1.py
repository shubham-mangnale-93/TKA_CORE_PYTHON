# wap to percentage 
students = {
    "kunal kale": {"t1":45, "t2":89, "t3":67},
    "umesh jadhav": {"t1":65, "t2":79, "t3":87}
}
percentage = {}

for name, marks_data in students.items():
    obt=0
    for mk in marks_data.values():
        # print(mk)
        obt = obt + mk
    total = len(marks_data)*100
    per = obt/total*100
    percentage[name] = per    
print(percentage)  
    
#------------------------------------------------------------------------------------------------

# Total Bill amount = {"kunal kale":7000, ....} 
orders = {
    "kunal kale": {"p1":3000, "p2":4000},
    "om yadav": {"p4":2000, "p5":9000, "p8":4000}
}

total_bill = {}   # empty dictionary -- result will be stored here

for name, products in orders.items():
    amount = 0                          # counter starts at 0 for each customer
    for price in products.values():     # products.values() = only the prices (3000, 4000, etc.)
        amount = amount + price          # each price added to the running total
    total_bill[name] = amount            # total bill stored against that customer's name

print(total_bill)
#------------------------------------------------------------------------------------------------

# wap to cal total sales:--->
orders = {
    "kunal kale": {"p1":3000, "p2":4000},
    "om yadav": {"p4":2000, "p5":9000, "p8":4000}
}
total_sales = 0
for sales in orders.values():
    # print(sales)
    for i in sales.values():
        # print(i)
        total_sales = total_sales + i
print(total_sales)        
#------------------------------------------------------------------------------------------------

#15% discount on every product:--->
orders = {
    "kunal kale": {"p1":3000, "p2":4000},
    "om yadav": {"p4":2000, "p5":9000, "p8":4000}
}
total_bill = {}

for name, order_data in orders.items():
    total = 0
    for mrp in order_data.values():
        total = total + (mrp - mrp*15/100)    
    total_bill[name] = total

print(total_bill)
#--------------------------------------------------------------------------------------------

emp = {
    "rahul yadav": {"basic":30000, "HRA":10, "DA":5},
    "mohan raut": {"basic":40000, "HRA":9, "DA":6},
    "rajesh patil": {"basic":20000, "HRA":15, "DA":8}
}
# {"rahul yadav":40000, .....}

emp_sal = {}
for name,sal_data in emp.items():
    basic_sal = sal_data["basic"]
    hra_per = sal_data["HRA"]
    da_per = sal_data["DA"]
    hra = basic_sal * hra_per/100
    da = basic_sal*da_per/100
    salary = basic_sal+hra+da
    emp_sal[name] = salary

print(emp_sal)
