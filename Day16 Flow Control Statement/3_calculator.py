'''
Task :
 "WAP to create a simple calculator using nested if-else (without using elif)
  that performs addition, subtraction, multiplication, and division based on user input operator."
'''
# num1 = eval (input("Enter First Number: "))
# num2 = eval (input("Enter Second Number: "))

# op = input("Enter Operator (+,-,*,/,%): ")

# if op=="+":
#     print("Addition: ",num1 + num2)

# if op=="-":
#     print("Substraction: ",num1 - num2)

# if op=="*":
#     print("Multiplication: ",num1 * num2)  

# if op=="/":
#     print("Division: ",num1 / num2)

# if op=="%":
#     print("Modulus: ",num1 % num2)    

#--------------------------------------------------------------------------------------------
print("=" * 40)
print("     SIMPLE CALCULATOR 🧮")
print("=" * 40)
num1 = eval (input("Enter First Number: "))
op = input("Enter Operator (+,-,*,/,%): ")
num2 = eval (input("Enter Second Number: "))

# op = input("Enter Operator (+,-,*,/,%): ")

if op=="+":
    print("Addition: ",num1+num2)
else:
    if op=="-":
        print("Substraction: ",num1-num2)

    else:
        if op=="*":
            print("Multiplication: ",num1 * num2)

        else:
            if op=="/":
                print("Division: ",num1 / num2)

            else:
                if op=="%":
                    print("Modulus: ",num1 % num2)
                else:
                    print("Invalid Operator! Please enter +, -, *, / or %")

print("=" * 40)                    
print("THANK YOU FOR USING!".center(40, " "))
print("=" * 40)                


        
               


         


