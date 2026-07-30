pin = 1234
for i in range(3):
    p = int(input("Enter Your Pin :" ))
    if p==pin:
        print("Correct Pin!")
        print("Transaction Successfully!")
        break
    else:
        print("Incorrect Pin")
else:
    print("\nCard Blocked")

