products = {
    "p101": {"p_name":"mobile", "p_price":30000},
    "p102": {"p_name":"laptop", "p_price":75000}
}

# access p101 data
# add p101 dis price -->10%
# delete p102 "p_price"
# update p102 price ---->after 15% dis

print("Original products:", products)
 
# ---------------- 1. Access p101 data ----------------
print("\n1. Access p101 data:")
print(products["p101"])
 
# ---------------- 2. Add p101 discount price --> 10% discount ----------------
dis_price = products["p101"]["p_price"] - (products["p101"]["p_price"] * 10/100)
products["p101"]["dis_price"] = dis_price

print("\n2. After adding p101 discount price (10% off):")
print(products["p101"])
 
# ---------------- 3. Delete p102 "p_price" ----------------
# del products["p102"]["p_price"]
# print("\n3. After deleting p102's p_price:")
# print(products["p102"])

removed_price = products["p102"].pop("p_price")
print("\n3. After deleting p102's p_price using pop():")
print(products["p102"])
print("Removed value:", removed_price) 

# ---------------- 4. Update p102 price after 15% discount ----------------
products["p102"]["p_price"] = 75000                     # p_price add zali karan wardhi delete keli hoti
products["p102"]["p_price"] = products["p102"]["p_price"] - (products["p102"]["p_price"] * 15/100)
print("\n4. After updating p102 price (15% discount):")
print(products["p102"])
 
print("\nFinal products:", products)
 
