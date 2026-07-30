# ==========================================
#         ATM MANAGEMENT SYSTEM
# ==========================================

# -------------------------------
# Initial Data:------>>>
# -------------------------------

pin = 932572
balance = 10000

# Store all transactions:----->>>
transactions = []

# Login System (3 attempts):----->>>
for attempt in range(3):
    entered_pin = int(input("Enter Your Pin : "))
    if entered_pin==pin:
        print("\nCorrect PIN!")
        break
    else:
        print("\nIncorrect PIN!")
else:
    print("\nCard Blocked!")
    exit()    

# -------------------------------
# MAIN MENU
# -------------------------------

while True:
    print("\n==============================")
    print("         ATM MENU")
    print("==============================")

    print("1.Check Balance")
    print("2.Deposit Balance")
    print("3.Withdraw Balance")
    print("4.Change PIN")
    print("5.Mini Statement")
    print("6.Exit")

    choice = int(input("\nEnter Your Choice : "))

    # ---------------------------------
    # CHECK BALANCE
    # ---------------------------------
    if choice==1:
        print(f"\n Current Balance : ₹{balance}")

    # ---------------------------------
    # DEPOSIT MONEY
    # ---------------------------------
    elif choice==2:
        amount = int(input("Enter Deposit Amount : "))

        if amount>0:
            balance +=amount

            transactions.append(f"Deposit : ₹{amount}")

            print("Amount Deposited Successfully")
            print("Current Balance : ",balance)

        else:
            print("Invalid Amount!")

    # ---------------------------------
    # WITHDRAW MONEY
    # ---------------------------------
    elif choice==3:
        amount = int(input("Enter Withdraw Amount : "))

        if amount<=balance:
            balance-=amount

            transactions.append(f"Withdraw : ₹{amount}")

            print("Withdraw Successfully")
            print("Remaining Balance : ",balance)
        else:
            print("Insufficient Balance!")

    # ---------------------------------
    # CHANGE PIN
    # ---------------------------------
    elif choice==4:
        old_pin = int(input("Enter Old PIN : "))

        if old_pin==pin:
            new_pin = int(input("Enter New PIN : "))

            pin=new_pin

            print("PIN Changed Successfully")
        else:
            print("Wrong PIN!")

    # ---------------------------------
    # MINI STATEMENT
    # ---------------------------------
    elif choice==5:
         print("\n========= MINI STATEMENT =========")

         if len(transactions) == 0:

            print("No Transactions Found.")

         else:

            for transaction in transactions:

                print(transaction)

         print(f"\nCurrent Balance : ₹{balance}")

     # ---------------------------------
    # EXIT
    # ---------------------------------

    elif choice == 6:

        print("\nThank You For Using Our ATM")
        break

    # ---------------------------------
    # INVALID CHOICE
    # ---------------------------------

    else:

        print("Invalid Choice. Please Try Again.")     






































