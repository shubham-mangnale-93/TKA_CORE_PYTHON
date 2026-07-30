# Task 1 - wap to cal simple interest :

#data
principle = float(input("Enter Principle: "))
rate = float(input("Enter Rate (%): "))
time = float(input("Enter Time (y): "))

#logic
Simple_Interest = principle * rate * time /100

Total_Amount = principle + Simple_Interest

#display
print(f"Simple Interest: {Simple_Interest} \nTotal Amount: {Total_Amount}")
