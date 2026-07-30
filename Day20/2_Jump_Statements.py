'''
# Transfer Statement:------------->
1) pass : pass is a placeholder statement. 
It does nothing and is used when a statement is required syntactically, but you don't want to write any code yet.

2) continue : continue skips the current iteration of the loop and moves to the next iteration.
3) break : break immediately terminates the loop and exits from it.
'''
# pass:----->
# product_mrp = eval(input("MRP: "))
# if product_mrp > 30000:
#     print("apply 10 % dis")
# elif product_mrp > 20000:
#     print("5 % dis")
# elif product_mrp > 10000:
#     pass
# elif product_mrp > 5000:
#     print("3% dis")
#------------------------------------------------------------------------------------

# continue:----->
# numbers = [10, 20, 30, 40, 50, 60]
# for i in numbers:
#     if i == 40:
#         continue
#     print(i)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in numbers:
#     if i % 2 == 0:
#         continue
#     print(i)

# for num in range(1,11):
#     if num==5:
#         continue  
#     print(num)  
#------------------------------------------------------------------------------------

# break:----->
for num in range(1,11):
    if num==5:
        break  
    print(num)  

students = {"Amit": 85, "Sneha": 92, "Raj": 78, "Priya": 95, "Vikas": 60}

for name, marks in students.items():
    if name == "Raj":
        print(f"{name} sapadla! Marks: {marks}")
        break
    print(name, "->", marks)    