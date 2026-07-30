# if-elif-else:----->
'''
The if-elif-else statement is used to check multiple conditions and execute the matching block of code.
syntax: if con1:
            #code1
        elif con2:
            #code2
        elif con3:
            # code3  
        elif con4:
            # code4
        else:
            # code      
'''
# print("start")
# num = int (input("Enter The Number: "))

# if num>0:
#     print(f"{num} is Positive Number")
# elif num<0:
#     print(f"{num} is Negative Number")    
# else:
#     print(f"{num} is Zero")
# print("THE END")  
#------------------------------------------------------------------------------------

# print("Welcome")
# age = int(input("Enter Age: "))

# if age<18:
#     print("You Are Child")
# elif age<60:
#     print("You Are Adult")
# else:
#     print("You Are SS")
# print("THANK YOU!")   
#------------------------------------------------------------------------------------

# Divisibility check:----->

# num = int (input("Enter The Number: "))

# if num%3==0:
#     print("Divisible by 3")
# elif num%5==0:
#     print("Divisible by 5")
# elif num%3==0 and num%5==0:
#     print("Divisible by 3 or 5")
# else:
#     print("Not Divisible by 3 or 5")
# print("THE END")            
#------------------------------------------------------------------------------------

# Grade calculator:----->

# marks = eval(input("Enter The Marks: "))

# if marks>=90:
#     print("Grade A")
# elif marks<=89 and marks>=75:
#     print("Grade B")    
# elif marks>=60 and marks<=74:
#     print("Grade C")    
# elif marks>=40 and marks<=59:
#     print("Grade D")    
# else:    
#     print ("Below 40 Fail")


#Method 2:----->
# marks = eval(input("Enter Marks: "))

# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 60:
#     print("C")
# elif marks >= 40:
#     print("D")
# else:
#     print("Fail")

#------------------------------------------------------------------------------------

# Bill-Amount:-------->
# user bill?, if bill>2000 dis15%, if bill 1500-2000 dis 10%, bill<1500 dis5%, bill<1000 dis no%

# METHOD 1:------------------>
# bill_amount = eval(input("Enter Your Bill Amount: "))

# if bill_amount >= 2000:
#     dis_amount = bill_amount * 15 / 100
#     final_bill = bill_amount - dis_amount
#     print(f"Final Bill Amount after 15 per dis : {final_bill}")

# elif bill_amount >= 1500:
#     dis_amount = bill_amount * 10 / 100
#     final_bill = bill_amount - dis_amount
#     print(f"Final Bill Amount after 10 per dis : {final_bill}")

# elif bill_amount >= 1000:
#     dis_amount = bill_amount * 5 / 100
#     final_bill = bill_amount - dis_amount
#     print(f"Final Bill Amount after 5 per dis : {final_bill}")

# else:
#     print(f"No discount, final bill amount: {bill_amount}")


# METHOD 2:------------------>
# bill_amount = eval(input("Enter Your Bill Amount: "))

# if bill_amount >= 2000:
#     dis_amount = bill_amount * 15 / 100
#     dis = 15

# elif bill_amount >= 1500:
#     dis_amount = bill_amount * 10 / 100
#     dis = 10

# elif bill_amount >= 1000:
#     dis_amount = bill_amount * 5 / 100
#     dis = 5

# else:
#     dis_amount = 0
#     dis = 0
#     print(f"No discount, final bill amount: {bill_amount}")

# final_bill = bill_amount - dis_amount
# print(f"Final Bill Amount after {dis} per dis : {final_bill}")

#------------------------------------------------------------------------------------

# product_mrp = {"p1":70000,"p2":40000,"p3":20000,"p4":10000,"p5":30000,"p6":90000,"p7":44000}
# METHOD 1:-------------->

# product_price = {}
# for n, price in product_mrp.items():
#     # print(p)
#     if price<=10000:
#         disc = price*5/100
#         sp = price - disc
#         product_price[n] = sp
#     elif price<=35000:
#         disc = price*10/100
#         sp = price - disc
#         product_price[n] = sp
#     elif price<=65000:
#         disc = price*15/100
#         sp = price - disc
#         product_price[n] = sp    
#     else:
#         disc = price*20/100
#         sp = price - disc
#         product_price[n] = sp  
# print ("new selling price after discount: ",product_price) 


# METHOD 2:-------------->
product_mrp = {
    "p1": 70000,
    "p2": 40000,
    "p3": 20000,
    "p4": 10000,
    "p5": 30000,
    "p6": 80000,
    "p8": 65000
}

product_sp = {}
for pname, mrp in product_mrp.items():

    if mrp <= 10000:
        sp = mrp - mrp * 5 / 100
        # var[key] = value
        product_sp[pname] = sp

    elif mrp <= 35000:
        sp = mrp - mrp * 10 / 100
        product_sp[pname] = sp

    elif mrp <= 65000:
        sp = mrp - mrp * 15 / 100
        product_sp[pname] = sp

    else:
        sp = mrp - mrp * 20 / 100
        product_sp[pname] = sp

print(product_sp)
  
#------------------------------------------------------------------------------------


        
































