# ==========================================
#         ATM MANAGEMENT SYSTEM
# ==========================================

pin = 932572
balance = 10000

transactions = []
transaction_count = 0
total_deposit = 0
total_withdraw = 0

# -------------------------------
# LOGIN SYSTEM (3 Attempts)
# -------------------------------
for attempt in range(1,4):
    print(f"\nAttempt {attempt} of 3")
    entered_pin = int(input("Enter Your PIN: "))
    if entered_pin == pin:
        print("Login Successful!")
        break
    else:
        print("Incorrect PIN")
else:
    print("Card Blocked!")
    raise SystemExit

while True:
    print("\n==============================")
    print("         ATM MENU")
    print("==============================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Mini Statement")
    print("6. Fast Cash")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print(f"Current Balance: ₹{balance}")

    elif choice == 2:
        amount = int(input("Enter Deposit Amount: "))
        if amount > 0:
            balance += amount
            total_deposit += amount
            transaction_count += 1
            transactions.append(f"Deposit : ₹{amount}")
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = int(input("Enter Withdraw Amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            total_withdraw += amount
            transaction_count += 1
            transactions.append(f"Withdraw : ₹{amount}")
            print("Withdrawal Successful")
        elif amount <= 0:
            print("Invalid Amount")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        old = int(input("Enter Old PIN: "))

        if old == pin:
            new = int(input("Enter New 6-digit PIN: "))
            confirm = int(input("Confirm New PIN: "))
            
            if len(str(new)) == 6 and new == confirm:
                pin = new
                print("PIN Changed Successfully")
            elif new != confirm:
                print("PIN Mismatch")
            else:
                print("PIN must be 6 digits")
        else:
            print("Wrong Old PIN")

    elif choice == 5:
        print("\n========= MINI STATEMENT =========")
        if not transactions:
            print("No Transactions")
        else:
            for t in transactions:
                print(t)
        print("--------------------------------")
        print("Total Deposit    :", total_deposit)
        print("Total Withdraw   :", total_withdraw)
        print("Transactions     :", transaction_count)
        print("Current Balance  :", balance)

    elif choice == 6:
        print("\nFast Cash")
        print("1. ₹500")
        print("2. ₹1000")
        print("3. ₹2000")
        print("4. ₹5000")
        fc = int(input("Select Option: "))
        mapping = {1:500,2:1000,3:2000,4:5000}
        if fc in mapping:
            amt = mapping[fc]
            if amt <= balance:
                balance -= amt
                total_withdraw += amt
                transaction_count += 1
                transactions.append(f"Fast Cash : ₹{amt}")
                print(f"₹{amt} Withdrawn Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Option")

    elif choice == 7:
        print("Thank You For Using Our ATM.")
        break

    else:
        print("Invalid Choice")
